# 📦 Files to Upload to GitHub - Checklist

## ✅ CORE FILES (Bắt buộc)

### Entry Point
- [x] `main.py` - Application entry point

### Core Logic
- [x] `core/__init__.py`
- [x] `core/video_player.py` - Video playback
- [x] `core/whisper_transcriber.py` - Whisper AI transcription
- [x] `core/nllb_translator.py` - NLLB-200 translation
- [x] `core/subtitle_manager.py` - Subtitle management
- [x] `core/playlist_manager.py` - Playlist features

### UI Components
- [x] `ui/__init__.py`
- [x] `ui/main_window.py` - Main application window
- [x] `ui/fullscreen_overlay.py` - Fullscreen controls
- [x] `ui/subtitle_editor.py` - Subtitle editor
- [x] `ui/playlist_widget.py` - Playlist widget

### Utilities
- [x] `utils/__init__.py`

### Assets (if any)
- [x] `assets/` - Icons, images, etc.

---

## 📚 DOCUMENTATION FILES (Khuyến nghị)

### Essential Docs
- [x] `README.md` - Main documentation
- [x] `LICENSE` - License file (MIT)
- [x] `CONTRIBUTING.md` - Contribution guidelines
- [x] `GITHUB_SETUP.md` - GitHub setup guide

### Installation & Setup
- [x] `INSTALL.md` - Installation guide
- [x] `CUDA_SETUP.md` - GPU/CUDA setup
- [x] `QUICKSTART.md` - Quick start guide
- [x] `setup.ps1` - PowerShell setup script
- [x] `setup.bat` - Batch setup script
- [x] `run.ps1` - PowerShell run script
- [x] `run.bat` - Batch run script

### Feature Documentation
- [x] `FEATURES.md` - Feature overview
- [x] `WORKFLOW.md` - Usage workflow
- [x] `NLLB_TRANSLATION_GUIDE.md` - Translation guide (200+ languages)
- [x] `FULLSCREEN_GUIDE.md` - Fullscreen mode guide
- [x] `PLAYLIST_GUIDE.md` - Playlist management
- [x] `SUBTITLE_EDITOR.md` - Subtitle editor guide
- [x] `DEMO_GUIDE.md` - Demo guide
- [x] `QUICK_REFERENCE.md` - Quick reference

### Project Info
- [x] `CHANGELOG.md` - Version history
- [x] `PROJECT_SUMMARY.md` - Project summary
- [x] `PERFORMANCE.md` - Performance benchmarks
- [x] `PYTHON_VERSION.md` - Python version info

---

## 🔧 CONFIGURATION FILES (Bắt buộc)

### Dependencies
- [x] `requirements.txt` - Python dependencies (CPU/CUDA)
- [x] `requirements-cuda.txt` - CUDA-specific dependencies

### Git Configuration
- [x] `.gitignore` - Files to ignore

---

## ❌ FILES TO EXCLUDE (Không upload)

### Virtual Environments
- [ ] `.venv/` - Virtual environment
- [ ] `venv/` - Alternative venv name
- [ ] `env/` - Another venv name

### Python Cache
- [ ] `__pycache__/` - Python cache folders
- [ ] `*.pyc` - Compiled Python files
- [ ] `*.pyo` - Optimized Python files
- [ ] `*.py[cod]` - Other compiled files

### IDE Settings
- [ ] `.vscode/` - VS Code settings (optional to include)
- [ ] `.idea/` - PyCharm settings
- [ ] `*.swp`, `*.swo` - Vim swap files

### Model Caches (Quá lớn!)
- [ ] `~/.cache/whisper/` - Whisper model cache
- [ ] `~/.cache/huggingface/` - Hugging Face model cache
- [ ] `*.bin` - Model binary files
- [ ] `*.safetensors` - Model safetensor files

### User Data & Generated Files
- [ ] `playlist_history.json` - User's playlist history
- [ ] `*.srt` - Generated subtitle files
- [ ] `*.vtt` - Generated subtitle files
- [ ] `temp_audio_*.wav` - Temporary audio files
- [ ] `*.tmp`, `*.temp` - Temporary files

