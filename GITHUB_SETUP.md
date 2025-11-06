# 🚀 GitHub Setup Guide - Đóng gói và Deploy Project

Hướng dẫn chi tiết để đưa project lên GitHub và quản lý repository.

---

## 📋 Mục lục
1. [Chuẩn bị trước khi upload](#1-chuẩn-bị-trước-khi-upload)
2. [Tạo GitHub Repository](#2-tạo-github-repository)
3. [Upload code lên GitHub](#3-upload-code-lên-github)
4. [Quản lý Repository](#4-quản-lý-repository)
5. [Best Practices](#5-best-practices)

---

## 1. 📦 Chuẩn bị trước khi upload

### Kiểm tra các file cần thiết

#### ✅ Files BẮT BUỘC phải có:
```
✓ README.md                    # Giới thiệu project
✓ LICENSE                      # License file
✓ requirements.txt             # Python dependencies
✓ requirements-cuda.txt        # CUDA dependencies
✓ .gitignore                   # Ignore unnecessary files
✓ main.py                      # Entry point
✓ setup.ps1 / setup.bat       # Setup scripts
✓ run.ps1 / run.bat           # Run scripts
```

#### ✅ Files NÊNCÓ (documentation):
```
✓ INSTALL.md                   # Installation guide
✓ QUICKSTART.md                # Quick start guide
✓ CONTRIBUTING.md              # Contribution guidelines
✓ CHANGELOG.md                 # Version history
✓ CUDA_SETUP.md                # GPU setup
✓ FEATURES.md                  # Feature list
✓ WORKFLOW.md                  # Usage workflow
✓ NLLB_TRANSLATION_GUIDE.md    # Translation guide
```

#### ❌ Files KHÔNG NÊN upload (đã có trong .gitignore):
```
✗ .venv/, venv/                # Virtual environments
✗ __pycache__/                 # Python cache
✗ *.pyc, *.pyo                 # Compiled Python
✗ .vscode/, .idea/             # IDE settings
✗ playlist_history.json        # User data
✗ *.srt, *.vtt                 # Generated subtitles
✗ test_*.py, demo_*.py         # Test files (optional)
✗ ~/.cache/huggingface/        # Model cache
✗ temp_audio_*.wav             # Temporary files
```

### Kiểm tra .gitignore
```powershell
# Xem file .gitignore hiện tại
cat .gitignore

# Nếu cần, thêm các file/folder vào .gitignore
echo "*.log" >> .gitignore
echo "my_private_folder/" >> .gitignore
```

### Test project trước khi upload
```powershell
# 1. Test setup
python test_setup.py

# 2. Test main app
python main.py

# 3. Kiểm tra không có lỗi
# Load video → Transcribe → Translate → Export
```

---

## 2. 🌐 Tạo GitHub Repository

### Option A: Tạo mới trên GitHub Website

1. **Đăng nhập GitHub** → https://github.com
2. **Click "+" (top right)** → "New repository"
3. **Điền thông tin:**
   ```
   Repository name:    subtitle-generator-ver2
   Description:        🎬 AI-powered subtitle generator using Whisper & NLLB-200
   Visibility:         ○ Public  ◉ Private (choose one)
   
   Initialize:
   [ ] Add a README file          (KHÔNG check - ta đã có rồi)
   [ ] Add .gitignore             (KHÔNG check)
   [ ] Choose a license           (KHÔNG check - ta đã có LICENSE)
   ```
4. **Click "Create repository"**

### Option B: Tạo bằng GitHub CLI
```powershell
# Install GitHub CLI (nếu chưa có)
winget install --id GitHub.cli

# Login
gh auth login

# Tạo repository
gh repo create subtitle-generator-ver2 --public --description "AI-powered subtitle generator"
```

---

## 3. ⬆️ Upload code lên GitHub

### Bước 1: Cài đặt Git (nếu chưa có)
```powershell
# Check Git đã cài chưa
git --version

# Nếu chưa có, cài Git
winget install --id Git.Git
```

### Bước 2: Configure Git (lần đầu tiên)
```powershell
# Set user name và email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Kiểm tra config
git config --list
```

### Bước 3: Initialize Git trong project
```powershell
# Di chuyển vào project folder
cd C:\Users\hoang\Desktop\Codespaces\subtitle-generator-ver2

# Initialize git
git init

# Thêm remote repository (thay YOUR_USERNAME bằng username GitHub của bạn)
git remote add origin https://github.com/YOUR_USERNAME/subtitle-generator-ver2.git

# Hoặc dùng SSH (nếu đã setup SSH key)
git remote add origin git@github.com:YOUR_USERNAME/subtitle-generator-ver2.git
```

### Bước 4: Commit và Push lần đầu
```powershell
# Thêm tất cả files (trừ những file trong .gitignore)
git add .

# Kiểm tra files sẽ được commit
git status

# Commit với message
git commit -m "Initial commit: Subtitle Generator Ver 2 with Whisper & NLLB-200"

# Đổi branch thành main (nếu đang là master)
git branch -M main

# Push lên GitHub
git push -u origin main

# Nếu bị lỗi authentication, dùng Personal Access Token:
# Settings → Developer settings → Personal access tokens → Generate new token
# Khi push, dùng token thay cho password
```

### Bước 5: Verify upload thành công
```powershell
# Check GitHub repository
# Mở browser: https://github.com/YOUR_USERNAME/subtitle-generator-ver2

# Hoặc dùng GitHub CLI
gh repo view --web
```

---

## 4. 🔧 Quản lý Repository

### Cập nhật code lên GitHub
```powershell
# 1. Kiểm tra files đã thay đổi
git status

# 2. Add files muốn commit
git add .                          # Add tất cả
git add main.py core/              # Add specific files/folders

# 3. Commit với message rõ ràng
git commit -m "feat: Add VRAM cleanup after model inference"

# 4. Push lên GitHub
git push

# Nếu có conflict, pull trước:
git pull origin main
# Resolve conflicts → git add → git commit → git push
```

### Tạo branches cho features mới
```powershell
# Tạo và switch sang branch mới
git checkout -b feature/translation-improvement

# Làm việc trên branch này...
# ... make changes ...

# Commit changes
git add .
git commit -m "feat: Improve translation context window"

# Push branch lên GitHub
git push -u origin feature/translation-improvement

# Trên GitHub, tạo Pull Request để merge vào main
```

### Tạo Release/Tags
```powershell
# Tạo tag cho version
git tag -a v2.0.0 -m "Version 2.0.0: Added NLLB-200 translation"

# Push tag lên GitHub
git push origin v2.0.0

# Hoặc push tất cả tags
git push --tags

# Trên GitHub:
# Releases → "Create a new release" → Choose tag → Add release notes
```

### Clone repository về máy khác
```powershell
# Clone repository
git clone https://github.com/YOUR_USERNAME/subtitle-generator-ver2.git

# Di chuyển vào folder
cd subtitle-generator-ver2

# Setup virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run app
python main.py
```

---

## 5. ✨ Best Practices

### README.md nên có:
- ✅ Project description
- ✅ Features list
- ✅ Installation instructions
- ✅ Quick start guide
- ✅ Screenshots/GIFs (if possible)
- ✅ Tech stack
- ✅ License info
- ✅ Contributing guidelines link

### Commit Message Guidelines:
```
feat: Add new feature
fix: Fix bug
docs: Update documentation
style: Code formatting
refactor: Code refactoring
test: Add tests
chore: Maintenance tasks

Examples:
feat: Add NLLB-200 translation with 200+ languages
fix: Fix VRAM memory leak in Whisper transcription
docs: Update installation guide for CUDA 12.4
refactor: Improve subtitle editor performance
```

### GitHub Settings (trên website):

#### 1. Repository Settings
- **Description**: Viết mô tả ngắn gọn
- **Website**: Link đến docs (nếu có)
- **Topics**: Add tags (VD: python, ai, subtitles, whisper, nllb)

#### 2. Enable GitHub Actions (CI/CD)
```yaml
# .github/workflows/test.yml
name: Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: python test_setup.py
```

#### 3. Add Badges to README.md
```markdown
![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![Stars](https://img.shields.io/github/stars/YOUR_USERNAME/subtitle-generator-ver2)
```

#### 4. Enable Issues & Discussions
- **Issues**: Cho bug reports và feature requests
- **Discussions**: Cho Q&A và community chat

#### 5. Add CONTRIBUTING.md
- Guidelines cho contributors
- Code style rules
- How to submit PRs

---

## 🎯 Checklist trước khi upload

### Code Quality
- [ ] Code chạy được không lỗi
- [ ] Đã test các tính năng chính
- [ ] Không có hardcoded passwords/API keys
- [ ] Đã format code đẹp

### Documentation
- [ ] README.md đầy đủ thông tin
- [ ] INSTALL.md có hướng dẫn chi tiết
- [ ] Các file .md khác đã update
- [ ] Comments trong code rõ ràng

### Git Setup
- [ ] .gitignore đã setup đúng
- [ ] Không commit file không cần thiết
- [ ] LICENSE file đã có
- [ ] requirements.txt đầy đủ

### GitHub Repository
- [ ] Repository name rõ ràng
- [ ] Description hấp dẫn
- [ ] Topics/tags đã add
- [ ] README hiển thị đẹp trên GitHub

---

## 🚀 Commands Tổng hợp

### Quick Reference
```powershell
# Setup Git lần đầu
git init
git remote add origin https://github.com/YOUR_USERNAME/subtitle-generator-ver2.git
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main

# Workflow hàng ngày
git status                 # Check changes
git add .                  # Stage all changes
git commit -m "message"    # Commit
git push                   # Push to GitHub
git pull                   # Pull from GitHub

# Branching
git checkout -b feature/new-feature    # Create & switch to new branch
git checkout main                      # Switch back to main
git merge feature/new-feature          # Merge branch to current

# Tags & Releases
git tag -a v2.0.0 -m "Version 2.0.0"  # Create tag
git push --tags                        # Push tags

# Undo changes
git checkout -- file.py               # Discard changes to file
git reset HEAD file.py                # Unstage file
git reset --hard HEAD~1               # Undo last commit (CAREFUL!)
```

---

## 📞 Troubleshooting

### Lỗi: "Permission denied (publickey)"
```powershell
# Giải pháp 1: Dùng HTTPS thay vì SSH
git remote set-url origin https://github.com/YOUR_USERNAME/subtitle-generator-ver2.git

# Giải pháp 2: Setup SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"
# Copy public key vào GitHub Settings → SSH Keys
```

### Lỗi: "Authentication failed"
```powershell
# Dùng Personal Access Token thay cho password
# GitHub → Settings → Developer settings → Personal access tokens
# Generate token → Copy → Dùng làm password khi git push
```

### Lỗi: ".gitignore không work"
```powershell
# Clear git cache
git rm -r --cached .
git add .
git commit -m "fix: Update .gitignore"
git push
```

---

## 🎉 Hoàn tất!

Sau khi upload thành công:
1. ✅ Kiểm tra repository trên GitHub
2. ✅ Test clone về máy khác xem có chạy được không
3. ✅ Share link với team/community
4. ✅ Add ⭐ cho repo (tự star project của mình là okay! 😄)

**Repository link mẫu:**
```
https://github.com/YOUR_USERNAME/subtitle-generator-ver2
```

---

**Happy Coding & Sharing! 🚀**
