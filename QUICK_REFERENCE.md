# 🚀 Quick Reference Card

## Virtual Environment Setup - Python 3.11

### ✅ SETUP HOÀN THÀNH!

```
✓ Python 3.11.9
✓ Virtual Environment: .venv/
✓ All packages installed
✓ Tests passed
```

---

## 📝 IMPORTANT COMMANDS

### 🎯 Run App (Recommended)
```powershell
.\run.ps1
```

### 🔧 Manual Run
```powershell
# Activate venv
.\.venv\Scripts\Activate.ps1

# Run app
python main.py
```

### 🧪 Test Setup
```powershell
python test_setup.py
```

### 📦 Reinstall Packages
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## ⌨️ KEYBOARD SHORTCUTS

| Shortcut | Action |
|----------|--------|
| `Ctrl+O` | Open video/audio |
| `Ctrl+T` | Start transcription |
| `Ctrl+Q` | Quit app |
| `Space` | Play/Pause (when focused) |

---

## 🎬 WORKFLOW

```
1. .\run.ps1
2. Ctrl+O → Load video
3. Click 🎤 Transcribe
4. Choose model (base)
5. Wait 2-5 min
6. Review subtitles
7. Export SRT/VTT
```

---

## 🤖 WHISPER MODELS

| Model | Speed | Quality | RAM |
|-------|-------|---------|-----|
| tiny | ⚡⚡⚡⚡⚡ | ⭐⭐ | 1GB |
| **base** | ⚡⚡⚡⚡ | ⭐⭐⭐ | 1GB ✅ |
| small | ⚡⚡⚡ | ⭐⭐⭐⭐ | 2GB |
| medium | ⚡⚡ | ⭐⭐⭐⭐⭐ | 5GB |
| large | ⚡ | ⭐⭐⭐⭐⭐ | 10GB |

**Recommended:** base

---

## 🆘 QUICK FIXES

### Import Error
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Wrong Python
```powershell
python --version
# Should be: Python 3.11.9
```

### FFmpeg Missing
```powershell
choco install ffmpeg
```

### Permission Error
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📚 DOCUMENTATION

| File | Description |
|------|-------------|
| **SETUP_COMPLETE.md** | Setup summary |
| **QUICKSTART.md** | Quick start guide |
| **WORKFLOW.md** | Detailed workflow |
| **PYTHON_VERSION.md** | Python info |
| **INSTALL.md** | Full installation |

---

## ✅ CHECKLIST

Before running:
- [ ] FFmpeg installed? (`ffmpeg -version`)
- [ ] Virtual env active? (see `(venv)` in prompt)
- [ ] Python 3.11? (`python --version`)
- [ ] Tests passed? (`python test_setup.py`)

---

## 🎯 READY TO GO!

```powershell
.\run.ps1
```

**Happy subtitle creation! 🎬✨**
