# Quick Start Guide - Subtitle Generator

## 🚀 Cài đặt nhanh

```powershell
# 1. Cài FFmpeg (nếu chưa có)
choco install ffmpeg

# 2. Tạo và kích hoạt virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Cài đặt dependencies
pip install -r requirements.txt

# 4. Chạy ứng dụng
python main.py
```

## 📖 Workflow cơ bản

### 1️⃣ Load Video/Audio
- **Menu:** File → Open Video/Audio
- **Shortcut:** Ctrl+O
- **Hỗ trợ:** MP4, AVI, MKV, MP3, WAV, và nhiều format khác

### 2️⃣ Play Video
- **Play/Pause:** Click nút ▶️ hoặc ⏸️
- **Stop:** Click nút ⏹️
- **Seek:** Kéo thanh timeline
- **Volume:** Điều chỉnh slider bên phải

### 3️⃣ Transcribe với Whisper AI
1. Click nút **🎤 Transcribe with Whisper AI**
2. Chọn model (khuyến nghị: **base**)
3. Chờ xử lý (có thể mất vài phút)
4. Subtitle sẽ tự động hiển thị khi play

### 4️⃣ Export Subtitle
- **Menu:** Subtitle → Export as SRT/VTT
- File sẽ được lưu cùng tên với video

## ⚙️ Chọn Model Whisper

| Model | Tốc độ | Độ chính xác | RAM | Khuyến nghị |
|-------|---------|--------------|-----|-------------|
| tiny | ⚡⚡⚡⚡⚡ | ⭐⭐ | ~1GB | Testing nhanh |
| base | ⚡⚡⚡⚡ | ⭐⭐⭐ | ~1GB | **Đa số trường hợp** |
| small | ⚡⚡⚡ | ⭐⭐⭐⭐ | ~2GB | Chất lượng tốt |
| medium | ⚡⚡ | ⭐⭐⭐⭐⭐ | ~5GB | Chuyên nghiệp |
| large | ⚡ | ⭐⭐⭐⭐⭐ | ~10GB | Tốt nhất (rất chậm) |

## 💡 Tips & Tricks

### Tăng tốc độ transcribe:
- Dùng model **tiny** hoặc **base**
- Nếu có GPU NVIDIA, PyTorch sẽ tự động dùng CUDA
- Close các ứng dụng khác để giải phóng RAM

### Cải thiện độ chính xác:
- Dùng model **small** hoặc lớn hơn
- Đảm bảo audio rõ ràng, ít noise
- Với audio tiếng Việt accent, có thể cần model lớn hơn

### Keyboard Shortcuts:
- **Ctrl+O**: Open file
- **Ctrl+T**: Start transcription
- **Ctrl+Q**: Quit
- **Space**: Play/Pause (khi focus vào video)

## 🔧 Xử lý lỗi

### "Module not found"
```powershell
# Kích hoạt lại venv và cài đặt
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### "FFmpeg not found"
```powershell
# Kiểm tra FFmpeg
ffmpeg -version

# Nếu không có, cài đặt:
choco install ffmpeg
```

### Transcription chậm/treo
- Chọn model nhỏ hơn (tiny/base)
- Check Task Manager - RAM usage
- Đảm bảo không chạy app khác tốn RAM

### Subtitle không hiển thị
- Đảm bảo đã transcribe xong (check dialog)
- Click Play để thấy subtitle
- Check timeline có đang ở vị trí có subtitle không

## 📚 Thêm thông tin

Xem chi tiết trong:
- **README.md**: Tổng quan dự án
- **INSTALL.md**: Hướng dẫn cài đặt đầy đủ

## 🆘 Support

Gặp vấn đề? Check:
1. Đã cài FFmpeg chưa?
2. Đã activate venv chưa?
3. Đã install requirements.txt chưa?
4. File video có format được hỗ trợ không?

---

**Enjoy creating subtitles! 🎬✨**
