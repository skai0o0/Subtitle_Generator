# 🎬 Subtitle Generator Ver 2

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![Status](https://img.shields.io/badge/status-production--ready-brightgreen)

**Ứng dụng desktop tạo subtitle tự động cho video/audio sử dụng AI Whisper**

[Features](#-tính-năng) • [Installation](#-cài-đặt-nhanh) • [Usage](#-sử-dụng) • [Documentation](#-tài-liệu)

</div>

---

## ✨ Tính năng

### 🎬 Video/Audio Player
- ✅ Load và playback đa định dạng (MP4, AVI, MKV, MP3, WAV, ...)
- ✅ Play/Pause/Stop controls
- ✅ Timeline slider với seek
- ✅ Volume control
- ✅ Time display (current/duration)

### 🤖 AI Transcription & Translation
- ✅ Powered by **OpenAI Whisper**
- ✅ **GPU-accelerated** (CUDA primary, CPU fallback)
- ✅ 5 model sizes (tiny → large)
- ✅ **10-15x faster** with NVIDIA GPU
- ✅ **Transcribe mode**: Giữ nguyên ngôn ngữ gốc
- ✅ **Translate mode**: Dịch sang tiếng Anh tự động
- ✅ Multi-threaded processing
- ✅ Progress tracking
- ✅ Hỗ trợ 99+ ngôn ngữ

### 🌍 Multi-language Translation
- ✅ Powered by **Meta NLLB-200**
- ✅ **200+ languages** support
- ✅ 4 model sizes (600M → 3.3B)
- ✅ Context-aware translation (sliding window)
- ✅ GPU acceleration
- ✅ Auto VRAM management

### 📝 Subtitle Management
- ✅ Real-time subtitle display
- ✅ Auto-sync với video
- ✅ Export SRT/VTT format
- ✅ Import SRT files
- ✅ Subtitle editor

### 🎨 Modern UI
- ✅ PySide6 interface
- ✅ Fullscreen mode với overlay controls
- ✅ Menu bar & shortcuts
- ✅ Status notifications
- ✅ Progress dialogs
- ✅ Playlist management

---

## 🚀 Cài đặt nhanh

### 📋 Yêu cầu
- **Python** 3.11.x (khuyến nghị) hoặc 3.8-3.11
- **FFmpeg** (system install)
- **NVIDIA GPU** với CUDA (khuyến nghị, RTX series)
- 4-12GB VRAM (GPU) hoặc 8-16GB RAM (CPU)

### ⚡ Quick Setup

#### Windows PowerShell:
```powershell
# 1. Cài FFmpeg
choco install ffmpeg

# 2. Run setup script
.\setup.ps1

# 3. Test installation
python test_setup.py

# 4. Run app
.\run.ps1
```

#### Manual Setup:
```powershell
# 1. Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run app
python main.py
```

> 📖 **Chi tiết:** Xem [INSTALL.md](INSTALL.md) để biết hướng dẫn đầy đủ

---

## 📖 Sử dụng

### 🎯 Workflow cơ bản

#### Option 1: Transcribe (giữ nguyên ngôn ngữ gốc)
1. **Launch app** → `python main.py`
2. **Open video** → `Ctrl+O`
3. **Transcribe** → Click "🎤 Transcribe with Whisper AI"
4. **Choose mode** → **"Transcribe (Original Language)"**
5. **Choose model** → Khuyến nghị: **base**
6. **Wait** → 2-5 phút (tùy video length)
7. **Review** → Play video để xem subtitle
8. **Export** → Subtitle → Export as SRT/VTT

#### Option 2: Transcribe + Translate (Anh → Ngôn ngữ khác)
1. **Transcribe** → Choose **"Translate to English"**
2. **Wait** → Whisper dịch sang tiếng Anh
3. **Translate** → Menu → Transcribe → **"Translate Subtitles..."**
4. **Choose language** → Chọn ngôn ngữ đích (VD: Vietnamese)
5. **Choose model** → Khuyến nghị: **NLLB-200 Distilled 600M**
6. **Wait** → NLLB dịch sang ngôn ngữ đích
7. **Done** → Subtitle đã được dịch!

> 🎓 **Chi tiết:** Xem [QUICKSTART.md](QUICKSTART.md) hoặc [WORKFLOW.md](WORKFLOW.md)

### ⌨️ Keyboard Shortcuts
- `Ctrl+O` - Open video/audio
- `Ctrl+T` - Start transcription
- `Ctrl+Q` - Quit

---

## 🏗️ Cấu trúc dự án

```
subtitle-generator-ver2/
│
├── 📄 main.py                      # Entry point
├── 📄 requirements.txt             # Dependencies
├── 📄 test_setup.py               # Setup verification
│
├── 🎨 ui/                         # User Interface
│   └── main_window.py            # Main window (500+ lines)
│
├── ⚙️ core/                       # Core Logic
│   ├── video_player.py           # Video player
│   ├── whisper_transcriber.py    # AI transcription
│   ├── nllb_translator.py        # Multi-language translation
│   ├── subtitle_manager.py       # Subtitle management
│   └── playlist_manager.py       # Playlist management
│
├── 🔧 utils/                      # Utilities
│
└── 📚 docs/                       # Documentation
    ├── README.md                  # This file
    ├── INSTALL.md                 # Installation guide
    ├── QUICKSTART.md              # Quick reference
    ├── FEATURES.md                # Feature overview
    ├── WORKFLOW.md                # Workflow guide
    └── CHANGELOG.md               # Version history
```

---

## 💻 Công nghệ

| Technology | Purpose |
|-----------|---------|
| ![PySide6](https://img.shields.io/badge/PySide6-6.6.0-41CD52?logo=qt) | GUI Framework |
| ![Whisper](https://img.shields.io/badge/Whisper-latest-412991?logo=openai) | AI Transcription |
| ![NLLB-200](https://img.shields.io/badge/NLLB--200-Meta_AI-0467DF?logo=meta) | Multi-language Translation |
| ![PyTorch](https://img.shields.io/badge/PyTorch-2.6.0+cu124-EE4C2C?logo=pytorch) | Deep Learning + CUDA |
| ![CUDA](https://img.shields.io/badge/CUDA-12.4-76B900?logo=nvidia) | GPU Acceleration |
| ![Transformers](https://img.shields.io/badge/Transformers-4.35.0+-FFD21E?logo=huggingface) | Hugging Face Models |
| ![FFmpeg](https://img.shields.io/badge/FFmpeg-latest-007808?logo=ffmpeg) | Media Processing |

---

## 📚 Tài liệu

| Document | Description |
|----------|-------------|
| [**INSTALL.md**](INSTALL.md) | 📦 Hướng dẫn cài đặt chi tiết |
| [**CUDA_SETUP.md**](CUDA_SETUP.md) | 🎮 GPU/CUDA setup guide |
| [**QUICKSTART.md**](QUICKSTART.md) | ⚡ Quick start guide |
| [**WORKFLOW.md**](WORKFLOW.md) | 🔄 Workflow diagrams |
| [**FEATURES.md**](FEATURES.md) | ✨ Feature overview |
| [**NLLB_TRANSLATION_GUIDE.md**](NLLB_TRANSLATION_GUIDE.md) | 🌍 Translation guide (200+ languages) |
| [**FULLSCREEN_GUIDE.md**](FULLSCREEN_GUIDE.md) | 🖥️ Fullscreen mode guide |
| [**PLAYLIST_GUIDE.md**](PLAYLIST_GUIDE.md) | 📋 Playlist management |
| [**SUBTITLE_EDITOR.md**](SUBTITLE_EDITOR.md) | ✏️ Subtitle editor guide |
| [**CHANGELOG.md**](CHANGELOG.md) | 📝 Version history |

---

## 📊 Statistics

```
📦 Total Files: 21
💻 Python Code: 1054 lines
📚 Documentation: 6 markdown files
⚙️ Core Modules: 3
🎨 UI Components: 1 main window
```

---

## 🎯 Model Comparison

| Model | Size | Speed | Accuracy | Use Case |
|-------|------|-------|----------|----------|
| tiny | 39 MB | ⚡⚡⚡⚡⚡ | ⭐⭐ | Quick tests |
| **base** | 74 MB | ⚡⚡⚡⚡ | ⭐⭐⭐ | **Recommended** |
| small | 244 MB | ⚡⚡⚡ | ⭐⭐⭐⭐ | Good quality |
| medium | 769 MB | ⚡⚡ | ⭐⭐⭐⭐⭐ | Professional |
| large | 1550 MB | ⚡ | ⭐⭐⭐⭐⭐ | Best quality |

---

## 🔧 Troubleshooting

### Common Issues:

**"FFmpeg not found"**
```powershell
choco install ffmpeg
```

**"Import errors"**
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Slow transcription**
→ Use smaller model (tiny/base)

**Out of memory**
→ Close other apps, use tiny model

> 💡 Xem thêm trong [INSTALL.md](INSTALL.md#xử-lý-lỗi-thường-gặp)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

---

## 📄 License

**MIT License** - See [LICENSE](LICENSE) file for details.

---

## 🎉 Credits

- **Whisper AI** by OpenAI
- **PySide6** by Qt
- **PyTorch** by Facebook AI

---

<div align="center">

**Made with ❤️ using Python, PySide6, and Whisper AI**

⭐ Star this repo if you find it useful!

[Report Bug](https://github.com) • [Request Feature](https://github.com)

</div>
