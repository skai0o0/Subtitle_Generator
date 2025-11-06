# Hướng dẫn Cài đặt Subtitle Generator

## Bước 1: Cài đặt FFmpeg

FFmpeg là công cụ bắt buộc để xử lý video/audio.

### Windows:

**Cách 1: Sử dụng Chocolatey (khuyến nghị)**
```powershell
choco install ffmpeg
```

**Cách 2: Download thủ công**
1. Tải FFmpeg từ: https://www.gyan.dev/ffmpeg/builds/
2. Chọn "ffmpeg-release-essentials.zip"
3. Giải nén vào thư mục (ví dụ: `C:\ffmpeg`)
4. Thêm vào PATH:
   - Mở System Properties → Environment Variables
   - Thêm `C:\ffmpeg\bin` vào PATH
   - Khởi động lại terminal

**Kiểm tra cài đặt:**
```powershell
ffmpeg -version
```

## Bước 2: Tạo Virtual Environment

```powershell
# Di chuyển vào thư mục dự án
cd subtitle-generator-ver2

# Tạo virtual environment
python -m venv venv

# Kích hoạt virtual environment
.\venv\Scripts\Activate.ps1

# Nếu gặp lỗi ExecutionPolicy, chạy:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Bước 3: Cài đặt Dependencies

```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Cài đặt dependencies
pip install -r requirements.txt
```

**Lưu ý:** 
- Quá trình cài đặt PyTorch và Whisper có thể mất vài phút
- Whisper sẽ tự động download model khi lần đầu sử dụng

## Bước 4: Chạy ứng dụng

```powershell
python main.py
```

## Xử lý lỗi thường gặp

### Lỗi: "Import PySide6 could not be resolved"
**Giải pháp:** Đảm bảo đã kích hoạt virtual environment và cài đặt requirements.txt

### Lỗi: "ffmpeg not found"
**Giải pháp:** 
1. Kiểm tra FFmpeg đã được cài đặt: `ffmpeg -version`
2. Đảm bảo FFmpeg có trong PATH
3. Khởi động lại terminal/VS Code

### Lỗi: "CUDA out of memory"
**Giải pháp:** Chọn model nhỏ hơn (tiny hoặc base) khi transcribe

### Lỗi: "Could not load dynamic library 'cudart64_*.dll'"
**Giải pháp:** Đây là warning bình thường nếu không có GPU NVIDIA. Ứng dụng sẽ tự động sử dụng CPU.

## Sử dụng ứng dụng

1. **Load video/audio:** File → Open Video/Audio (Ctrl+O)
2. **Play/Pause:** Click button hoặc spacebar
3. **Transcribe:** Click "🎤 Transcribe with Whisper AI"
4. **Chọn model:** 
   - tiny: Nhanh nhất, độ chính xác thấp
   - base: Cân bằng (khuyến nghị)
   - small/medium/large: Chính xác hơn, chậm hơn
5. **Export subtitle:** Subtitle → Export as SRT/VTT

## Thông tin thêm

### Model Whisper
- Lần đầu sử dụng mỗi model, Whisper sẽ tự động download
- Models được lưu trong `~/.cache/whisper/`
- Kích thước models:
  - tiny: ~39 MB
  - base: ~74 MB
  - small: ~244 MB
  - medium: ~769 MB
  - large: ~1550 MB

### Định dạng hỗ trợ
- **Video:** MP4, AVI, MKV, MOV, WMV, FLV
- **Audio:** MP3, WAV, M4A, AAC, FLAC, OGG

### Ngôn ngữ
- Mặc định: Tiếng Việt
- Có thể chỉnh sửa trong `core/whisper_transcriber.py` (dòng 31):
  ```python
  language="vi",  # Đổi thành "en", "ja", "ko", etc.
  ```
