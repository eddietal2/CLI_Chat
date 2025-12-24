from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core import Settings
from .config import YEARS, STORAGE_DIR, GOOGLE_API_KEY, CHUNK_SIZE

Settings.chunk_size = CHUNK_SIZE
if GOOGLE_API_KEY:
    Settings.embed_model = GoogleGenAIEmbedding(api_key=GOOGLE_API_KEY)
else:
    raise ValueError("GOOGLE_API_KEY is required but not set. Please check your .env file or environment variables.")

def setup_indices(doc_set):
    index_set = {}
    for year in YEARS:
        storage_context = StorageContext.from_defaults()
        cur_index = VectorStoreIndex.from_documents(
            doc_set[year], storage_context=storage_context
        )
        index_set[year] = cur_index
        storage_context.persist(persist_dir=STORAGE_DIR / str(year))
    return index_set

def load_indices():
    index_set = {}
    for year in YEARS:
        storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR / str(year))
        cur_index = load_index_from_storage(storage_context)
        index_set[year] = cur_index
    return index_set
