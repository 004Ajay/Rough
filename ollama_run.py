# !pip install rouge-score, bert-score, PyMuPDF, ollama, scikit-learn

import ollama
import json
from bert_score import score
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from rouge_score import rouge_scorer
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

pdf_text = extract_text_from_pdf('AI.pdf') # not connected to the model

sys_prompt ="""
You're a helpful assistant, take the context from provided text only 
and then give the citation from where you've taken the answers from.
You just need to give answer to the question asked directly under two or threee 
sentences and no need of big explanations.
"""

def get_model_answer(question, context, model_name=None):
    prompt = f"Question: {question}\nContext: {pdf_text}\nAnswer:"
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt, "system": sys_prompt}])
    return response.message.content

def compute_bert_score(hypothesis, reference):
    P, R, F1 = score([hypothesis], [reference], lang="en")
    return F1.item()

def compute_rouge_score(hypothesis, reference):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    return scorer.score(reference, hypothesis)

def compute_cosine_similarity(hypothesis, reference):
    emb1 = np.random.rand(1, 768)  # Replace with actual embeddings
    emb2 = np.random.rand(1, 768)  # Replace with actual embeddings
    return cosine_similarity(emb1, emb2)[0][0]

# Example question-answer pairs
with open('qa.json', 'r') as f:
    qa_pairs = json.load(f)

# Loop through questions and models
for pair in qa_pairs:
    question = pair['question']
    real_answer = pair['real_answer']
    context = pair.get('context', '')

    model_answers = {}
    for model in ['llama3.2:latest']:  # Add your installed models here
        model_answer = get_model_answer(question, context, model)
        model_answers[model] = model_answer
        
        # Evaluate answers using different metrics
        bert_score = round(compute_bert_score(model_answer, real_answer), 2)
        rouge_score = compute_rouge_score(model_answer, real_answer)
        cosine_sim = round(compute_cosine_similarity(model_answer, real_answer), 2)
        
        print(f"\nMODEL: {model}")
        print(f"\nQuestion: {question}")
        print(f"\nReal Answer: {real_answer}")
        print(f"\nModel's Answer: {model_answer}")
        print(f"\nBERT Score: {bert_score}")
        print(f"\nROUGE Score: {rouge_score}")
        print(f"\nCosine Similarity: {cosine_sim}")
        print("\n")
        print("-x-" * 50)