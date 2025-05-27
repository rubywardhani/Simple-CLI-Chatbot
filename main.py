from src.utils.logger import get_logger
from src.chatbot import ChatBot

logger = get_logger()


def main():
    bot = ChatBot()
    print(bot.greeting)

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("ChatBot: Goodbye!")
                break

            response = bot.get_response(user_input)
            print(f"ChatBot: {response}")
            logger.info(f"User: {user_input} | ChatBot: {response}")

        except KeyboardInterrupt:
            print("\nChatBot: Exiting. Bye!")
            break


if __name__ == "__main__":
    main()
