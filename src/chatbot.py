from .config import GREETING
from .responses.response_handler import handle_response


class ChatBot:
    def __init__(self):
        self.greeting = GREETING

    def get_response(self, user_input: str) -> str:
        """
        Get chatbot response from user input.
        """
        return handle_response(user_input)
