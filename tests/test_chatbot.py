import unittest
from src.chatbot import ChatBot


class TestChatBot(unittest.TestCase):
    def setUp(self):
        self.bot = ChatBot()

    def test_greeting(self):
        self.assertIn("Hello", self.bot.greeting)

    def test_response_known(self):
        response = self.bot.get_response("hello")
        self.assertEqual(response, "Hi there!")

    def test_response_unknown(self):
        response = self.bot.get_response("unknown input")
        self.assertEqual(response, "Sorry, I don't understand.")


if __name__ == "__main__":
    unittest.main()
