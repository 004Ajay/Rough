import ollama
import json
import fitz  # PyMuPDF
import faiss
import numpy as np
import pandas as pd
import time
import torch
import psutil
import GPUtil
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from rouge_score import rouge_scorer
from bert_score import score
import matplotlib.pyplot as plt

############ Inputs required for the program

pdf_paths = ['AI.pdf']
QnA_File = 'qa.json'
models = ["llama3.2:latest", "granite3-moe:3b"]

def extract_text_from_pdfs(pdf_paths, chunk_size=500):
    all_chunks = []
    for pdf_path in pdf_paths:
        doc = fitz.open(pdf_path)
        text = "".join([page.get_text() for page in doc])
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        all_chunks.extend(chunks)
    return all_chunks

# Initialize embedding model
embedding_model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
pdf_chunks = extract_text_from_pdfs(pdf_paths)
chunk_embeddings = np.array(embedding_model.encode(pdf_chunks, normalize_embeddings=True))

dimension = chunk_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(chunk_embeddings)

def retrieve_top_chunks(query, top_k=3):
    query_embedding = np.array(embedding_model.encode([query], normalize_embeddings=True))
    distances, indices = index.search(query_embedding, top_k)
    return [pdf_chunks[i] for i in indices[0]]

def get_gpu_memory():
    gpus = GPUtil.getGPUs()
    if gpus:
        return max([gpu.memoryUsed for gpu in gpus]) / 1024  # Convert MB to GB
    return 0

def get_cpu_memory():
    return psutil.virtual_memory().used / (1024 ** 3)

def get_model_answer(question, model_name=None):
    retrieved_context = "\n\n".join(retrieve_top_chunks(question))
    prompt = f"Question: {question}\nContext: {retrieved_context}\nAnswer:"
    
    start_time = time.perf_counter()
    start_gpu_mem = get_gpu_memory()
    start_cpu_mem = get_cpu_memory()
    
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
    
    end_time = time.perf_counter()
    end_gpu_mem = get_gpu_memory()
    end_cpu_mem = get_cpu_memory()
    
    latency = round(end_time - start_time, 2)
    gpu_usage = round(end_gpu_mem - start_gpu_mem, 2)
    cpu_usage = round(end_cpu_mem - start_cpu_mem, 2)
    
    return response.message.content, retrieved_context, latency, gpu_usage, cpu_usage

def compute_bert_score(hypothesis, reference):
    P, R, F1 = score([hypothesis], [reference], lang="en")
    return F1.item()

def compute_rouge_score(hypothesis, reference):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    return scorer.score(reference, hypothesis)

def compute_cosine_similarity(hypothesis, reference):
    emb1 = embedding_model.encode([hypothesis], normalize_embeddings=True)
    emb2 = embedding_model.encode([reference], normalize_embeddings=True)
    return cosine_similarity(emb1, emb2)[0][0]

with open(QnA_File, 'r') as f:
    qa_pairs = json.load(f)

results = {model: [] for model in models}

for pair in qa_pairs:
    question = pair['question']
    real_answer = pair['real_answer']
    
    for model_name in models:
        model_answer, used_context, latency, gpu_usage, cpu_usage = get_model_answer(question, model_name)
        
        bert_score = round(compute_bert_score(model_answer, real_answer), 2)
        rouge_score = compute_rouge_score(model_answer, real_answer)
        cosine_sim = round(compute_cosine_similarity(model_answer, real_answer), 2)
        
        results[model_name].append({
            'question': question,
            'real_answer': real_answer,
            'model_answer': model_answer,
            'retrieved_context': used_context,
            'bert_score': bert_score,
            'rouge1_fmeasure': rouge_score['rouge1'].fmeasure,
            'rouge2_fmeasure': rouge_score['rouge2'].fmeasure,
            'rougeL_fmeasure': rouge_score['rougeL'].fmeasure,
            'cosine_similarity': cosine_sim,
            'latency_sec': latency,
            'gpu_usage_gb': gpu_usage,
            'cpu_usage_gb': cpu_usage
        })

df = pd.DataFrame([{**result, 'model_name': model} for model, results_list in results.items() for result in results_list])
df.to_csv("Model_Comparison_with_Latency.csv", index=False)

avg_scores = df.groupby('model_name')[['bert_score', 'rouge1_fmeasure', 'rouge2_fmeasure', 'rougeL_fmeasure', 'cosine_similarity', 'latency_sec', 'gpu_usage_gb', 'cpu_usage_gb']].mean()
avg_scores.to_csv("Model_Average_Scores_with_Latency.csv")

# Plot
models = avg_scores.index
bar_width = 0.15
index = np.arange(len(models))

fig, ax = plt.subplots(figsize=(12, 6))
bar1 = ax.bar(index - bar_width, avg_scores['bert_score'], bar_width, label='BERT Score', color='blue')
bar2 = ax.bar(index, avg_scores['rouge1_fmeasure'], bar_width, label='ROUGE-1 Fmeasure', color='green')
bar3 = ax.bar(index + bar_width, avg_scores['rouge2_fmeasure'], bar_width, label='ROUGE-2 Fmeasure', color='red')
bar4 = ax.bar(index + 2*bar_width, avg_scores['rougeL_fmeasure'], bar_width, label='ROUGE-L Fmeasure', color='purple')
bar5 = ax.bar(index + 3*bar_width, avg_scores['cosine_similarity'], bar_width, label='Cosine Similarity', color='orange')
bar6 = ax.bar(index + 4*bar_width, avg_scores['latency_sec'], bar_width, label='Latency (sec)', color='cyan')
bar7 = ax.bar(index + 5*bar_width, avg_scores['gpu_usage_gb'], bar_width, label='GPU Usage (GB)', color='pink')
bar8 = ax.bar(index + 6*bar_width, avg_scores['cpu_usage_gb'], bar_width, label='CPU Usage (GB)', color='gray')

def add_labels(bars):
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, round(bar.get_height(), 2), ha='center', va='bottom', fontsize=10)

[add_labels(b) for b in [bar1, bar2, bar3, bar4, bar5, bar6, bar7, bar8]]
ax.set_xlabel('Model Name')
ax.set_ylabel('Scores')
ax.set_title('Model Comparison on RAG Tasks')
ax.set_xticks(index + 2 * bar_width)
ax.set_xticklabels(models)
ax.legend()
plt.tight_layout()
plt.savefig("Model_Performance_with_Latency.jpg")
plt.show()
