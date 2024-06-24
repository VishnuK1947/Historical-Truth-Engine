from llama_index.embeddings.huggingface import HuggingFaceEmbedding

#generating embeddings
embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

#store it in MongoDB
