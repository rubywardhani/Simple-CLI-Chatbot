# 🤖 Chatbot CLI Sederhana

Chatbot sederhana berbasis Command Line Interface (CLI) yang dibuat dengan Python. Chatbot ini dirancang dengan struktur modular dan dapat dikembangkan lebih lanjut.

## ✨ Fitur

- ✅ Interface CLI yang user-friendly
- 🧠 Response berdasarkan keyword dan pattern
- 📝 Logging percakapan otomatis
- 🔧 Struktur modular dan mudah dikembangkan
- 🎯 Response yang bervariasi dan natural
- 📊 Preprocessing text sederhana

## 🏗️ Struktur Folder

```
chatbot-cli/
├── main.py                     # Entry point utama
├── README.md                   # Dokumentasi ini
├── requirements.txt            # Dependencies (opsional)
├── logs/                       # Folder untuk file log
│   └── conversation.log        # Log percakapan (dibuat otomatis)
└── src/                        # Source code utama
    ├── __init__.py
    ├── chatbot.py             # Core logic chatbot
    ├── config.py              # Konfigurasi chatbot
    ├── responses/             # Module untuk response
    │   ├── __init__.py
    │   ├── response_handler.py # Handler untuk response
    │   └── response_data.py   # Data keyword dan response
    └── utils/                 # Utilities
        ├── __init__.py
        ├── logger.py          # Logger untuk percakapan
        └── text_processor.py  # Processor untuk text input
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
   ```
   🤖 Selamat datang di Chatbot Sederhana!
   ==================================================
   Ketik 'quit', 'exit', atau 'bye' untuk keluar
   --------------------------------------------------
   
   🧑 Anda: Halo!
   🤖 Bot: Halo! Apa kabar? Ada yang bisa saya bantu?
   ```

## 💬 Contoh Percakapan

```
🧑 Anda: Hai bot!
🤖 Bot: Hi! Senang bertemu dengan Anda! 😊

🧑 Anda: Apa kabar?
🤖 Bot: Saya baik-baik saja, terima kasih! Bagaimana dengan Anda?

🧑 Anda: Siapa nama kamu?
🤖 Bot: Nama saya ChatBot! Saya di sini untuk mengobrol dengan Anda!

🧑 Anda: Cuaca hari ini panas banget
🤖 Bot: Semoga cuacanya bagus ya! Jangan lupa bawa payung kalau mendung!

🧑 Anda: Terima kasih
🤖 Bot: Sama-sama! Senang bisa membantu! 😊

🧑 Anda: bye
🤖 Bot: Terima kasih! Sampai jumpa lagi! 👋
```

## 🎯 Topik yang Didukung

Chatbot ini dapat merespons berbagai topik:

- **Salam**: hai, halo, hello, selamat pagi/siang/malam
- **Kabar**: apa kabar, bagaimana kabar, how are you
- **Identitas**: nama, siapa kamu, who are you
- **Ucapan terima kasih**: terima kasih, thanks, makasih
- **Cuaca**: cuaca, hujan, panas, cerah, mendung
- **Makanan**: makan, makanan, lapar, nasi, masak
- **Bantuan**: help, bantuan, tolong, gimana, bagaimana
- **Hobi**: hobi, suka, senang, main, bermain
- **Waktu**: waktu, jam, time, sekarang

## 📝 Logging

Semua percakapan akan dicatat secara otomatis di file `logs/conversation.log`:

```
[2024-01-15 14:30:25] USER: Halo bot!
[2024-01-15 14:30:25] BOT: Hi! Senang bertemu dengan Anda! 😊
[2024-01-15 14:30:30] USER: Apa kabar?
[2024-01-15 14:30:30] BOT: Saya baik-baik saja, terima kasih! Bagaimana dengan Anda?
```

## 🔧 Pengembangan Lebih Lanjut

### Menambah Response Baru

1. **Edit file `src/responses/response_data.py`**:
   ```python
   "kategori_baru": {
       "keywords": ["keyword1", "keyword2", "keyword3"],
       "responses": [
           "Response pertama",
           "Response kedua",
           "Response ketiga"
       ]
   }
   ```

2. **Atau gunakan method `add_response_category()`** di `ResponseHandler`

### Fitur yang Bisa Ditambahkan

- **Machine Learning**: Integrasi dengan scikit-learn atau TensorFlow
- **Database**: Menyimpan percakapan di database (SQLite/PostgreSQL)
- **API Integration**: Koneksi ke external API (cuaca, berita, dll)
- **Context Memory**: Mengingat konteks percakapan sebelumnya
- **Sentiment Analysis**: Analisis sentimen yang lebih advanced
- **Voice Interface**: Text-to-speech dan speech-to-text
- **Web Interface**: Membuat web version dengan Flask/FastAPI
- **Multi-language**: Dukungan bahasa lain

### Struktur Code untuk Pengembangan

Code sudah didesain dengan prinsip:
- **Modular**: Setiap komponen terpisah dan bisa ditest sendiri
- **Scalable**: Mudah menambah fitur baru tanpa mengubah core
- **Maintainable**: Code yang bersih dengan dokumentasi yang jelas
- **Extensible**: Interface yang jelas untuk plugin dan extension

## 🧪 Testing

Untuk testing manual, coba berbagai input:

```bash
# Test greeting
python main.py
> hai
> halo bot
> selamat pagi

# Test questions
> apa kabar?
> siapa nama kamu?
> bagaimana cuaca?

# Test edge cases
> (input kosong)
> !@#$%^&*()
> text yang sangat panjang sekali...

# Test exit
> quit
> exit
> bye
```

## 📚 Dependencies

Project ini menggunakan Python standard library saja:
- `os`: File operations
- `datetime`: Timestamp untuk logging
- `random`: Random response selection
- `re`: Regular expressions untuk text processing
- `string`: String operations
- `sys`: System operations

## 🤝 Kontribusi

Untuk berkontribusi:

1. Fork repository ini
2. Buat branch untuk fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -am 'Tambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 📄 Lisensi

Project ini menggunakan lisensi MIT. Bebas digunakan untuk pembelajaran dan pengembangan.

## 🐛 Bug Reports & Feature Requests

Jika menemukan bug atau ingin request fitur baru, silakan:
1. Buka issue di repository
2. Jelaskan bug/fitur yang diinginkan
3. Sertakan langkah-langkah reproduce (untuk bug)

## 📞 Kontak

Jika ada pertanyaan atau butuh bantuan:
- Email: developer@example.com
- GitHub: @username

---

**Selamat mencoba dan happy coding! 🚀**