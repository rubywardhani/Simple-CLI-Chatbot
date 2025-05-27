# 🤖 Chatbot CLI Sederhana

Chatbot sederhana berbasis Command Line Interface (CLI) yang dibuat dengan Python. Chatbot ini dirancang dengan struktur modular dan clean, cocok untuk latihan dan pengembangan lanjutan.

---

## ✨ Fitur

- ✅ Interface CLI yang user-friendly  
- 🧠 Response berdasarkan keyword dan pattern  
- 📝 Logging percakapan otomatis ke file  
- 🧱 Struktur kode modular dan scalable  
- 🧪 Unit testing dengan pytest  
- 🛠️ Tidak menggunakan dependency eksternal  

---

## 🏗️ Struktur Folder

```
Simple-CLI-Chatbot/
├── main.py                     # Entry point utama
├── requirements.txt            # Dependencies
├── requirements-dev.txt        # Dependencies
├── logs/                       # Folder untuk file log
│   └── conversation.log        # Log percakapan (dibuat otomatis)
└── src/                        # Source code utama
    ├── chatbot.py              # Core logic chatbot
    ├── config.py               # Konfigurasi chatbot
    ├── responses/              # Module untuk response
    │   ├── response_handler.py # Handler untuk response
    │   └── response_data.py    # Data keyword dan response
    └── utils/                  # Utilities
        ├── logger.py           # Logger untuk percakapan
        └── text_processor.py   # Processor untuk text input
```

## 🚀 Cara Menjalankan

### Persyaratan
- Python 3.6 atau lebih baru
- Tidak ada dependencies eksternal (menggunakan standard library)

### Langkah-langkah

1. **Clone atau download project ini**
   ```bash
   # Jika menggunakan git
   git clone <repository-url>
   cd chatbot-cli
   
   # Atau extract jika download zip
   ```

2. **Jalankan chatbot**
   ```bash
   python main.py
   ```

3. **Mulai mengobrol!**
   ```bash
Hello! I'm your CLI chatbot. Type 'exit' to quit.
--------------------------------------------------

🧑 Anda: Halo
🤖 Bot: Halo juga! Ada yang bisa saya bantu?

🧑 Anda: Apa kabar?
🤖 Bot: Saya baik-baik saja, terima kasih! Bagaimana dengan Anda?

🧑 Anda: Terima kasih
🤖 Bot: Sama-sama! Senang bisa membantu 😊

🧑 Anda: bye
🤖 Bot: Terima kasih! Sampai jumpa lagi! 👋

```

## Selamat mencoba dan happy coding! 🚀