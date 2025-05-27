from ..utils.text_processor import normalize_text
from .response_data import RESPONSE_MAP


def handle_response(user_input: str) -> str:
    """
    Return a response string based on normalized user input.
    """
    normalized = normalize_text(user_input)
    return RESPONSE_MAP.get(normalized, "Sorry, I don't understand.")
