import os
from dataclasses import dataclass
from typing import Set

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


@dataclass
class ChatConfig:
    """Configuration for the chat application"""

    load_dotenv()


    api_key: str = os.getenv("OPENAI_API_KEY")  # This becomes a class variable
    model: str = os.getenv("FAST_LLM")
    exit_commands: Set[str] = frozenset({"/exit", "/quit"})

    def __init__(self):
        # Prevent instantiation
        raise TypeError("ChatConfig is not meant to be instantiated")
