import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

class Config_LLM:
    model_name = os.getenv("LLM_MODEL_NAME", "gpt-4o-mini")
    api_key = os.getenv("LLM_API_KEY", "")
    base_url = os.getenv("LLM_BASE_URL", 'https://bothub.chat/api/v2/openai/v1')
    temperature = float(os.getenv("LLM_TEMPERATURE", "0.5"))

# Путь к директории с документами
docs_dir = os.getenv("DOCS_DIR", os.path.join("C:", "Users", "Lenovo", "Desktop", "ИФ", "писянина", "ФМ", "6. модель рваного континуума"))

# Конфигурация RAG
RAG_CONFIG = {
    'similarity_threshold': float(os.getenv("RAG_SIMILARITY_THRESHOLD", "0.5")),
    'search_kwargs': {
        'k': int(os.getenv("RAG_SEARCH_K", "20")),
        'score_threshold': float(os.getenv("RAG_SCORE_THRESHOLD", "0.5"))
    },
    'text_splitter': {
        'chunk_size': int(os.getenv("RAG_CHUNK_SIZE", "512")),
        'chunk_overlap': int(os.getenv("RAG_CHUNK_OVERLAP", "128")),
        'length_function': len,
        'is_separator_regex': False,
        'separators': ["\n\n", "\n", ". ", " ", ""]
    },
    'max_context_length': int(os.getenv("RAG_MAX_CONTEXT_LENGTH", "16000"))
}
