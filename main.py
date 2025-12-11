import custom_console
import sys
import os
from pathlib import Path

# Start main.py
custom_console.clear_console()
custom_console.start_process_timer()

# Unstructured Data
from llama_index.readers.file import UnstructuredReader
loader = UnstructuredReader()
years = [2022, 2021, 2020, 2019]
doc_set = {}
all_docs = []
for year in years:
    year_docs = loader.load_data(
        file=Path(f"./data/UBER/UBER_{year}.html"), split_documents=False
    )
    # insert year metadata into each year
    for d in year_docs:
        d.metadata = {"year": year}
    doc_set[year] = year_docs
    all_docs.extend(year_docs)

# initialize simple vector indices``
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.core import Settings
from llama_index.core.llms import ChatMessage
import google_llm_init as google

Settings.chunk_size = 512
Settings.embed_model = GoogleGenAIEmbedding(api_key=google.GOOGLE_API_KEY)
Settings.llm = google.llm

# Setup VectorStoreIndex, saving it to disk initially
print(f"{custom_console.COLOR_CYAN}Setting Up VectorStoreIndexes for UBER SEC Filings{custom_console.RESET_COLOR}")
index_set = {}
for year in years:
    storage_context = StorageContext.from_defaults()
    cur_index = VectorStoreIndex.from_documents(
        doc_set[year],
        storage_context=storage_context,
    )
    index_set[year] = cur_index
    storage_context.persist(persist_dir=f"./storage/{year}")

# Load an Index from Disk
print(f"{custom_console.COLOR_YELLOW}Loaded UBER SEC files from VectorStoreIndex{custom_console.RESET_COLOR}")
index_set_2 = {}
for year in years:
    storage_context = StorageContext.from_defaults(
        persist_dir=f"./storage/{year}"
    )
    cur_index = load_index_from_storage(
        storage_context,
    )
    index_set_2[year] = cur_index

print(f"\n{custom_console.COLOR_MAGENTA}Vector Store Index: {custom_console.RESET_COLOR}")
print(index_set_2)

# Creating (4) Query Engines (tools) for each VectorStoreIndex
individual_query_engine_tools = [
    QueryEngineTool(
        query_engine=index_set_2[year].as_query_engine(),
        metadata=ToolMetadata(
            name=f"vector_index_{year}",
            description=f"useful for when you want to answer queries about the {year} SEC 10-K for Uber",
        ),
    )
    for year in years
]

# Sub Question Query Engine Init
# Adds the 4 Query Engines from before to one SubQuestionQuery

sub_question_query_engine = SubQuestionQueryEngine.from_defaults(
    query_engine_tools=individual_query_engine_tools,
    llm=google.llm,
)

# Outer Chatbot Agent
# - 
query_engine_tool = QueryEngineTool(
    query_engine=sub_question_query_engine,
    metadata=ToolMetadata(
        name="sub_question_query_engine",
        description="useful for when you want to answer queries that require analyzing multiple SEC 10-K documents for Uber",
    ),
)

# Combine the Tools we defined above into a single list of tools for the agent
tools = individual_query_engine_tools + [query_engine_tool]

# Using ChromaDB
# import chromadb
# from llama_index.vector_stores.chroma import ChromaVectorStore
# CHROMA_API_KEY = os.environ.get("CHROMA_API_KEY")

# # Create a Chroma client and collection
# collection_name = "all-my-documents"
# client = chromadb.CloudClient(
#   api_key= CHROMA_API_KEY,
#   tenant='44d54ab0-4822-4c12-9789-e812bcda1870',
#   database='UBER-10K'
# )

# # Create ChromaDB Collection
# # Uses Embedding all-MiniLM-L6-v2, which is hosted on Hugging Face
# try:
#     collection = client.create_collection(collection_name)
#     print("Created CDB Collection")
# except chromadb.errors.ChromaError as e:
#     print(f"{custom_console.COLOR_YELLOW}Error Creating new ChromaDB Collection:{custom_console.RESET_COLOR} {e}")
#     # sys.exit(1)

# # Add docs to the collection
# try:
#     collection = client.get_collection(collection_name)
#     if collection:
#         print(collection.metadata)

#         doc_one: any
#         doc_two: any
#         doc_three: any
#         doc_four: any


#         with open('./data/UBER/UBER_2019.html', 'r', encoding='utf-8') as f:
#                 doc_one = f.read()
#                 print("Document One: ", doc_one[:500])
#         with open('./data/UBER/UBER_2020.html', 'r', encoding='utf-8') as f:
#                 doc_two = f.read()
#                 # print("Document One: ", doc_two)
#         with open('./data/UBER/UBER_2021.html', 'r', encoding='utf-8') as f:
#                 doc_three = f.read()
#                 # print("Document One: ", doc_three)
#         with open('./data/UBER/UBER_2022.html', 'r', encoding='utf-8') as f:
#                 doc_four = f.read()
#                 # print("Document One: ", doc_four)
#         with open('system_prompt.txt', 'r', encoding='utf-8') as f:
#                 sys_prompt = f.read()
#                 # print("Document One: ", doc_four)
       

#     collection.add(
#         documents=[
#             sys_prompt, 
#             ], # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
#         metadatas=[{"source": "notion"}], # filter on these!
#         ids=["doc2-google"], # unique for each doc
#     )
#     print("Added Documents to ChromaDB")
# except Exception as e:
#     print(f"Error adding Document to ChromaDB-{client.database}: {e}")
#     sys.exit(1)

# sys.exit(0)

# Create Agent
import google_llm_init as google
from llama_index.core.agent.workflow import FunctionAgent
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# system_prompt.txt to be used for Agents' System Prompt.
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    loaded_system_prompt = f.read()
    print(f"{loaded_system_prompt}\n")

agent = FunctionAgent(
    tools=tools,
    llm=google.llm,
    system_prompt=loaded_system_prompt,
    verbose=True,
    name="uber_previous_finance_agent",
    description="AI Agent for Analyzing previous Uber financial years, from 2019 - 2022"
)

async def main():
    custom_console.simple_initializer_spinner(3,f"\n✅ Initial Program Loading complete!\n")
    print(google.llm.metadata)

    # User Input
    while True:
        text_input = input(f"{custom_console.COLOR_CYAN}~ ChiLLama Chat 🤖: {custom_console.RESET_COLOR}")
        if text_input == "exit":
            print("\n" + "-"*30 + " ~ Llama Chat Closing " + "-"*30)
            custom_console.process_timer_elapsed_time_success()
            break
        result = await agent.run(user_msg=text_input)
        response = result
        print(f"Type: {type(response)}, Data: {response._data}")
        print(f"{custom_console.COLOR_YELLOW}\nAgent{custom_console.RESET_COLOR}: {response}\n")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
