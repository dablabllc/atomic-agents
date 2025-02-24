import os
from dataclasses import dataclass
from dotenv import load_dotenv

def get_base_url() -> str:
    """Retrieve Base URL from environment or raise error"""
    base_url = os.getenv("BASE_URL")
    if not base_url:
        raise ValueError("base_url not found. Please set the BASE_URL environment variable.")
    return base_url

def get_api_key() -> str:
    """Retrieve API key from environment or raise error"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
    return api_key

def get_searxng_url() -> str:
    """Retrieve SearXNG Base URL from environment or raise error"""
    searxng_url = os.getenv("SEARXNG_BASE_URL")
    if not searxng_url:
        raise ValueError("searxng_url not found. Please set the SEARXNG_BASE_URL environment variable.")
    return searxng_url

def get_searxng_max_results() -> str:
    """Retrieve SearXNG max results from environment or raise error"""
    searxng_max_results = os.getenv("SEARXNG_MAX_RESULTS")
    if not searxng_max_results:
        raise ValueError("searxng_max_results not found. Please set the SEARXNG_MAX_RESULTS environment variable.")
    return searxng_max_results

def get_fast_llm() -> str:
    """Retrieve FAST_LLM from environment or raise error"""
    fast_llm_results = os.getenv("FAST_LLM")
    if not fast_llm_results:
        raise ValueError("fast_llm_results not found. Please set the FAST_LLM environment variable.")
    return fast_llm_results

def get_smart_llm() -> str:
    """Retrieve SMART_LLM from environment or raise error"""
    smart_llm_results = os.getenv("SMART_LLM")
    if not smart_llm_results:
        raise ValueError("smart_llm_results not found. Please set the SMART_LLM environment variable.")
    return smart_llm_results

def get_vision_llm() -> str:
    """Retrieve VISION_LLM from environment or raise error"""
    vision_llm_results = os.getenv("VISION_LLM")
    if not vision_llm_results:
        raise ValueError("vision_llm_results not found. Please set the VISION_LLM environment variable.")
    return vision_llm_results

def get_embed_llm() -> str:
    """Retrieve EMBED_LLM from environment or raise error"""
    embed_llm_results = os.getenv("EMBED_LLM")
    if not embed_llm_results:
        raise ValueError("embed_llm_results not found. Please set the EMBED_LLM environment variable.")
    return embed_llm_results


@dataclass
class ChatConfig:
    """Configuration for the chat application"""

    load_dotenv()

    api_key: str = get_api_key()  # This becomes a class variable
    model: str = get_fast_llm()
    exit_commands: set[str] = frozenset({"/exit", "exit", "quit", "/quit"})

    def __init__(self):
        # Prevent instantiation
        raise TypeError("ChatConfig is not meant to be instantiated")


# Model Configuration
EMBEDDING_MODEL = "text-embedding-3-small"  # OpenAI's latest embedding model
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Vector Search Configuration
NUM_CHUNKS_TO_RETRIEVE = 3
SIMILARITY_METRIC = "cosine"

# ChromaDB Configuration
CHROMA_PERSIST_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "chroma_db")

# Memory Configuration
MEMORY_SIZE = 10  # Number of messages to keep in conversation memory
MAX_CONTEXT_LENGTH = 4000  # Maximum length of combined context to send to the model
