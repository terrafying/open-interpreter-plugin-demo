import re
import requests


from api.llama_index_manager import LLAMA_Index_Manager
from llama_index import SimpleDirectoryReader

VECTOR_INDEX = 'blah/blah/eriks_vector_index' # 'Brians_Vector_Index'

manager = LLAMA_Index_Manager('vigilant-yeti-400300', 'oi-hackathon', VECTOR_INDEX )

print("LLama Index Manager initialized.")
class InterpreterPlugin:
    def __init__(self, name):
        print(f"Initializing {name} plugin...")
        self.name = name
        self.functions = []
        self.callMap = {}

    def get_functions(self):
        return self.functions

    def register_function(self, function_def, function):
        self.functions.append(function_def)
        self.callMap[function_def["name"]] = function

    def execute_function(self, function_name="", parameters={}):
        if function_name not in self.callMap:
            return {"error": "Function not found"}
        else:
            return self.callMap[function_name](self, **parameters)

plugin = InterpreterPlugin("retriever")

# Retrieve vector store (If you put a path that doesn't exist, it will return a new empty index)
# index = manager.retrieve_index_from_gcs()


def insert():
    global index
    print("Retrieved index successfully.")
    if not index:
        index = manager.retrieve_index_from_gcs()
    # Add docs from local directory
    documents = SimpleDirectoryReader('./test_library', recursive=True).load_data()
    for doc in documents:
        index.insert(doc)

    print("Added documents successfully.")

    # Save index persistently back to gcs
    manager.save_index_to_gcs_from_local(index, 'oi-hackathon', 'blah/blah/eriks_vector_index')

    print("Saved index successfully.")


def retrieve(self, query=""):
    print(f"Retrieve: {query}")
    return manager.retrieve_context([{'message': query}])


plugin.register_function(
    {
        "name": "retrieve",
        "description": "Plugin for searching through the user's documents (such as files, emails, and more) to retrieve relevant information. Use it only when a user asks to remember something about Elon Musk or python documentation, or only if the user tasks you to save information for later. On follow-up questions, DO NOT use this function, just refer to your own context.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query for embedding-based retrieval",
                },
            },
            "required": ["query"],
        },
    },
    function=retrieve,
)
