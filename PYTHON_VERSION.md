# Python Version Requirements

## Khuyến nghị: Python 3.11.x

### Tại sao Python 3.11?

1. **Tương thích tốt với Whisper AI**
   - OpenAI Whisper được test kỹ với Python 3.8 - 3.11
   - Python 3.11 có performance improvements đáng kể

2. **PyTorch compatibility**
   - PyTorch có pre-built wheels cho Python 3.11
   - Cài đặt nhanh hơn, ít lỗi hơn

3. **Stability**
   - Python 3.11 đã mature và stable
   - Nhiều packages hỗ trợ tốt

### Versions được hỗ trợ

| Python Version | Status | Notes |
|---------------|--------|-------|
| 3.8.x | ✅ Supported | Minimum version |
| 3.9.x | ✅ Supported | Good compatibility |
| 3.10.x | ✅ Supported | Good performance |
| **3.11.x** | ✅ **Recommended** | **Best choice** |
| 3.12.x | ⚠️ Partial | Some packages may have issues |
| 3.13+ | ❌ Not tested | May not work |

### Cài đặt Python 3.11

#### Windows:

**Option 1: Download từ python.org**
1. Visit: https://www.python.org/downloads/
2. Download Python 3.11.x (latest 3.11 version)
3. Install với options:
   - ✅ Add Python to PATH
   - ✅ Install pip
   - ✅ Install for all users

**Option 2: Chocolatey**
```powershell
choco install python311
```

**Option 3: Microsoft Store**
- Search "Python 3.11" trong Microsoft Store
- Click Install

### Kiểm tra version

```powershell
# Check default Python
python --version

# Check Python 3.11 specifically
py -3.11 --version

# List all Python versions
py --list
```

### Setup Virtual Environment

Project này đã được configure để tự động sử dụng Python 3.11:

```powershell
# Run setup script (sẽ tự động dùng Python 3.11)
.\setup.ps1

# Hoặc manual:
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Current Setup

Dự án này đang dùng:
- **Python Version:** 3.11.9
- **Virtual Environment:** `.venv/`
- **Package Manager:** pip

### Troubleshooting

#### "py -3.11 not found"
→ Cài đặt Python 3.11 (see instructions above)

#### "pip install fails"
→ Upgrade pip: `python -m pip install --upgrade pip`

#### "Whisper import error"
→ Reinstall in clean venv:
```powershell
Remove-Item -Recurse -Force .venv
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Benefits of Python 3.11

- 🚀 **10-60% faster** than Python 3.10
- 📦 Better error messages
- 🔧 Improved stability
- ✨ New features (tomllib, typing improvements)
- 🎯 Perfect for AI/ML workloads

---

**Recommendation:** Stick with Python 3.11.x for best experience!