### Test & Demo Files (Optional)
- [ ] `test_setup.py` - Setup test (có thể giữ)
- [ ] `test_fullscreen.py` - Test script
- [ ] `demo_*.py` - Demo scripts
- [ ] `changelogs/` - Changelog drafts

### Build & Distribution
- [ ] `build/` - Build output
- [ ] `dist/` - Distribution files
- [ ] `*.egg-info/` - Python package info

### OS-specific
- [ ] `.DS_Store` - macOS file
- [ ] `Thumbs.db` - Windows thumbnail cache

---

## 📊 File Count Summary

```
✅ To Upload:
   - Core Python files: ~15 files
   - Documentation: ~20 files
   - Configuration: ~5 files
   - Scripts: ~4 files
   TOTAL: ~44 files

❌ To Exclude:
   - Virtual environments
   - Python cache
   - Model caches (GB of data!)
   - User data
   - Temporary files
```

---

## 🎯 Quick Check Commands

### Check files that will be uploaded
```powershell
# See what files git will track
git status

# See what's ignored
git status --ignored

# Count files to be committed
git ls-files | Measure-Object -Line
```

### Verify .gitignore is working
```powershell
# Make sure these DON'T appear in git status:
git status | Select-String "venv"          # Should be empty
git status | Select-String "__pycache__"   # Should be empty
git status | Select-String ".cache"        # Should be empty
```

### Check repository size
```powershell
# Before commit
Get-ChildItem -Recurse | Measure-Object -Property Length -Sum

# After setting up .gitignore
git count-objects -vH
```

---

## ✅ Pre-Upload Checklist

### Before First Commit
- [ ] Verified `.gitignore` is working
- [ ] No sensitive data (passwords, API keys, tokens)
- [ ] No large model files (*.bin, *.safetensors)
- [ ] No virtual environment folders
- [ ] All documentation files are updated
- [ ] `requirements.txt` is complete and accurate
- [ ] Test that code runs on clean environment

### Documentation Check
- [ ] `README.md` has clear description
- [ ] `INSTALL.md` has complete setup steps
- [ ] All links in docs work
- [ ] No broken references to missing files

### Code Quality
- [ ] No debug print statements left
- [ ] No commented-out code blocks
- [ ] Proper error handling
- [ ] Clear variable names
- [ ] Docstrings for classes/functions

---

## 🚀 Upload Command Sequence

```powershell
# 1. Initialize Git (if not done)
git init

# 2. Add remote
git remote add origin https://github.com/YOUR_USERNAME/subtitle-generator-ver2.git

# 3. Stage all files (respecting .gitignore)
git add .

# 4. Check what will be committed
git status

# 5. Verify no unwanted files
git status | Select-String "venv|__pycache__|.cache"  # Should be empty

# 6. Commit
git commit -m "Initial commit: Subtitle Generator v2.0 with Whisper & NLLB-200"

# 7. Set main branch
git branch -M main

# 8. Push to GitHub
git push -u origin main
```

---

## 📝 Notes

### Repository Size Expectations
- **Without models**: ~500 KB - 2 MB
- **With venv/cache**: 5-10 GB ❌ (DON'T upload!)

### If You Accidentally Committed Large Files
```powershell
# Remove file from git history (use with caution!)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/large/file" \
  --prune-empty --tag-name-filter cat -- --all

# Or use BFG Repo-Cleaner (recommended)
# https://rtyley.github.io/bfg-repo-cleaner/
```

### GitHub File Size Limits
- Single file: 100 MB max (soft limit)
- Repository: 1 GB recommended, 5 GB warning
- **Solution**: Model files nên để user tự download (Whisper & NLLB sẽ auto-download khi dùng)

---

## 🎉 Done!

Sau khi upload xong:
1. Check GitHub repository trong browser
2. Clone về máy khác để test
3. Verify `git clone` + `setup.ps1` + `python main.py` works
4. Share repository link!

**Repository Structure on GitHub:**
```
subtitle-generator-ver2/
├── 📄 README.md (hiển thị đầu tiên)
├── 📁 core/
├── 📁 ui/
├── 📁 utils/
├── 📁 assets/
├── 📄 requirements.txt
├── 📄 LICENSE
└── 📚 Documentation files
```

---

**Ready to upload! 🚀**
