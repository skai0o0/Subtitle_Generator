# 🚀 Quick Upload to GitHub - Hướng dẫn nhanh

## 🎯 3 Bước đơn giản

### Bước 1: Tạo Repository trên GitHub
1. Vào https://github.com
2. Click **"+"** → **"New repository"**
3. Điền:
   - **Name**: `subtitle-generator-ver2`
   - **Description**: `🎬 AI-powered subtitle generator using Whisper & NLLB-200`
   - Chọn **Public** hoặc **Private**
   - **KHÔNG** tick "Add README" (ta đã có rồi)
4. Click **"Create repository"**

### Bước 2: Chạy Upload Script
```powershell
# Mở PowerShell trong folder project

# Option A: Dùng script tự động (KHUYẾN NGHỊ)
.\upload_to_github.ps1

# Option B: Chạy từng lệnh thủ công
git init
git remote add origin https://github.com/YOUR_USERNAME/subtitle-generator-ver2.git
git add .
git commit -m "Initial commit: Subtitle Generator v2.0"
git branch -M main
git push -u origin main
```

### Bước 3: Verify & Enjoy!
- Mở browser: `https://github.com/YOUR_USERNAME/subtitle-generator-ver2`
- Check xem files đã upload chưa
- Done! 🎉

---

## ⚡ Files sẽ được upload (44 files)

### Core Code
- ✅ `main.py`
- ✅ `core/` (5 files)
- ✅ `ui/` (4 files)
- ✅ `utils/` (1 file)

### Documentation
- ✅ `README.md`, `INSTALL.md`, `QUICKSTART.md`
- ✅ `CONTRIBUTING.md`, `GITHUB_SETUP.md`
- ✅ `NLLB_TRANSLATION_GUIDE.md`, `FULLSCREEN_GUIDE.md`
- ✅ Và 13+ docs khác

### Configuration
- ✅ `requirements.txt`, `requirements-cuda.txt`
- ✅ `.gitignore`, `LICENSE`
- ✅ `setup.ps1`, `run.ps1`

---

## 🚫 Files sẽ KHÔNG upload (theo .gitignore)

- ❌ `.venv/`, `venv/` - Virtual environments
- ❌ `__pycache__/`, `*.pyc` - Python cache
- ❌ `~/.cache/huggingface/` - Model cache (GB of data!)
- ❌ `playlist_history.json` - User data
- ❌ `*.srt`, `*.vtt` - Generated subtitles
- ❌ `test_*.py`, `demo_*.py` - Test files

---

## 🔧 Troubleshooting

### Lỗi: "Permission denied"
```powershell
# Dùng HTTPS thay vì SSH
git remote set-url origin https://github.com/YOUR_USERNAME/subtitle-generator-ver2.git
```

### Lỗi: "Authentication failed"
```powershell
# Tạo Personal Access Token:
# GitHub → Settings → Developer settings → Personal access tokens → Generate new token
# Permissions: repo (full control)
# Khi git push hỏi password, paste token vào
```

### Lỗi: "Repository not found"
```powershell
# Đảm bảo đã tạo repository trên GitHub trước!
# Hoặc check URL:
git remote -v
```

---

## 📊 Checklist trước khi upload

- [ ] Đã tạo repository trên GitHub
- [ ] `.gitignore` đã có (check xem venv/ không bị upload)
- [ ] `requirements.txt` đầy đủ
- [ ] `README.md` đã update
- [ ] Code chạy được không lỗi
- [ ] Không có password/API key hardcoded trong code

---

## 🎯 Repository Size

**Expected size:**
- Without venv/cache: **~2 MB** ✅
- With venv: **~5 GB** ❌ (KHÔNG upload!)

**Check size:**
```powershell
# See what will be uploaded
git ls-files | Measure-Object

# Check actual size
Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notmatch "venv|\.venv|__pycache__" } | Measure-Object -Property Length -Sum
```

---

## 🌐 After Upload

### Add Topics/Tags
Settings → Topics → Add:
- `python`
- `ai`
- `machine-learning`
- `subtitles`
- `whisper`
- `nllb-200`
- `video-processing`
- `gpu-acceleration`

### Enable Features
- ✅ **Issues** - For bug reports
- ✅ **Discussions** - For Q&A
- ✅ **Wiki** - For detailed docs (optional)

### Create First Release
1. Releases → "Create a new release"
2. Tag: `v2.0.0`
3. Title: `Version 2.0.0 - Initial Release`
4. Description:
   ```markdown
   ## 🎉 Initial Release
   
   ### Features
   - AI transcription with Whisper (5 models)
   - Multi-language translation with NLLB-200 (200+ languages)
   - GPU acceleration
   - Fullscreen mode
   - Playlist management
   - Subtitle editor
   
   ### Download
   Clone and run:
   ```bash
   git clone https://github.com/YOUR_USERNAME/subtitle-generator-ver2.git
   cd subtitle-generator-ver2
   .\setup.ps1
   python main.py
   ```
   ```

---

## 📞 Need Help?

- 📖 Full guide: [GITHUB_SETUP.md](GITHUB_SETUP.md)
- 🤝 Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
- 📋 File list: [FILES_TO_UPLOAD.md](FILES_TO_UPLOAD.md)

---

## ✅ Done!

**Your repository:**
```
https://github.com/YOUR_USERNAME/subtitle-generator-ver2
```

**Share with:**
- Friends & colleagues
- Reddit (r/Python, r/MachineLearning)
- Discord communities
- Social media

⭐ **Don't forget to star your own repo!** 😄

---

**Happy sharing! 🚀**
