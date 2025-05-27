# 🤖 Simple CLI Chatbot

A simple Command Line Interface (CLI) chatbot built with Python. This chatbot is designed with a modular and clean code structure, suitable for practice and further development.

---

## ✨ Features

- ✅ User-friendly CLI interface  
- 🧠 Keyword and pattern-based responses  
- 🧱 Modular and scalable code structure
- 🛠️ No external dependencies (standard library only)  

---

## 🏗️ Project Structure

```
Simple-CLI-Chatbot/
├── main.py                     # Main entry point
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
├── logs/                       # Log files folder
│   └── conversation.log        # Chat log (created automatically)
└── src/                        # Main source code
    ├── chatbot.py              # Core chatbot logic
    ├── config.py               # Chatbot configuration
    ├── responses/              # Response module
    │   ├── response_handler.py # Response handler
    │   └── response_data.py    # Keyword and response data
    └── utils/                  # Utility functions
        ├── logger.py           # Conversation logger
        └── text_processor.py   # Text input processor
```

## 🚀 Getting Started

### Requirements
- Python 3.6 or higher
- No external dependencies (uses standard library only)

### Steps

1. **Clone or download this project**
   ```bash
   # If using git
   git clone <repository-url>
   cd chatbot-cli
   
   # Or extract if downloaded as a zip
   ```

2. **Run the chatbot**
   ```bash
   python main.py
   ```

3. **Start chatting!**
   ```bash
   Hello! I'm your CLI chatbot. Type 'exit' to quit.
   --------------------------------------------------
   🧑 You: Hello
   🤖 Bot: Hi there!
   
   🧑 You: How are you?
   🤖 Bot: I'm just a bunch of code, but I'm doing great!
   
   🧑 You: Help
   🤖 Bot: Type something like 'hello', or 'how are you'. Type 'exit' to quit.
   
   🧑 You: what is your name
   🤖 Bot: I'm a simple CLI chatbot.
   ```

## Enjoy coding and have fun! 🚀