import unittest
from src.chatbot import ChatBot


class TestChatBot(unittest.TestCase):
    def setUp(self):
        self.bot = ChatBot()

    def test_greeting(self):
        self.assertIn("Hello", self.bot.greeting)

    def test_known_response(self):
        self.assertEqual(self.bot.get_response("hello"), "Hi there!")

    def test_unknown_response(self):
        self.assertEqual(self.bot.get_response("who are you"),
                         "Sorry, I don't understand.")


if __name__ == "__main__":
    unittest.main()
