from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from document_conversion import documents

#generating embeddings
embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

#store it in MongoDB
# Database connection
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

def get_mongo_client(mongo_uri):
    """Establish connection to the MongoDB."""
    try:
        client = pymongo.MongoClient(mongo_uri)
        print("Connection to MongoDB successful")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None


mongo_uri = os.getenv("MONGO_URI")
#print("MONGO_URI:", mongo_uri)
if not mongo_uri:
    print("MONGO_URI not set in environment variables")

mongo_client = get_mongo_client(mongo_uri)

# Ingest data into MongoDB
db = mongo_client["Historical-Turth-Engine"] # Database
collection = db["History-v1"] # Collection

# Insert documents into the collection
collection.insert_many(documents.to_dict())

print("Data ingestion into MongoDB completed")

