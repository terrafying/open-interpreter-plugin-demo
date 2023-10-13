from llama_index_manager import LLAMA_Index_Manager
from llama_index import SimpleDirectoryReader

manager = LLAMA_Index_Manager('vigilant-yeti-400300', 'oi-hackathon', 'blah/blah/eriks_vector_index')

print("LLama Index Manager initialized.")
# Retrieve vector store (If you put a path that doesn't exist, it will return a new empty index)
index = manager.retrieve_index_from_gcs()

print("Retrieved index successfully.")
# Add docs from local directory
documents = SimpleDirectoryReader('./test_library', recursive=True).load_data()
for doc in documents:
    index.insert(doc)

print("Added documents successfully.")
# Save index persistently back to gcs
manager.save_index_to_gcs_from_local(index, 'oi-hackathon', 'blah/blah/eriks_vector_index')

print("Saved index successfully.")

print(manager.retrieve_context([{ 'message': 'What is the use of Gaussian Mixture Models here?' }]))
# Now you can retrieve the index from the gcs path again whenever you want and continue adding docs to it and retrieving context from it.

print("Done!")