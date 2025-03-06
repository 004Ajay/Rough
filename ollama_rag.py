# Install required libraries (if not installed)
# !pip install rouge-score, bert-score, PyMuPDF, ollama, sentence-transformers, faiss-cpu

import ollama
import json
import fitz  # PyMuPDF
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from rouge_score import rouge_scorer
from bert_score import score

### 🔹 Step 1: Load and Chunk PDF ###
def extract_text_from_pdf(pdf_path, chunk_size=500):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n"

    # Chunking text (split into manageable pieces)
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

pdf_chunks = extract_text_from_pdf('AI.pdf')

### 🔹 Step 2: Embed Chunks using a Strong Model ###
embedding_model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def generate_embeddings(chunks):
    return np.array(embedding_model.encode(chunks, normalize_embeddings=True))

chunk_embeddings = generate_embeddings(pdf_chunks)

### 🔹 Step 3: Store Embeddings in FAISS ###
dimension = chunk_embeddings.shape[1]  # Embedding size
index = faiss.IndexFlatL2(dimension)
index.add(chunk_embeddings)  # Add embeddings to FAISS index

### 🔹 Step 4: Retrieve Relevant Chunks Based on Query ###
def retrieve_top_chunks(query, top_k=3):
    query_embedding = np.array(embedding_model.encode([query], normalize_embeddings=True))
    distances, indices = index.search(query_embedding, top_k)
    
    retrieved_chunks = [pdf_chunks[i] for i in indices[0]]
    return retrieved_chunks

### 🔹 Step 5: Use Retrieved Chunks in the LLM ###
sys_prompt = """
You're a helpful assistant. Answer the question **only using the provided context**.
Provide the **citation of the source chunk** where you got the answer from.
Keep answers **concise (2-3 sentences max)**.
"""

def get_model_answer(question, model_name="llama3.2:latest"):
    retrieved_context = "\n\n".join(retrieve_top_chunks(question))  # Use top relevant chunks
    prompt = f"Question: {question}\nContext: {retrieved_context}\nAnswer:"

    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt, "system": sys_prompt}])
    return response.message.content, retrieved_context

### 🔹 Step 6: Evaluate the Model Output ###
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

### 🔹 Step 7: Run RAG on Questions from JSON ###
with open('qa.json', 'r') as f:
    qa_pairs = json.load(f)

for pair in qa_pairs:
    question = pair['question']
    real_answer = pair['real_answer']

    model_answer, used_context = get_model_answer(question)

    # Evaluate performance
    bert_score = round(compute_bert_score(model_answer, real_answer), 2) # write what does these scores mean
    rouge_score = compute_rouge_score(model_answer, real_answer)
    cosine_sim = round(compute_cosine_similarity(model_answer, real_answer), 2)

    print(f"\n📌 **Question:** {question}") # change this style
    print(f"\n✅ **Real Answer:** {real_answer}")
    print(f"\n🤖 **Model's Answer:** {model_answer}")
    print(f"\n📚 **Retrieved Context:**\n{used_context}")
    print(f"\n📊 **BERT Score:** {bert_score}")
    print(f"\n📊 **ROUGE Score:** {rouge_score}")
    print(f"\n📊 **Cosine Similarity:** {cosine_sim}")
    print("\n" + "-x-" * 50)
