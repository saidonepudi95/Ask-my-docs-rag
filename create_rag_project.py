import os

structure = {
    "app": [
        "main.py",
        "config.py",
        "rag_pipeline.py",
        "prompt_template.py",
        "citation_checker.py"
    ],
    "ingestion": [
        "load_documents.py",
        "chunker.py",
        "embedder.py",
        "index_builder.py"
    ],
    "retrieval": [
        "bm25_retriever.py",
        "vector_retriever.py",
        "hybrid_fusion.py",
        "reranker.py"
    ],
    "evaluation": [
        "ragas_eval.py",
        "test_questions.json"
    ],
    "ui": [
        "streamlit_app.py"
    ],
    "data/documents": []
}

root = "ask-my-docs-rag"

for folder, files in structure.items():
    folder_path = os.path.join(root, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        open(os.path.join(folder_path, file), "w").close()

# root files
root_files = ["Dockerfile", "requirements.txt", "README.md"]

for file in root_files:
    open(os.path.join(root, file), "w").close()

print("✅ RAG Project structure created successfully!")
