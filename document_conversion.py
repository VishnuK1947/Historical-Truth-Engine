from llama_index.core import SimpleDirectoryReader

# conversion of books into a set of documents
def documents_creater():
    loader = SimpleDirectoryReader(
        input_dir="./books/",
        recursive=True,
        required_exts=[".epub"],
    )

    documents = loader.load_data()

    return documents

documents = documents_creater()
print(documents[1])