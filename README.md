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
winget install ffmpeg

# 2. Clone repository
git clone https://github.com/skai0o0/Subtitle_Generator.git

# 3. Open CMD
Open Subtitle_Generator foler
Type "CMD" on the address bar
Enter

# 4. Install Pytorch
- For CPU: pip3 install torch torchaudio torchvision
- For NVIDIA GPUs: pip3 install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cu126
- For NVIDIA RTX 50s GPUs: pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu130

# 5. Install requirements
Auto: run setup.bat
Manual: pip install -r requirements.txt

# 6. Run app
run run.bat
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
├── 📄 LICENSE                      # MIT License
│
├── 🎨 ui/                         # User Interface
│   ├── main_window.py            # Main window (500+ lines)
│   ├── fullscreen_overlay.py     # Fullscreen controls
│   ├── subtitle_editor.py        # Subtitle editor
│   └── playlist_widget.py        # Playlist widget
│
├── ⚙️ core/                       # Core Logic
│   ├── video_player.py           # Video player
│   ├── whisper_transcriber.py    # AI transcription (Whisper)
│   ├── nllb_translator.py        # Multi-language translation (NLLB-200)
│   ├── subtitle_manager.py       # Subtitle management
│   └── playlist_manager.py       # Playlist management
│
├── 🔧 utils/                      # Utilities
│
├── 🧪 tests/                      # Tests & Demos
│   ├── test_setup.py             # Setup verification
│   ├── test_fullscreen.py        # Fullscreen test
│   ├── demo_translation.py       # Translation demo
│   └── demo_transcribe_translate.py  # Full workflow demo
│
├── 🛠️ scripts/                    # Setup & Run Scripts
│   ├── setup.ps1 / setup.bat     # Setup script
│   ├── run.ps1 / run.bat         # Run script
│   └── upload_to_github.ps1      # GitHub upload script
│
└── 📚 docs/                       # Documentation
    ├── INSTALL.md                 # Installation guide
    ├── QUICKSTART.md              # Quick start guide
    ├── CONTRIBUTING.md            # Contribution guidelines
    ├── GITHUB_SETUP.md            # GitHub setup guide
    ├── FEATURES.md                # Feature overview
    ├── WORKFLOW.md                # Workflow guide
    ├── NLLB_TRANSLATION_GUIDE.md  # Translation guide (200+ languages)
    ├── FULLSCREEN_GUIDE.md        # Fullscreen mode guide
    ├── PLAYLIST_GUIDE.md          # Playlist management
    ├── SUBTITLE_EDITOR.md         # Subtitle editor guide
    ├── CUDA_SETUP.md              # GPU/CUDA setup
    ├── PERFORMANCE.md             # Performance benchmarks
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
| [**INSTALL.md**](docs/INSTALL.md) | 📦 Hướng dẫn cài đặt chi tiết |
| [**CUDA_SETUP.md**](docs/CUDA_SETUP.md) | 🎮 GPU/CUDA setup guide |
| [**QUICKSTART.md**](docs/QUICKSTART.md) | ⚡ Quick start guide |
| [**WORKFLOW.md**](docs/WORKFLOW.md) | 🔄 Workflow diagrams |
| [**FEATURES.md**](docs/FEATURES.md) | ✨ Feature overview |
| [**NLLB_TRANSLATION_GUIDE.md**](docs/NLLB_TRANSLATION_GUIDE.md) | 🌍 Translation guide (200+ languages) |
| [**FULLSCREEN_GUIDE.md**](docs/FULLSCREEN_GUIDE.md) | 🖥️ Fullscreen mode guide |
| [**PLAYLIST_GUIDE.md**](docs/PLAYLIST_GUIDE.md) | 📋 Playlist management |
| [**SUBTITLE_EDITOR.md**](docs/SUBTITLE_EDITOR.md) | ✏️ Subtitle editor guide |
| [**CONTRIBUTING.md**](docs/CONTRIBUTING.md) | 🤝 How to contribute |
| [**GITHUB_SETUP.md**](docs/GITHUB_SETUP.md) | 🚀 GitHub setup guide |
| [**CHANGELOG.md**](docs/CHANGELOG.md) | 📝 Version history |

---

## 📊 Statistics

```
📦 Total Files: 45+
💻 Python Code: 13 files (core + ui + utils)
📚 Documentation: 27 markdown files
⚙️ Core Modules: 6 (video, transcription, translation, subtitles, playlist)
🎨 UI Components: 4 (main window, fullscreen, editor, playlist)
🧪 Tests & Demos: 4 files
🛠️ Scripts: 5 files
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

> 💡 Xem thêm trong [INSTALL.md](docs/INSTALL.md#xử-lý-lỗi-thường-gặp)

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
