from .response_data import RESPONSE_MAP
from ..utils.text_processor import normalize_text


def handle_response(user_input: str) -> str:
    """
    Match normalized user input to predefined responses.
    """
    normalized = normalize_text(user_input)
    return RESPONSE_MAP.get(normalized, "Sorry, I don't understand.")
