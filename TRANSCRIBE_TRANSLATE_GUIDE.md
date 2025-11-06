# 🎤🌐 Transcribe & Translate Guide

## ✨ Tính năng mới: Chọn mode Transcribe hoặc Translate

### 🎯 Tổng quan

Khi nhấn nút **"🎤 Transcribe with Whisper AI"**, bạn sẽ thấy popup cho phép chọn:

1. **🎤 Transcribe** - Tạo phụ đề theo ngôn ngữ gốc của video
2. **🌐 Translate to English** - Tạo phụ đề tiếng Anh (dịch từ bất kỳ ngôn ngữ nào)

---

## 🎬 Cách sử dụng

### Bước 1: Load video
```
File → Open Video/Audio
hoặc nhấn Ctrl+O
```

### Bước 2: Nhấn nút Transcribe
```
Nhấn nút: 🎤 Transcribe with Whisper AI
```

### Bước 3: Chọn mode

**Popup sẽ hiện ra:**
```
┌─────────────────────────────────────────┐
│          Choose Mode                     │
├─────────────────────────────────────────┤
│ Select transcription mode:               │
│                                          │
│ 🎤 Transcribe: Generate subtitles in    │
│    the original language of the video   │
│                                          │
│ 🌐 Translate: Generate subtitles in     │
│    English (translates from any         │
│    language)                             │
│                                          │
├─────────────────────────────────────────┤
│  [🎤 Transcribe]  [🌐 Translate to      │
│                    English]   [Cancel]  │
└─────────────────────────────────────────┘
```

**Chọn một trong hai:**
- **🎤 Transcribe** - Giữ ngôn ngữ gốc
- **🌐 Translate to English** - Dịch sang tiếng Anh

### Bước 4: Chọn model
```
┌─────────────────────────────────────────┐
│      Select Whisper Model                │
├─────────────────────────────────────────┤
│ Choose transcription model:              │
│ (larger models are more accurate but     │
│  slower)                                 │
│                                          │
│ ▼ base (balanced)                        │
│                                          │
├─────────────────────────────────────────┤
│              [OK]     [Cancel]           │
└─────────────────────────────────────────┘
```

**Chọn model phù hợp:**
- tiny - Nhanh nhất, độ chính xác thấp
- **base** - Cân bằng (khuyên dùng)
- small - Chất lượng tốt
- medium - Chất lượng cao hơn, chậm hơn
- large - Tốt nhất, rất chậm

### Bước 5: Đợi xử lý
```
Progress dialog sẽ hiện:
- "Transcribing with Whisper AI" (mode transcribe)
- "Translating to English with Whisper AI" (mode translate)

Hiển thị:
- GPU/CPU được sử dụng
- Tiến trình xử lý
- Số segments tìm thấy
```

---

## 🎤 Mode: Transcribe (Giữ ngôn ngữ gốc)

### Khi nào dùng?
- Video bằng tiếng Việt → muốn phụ đề tiếng Việt
- Video bằng tiếng Anh → muốn phụ đề tiếng Anh
- Video bằng tiếng Nhật → muốn phụ đề tiếng Nhật
- Muốn giữ ngôn ngữ gốc của video

### Cách hoạt động:
```
Video tiếng Việt
    ↓
Whisper AI (transcribe mode)
    ↓
Phụ đề tiếng Việt
```

### Ví dụ:
```
Audio: "Xin chào, đây là video hướng dẫn"
Subtitle: "Xin chào, đây là video hướng dẫn"
```

### Progress messages:
```
📤 Extracting audio for transcription...
🎮 Using GPU: NVIDIA GeForce RTX 3060
🚀 Transcribing with GPU acceleration...
✅ Transcription complete! Found 42 segments.
```

---

## 🌐 Mode: Translate to English

### Khi nào dùng?
- Video bằng bất kỳ ngôn ngữ nào → muốn phụ đề tiếng Anh
- Tiếng Việt → English
- Tiếng Nhật → English
- Tiếng Trung → English
- Muốn chia sẻ video với người nước ngoài

### Cách hoạt động:
```
Video bất kỳ ngôn ngữ
    ↓
Whisper AI (translate mode)
    ↓
Tự động nhận diện ngôn ngữ
    ↓
Dịch sang tiếng Anh
    ↓
Phụ đề tiếng Anh
```

### Ví dụ:
```
Audio (Tiếng Việt): "Xin chào, đây là video hướng dẫn"
Subtitle (English):  "Hello, this is a tutorial video"

Audio (Tiếng Nhật): "こんにちは、これはチュートリアルビデオです"
Subtitle (English):  "Hello, this is a tutorial video"
```

### Progress messages:
```
📤 Extracting audio for translation...
🎮 Using GPU: NVIDIA GeForce RTX 3060
🚀 Translating to English with GPU acceleration...
🌐 Auto-detecting source language and translating to English...
✅ Translation complete! Found 42 segments in English.
🌐 Detected source language: vi (Vietnamese)
```

---

## 🎯 So sánh hai mode

| Feature | 🎤 Transcribe | 🌐 Translate |
|---------|---------------|--------------|
| **Output language** | Ngôn ngữ gốc | Tiếng Anh |
| **Auto-detect** | ✅ Yes | ✅ Yes |
| **Vietnamese → Vietnamese** | ✅ Yes | ❌ No |
| **Vietnamese → English** | ❌ No | ✅ Yes |
| **Japanese → Japanese** | ✅ Yes | ❌ No |
| **Japanese → English** | ❌ No | ✅ Yes |
| **Speed** | Fast | Same speed |
| **Accuracy** | High | High |
| **Use case** | Phụ đề cùng ngôn ngữ | Phụ đề tiếng Anh |

---

## 💡 Tips & Best Practices

### ✅ Chọn mode phù hợp:

**Transcribe khi:**
- Người xem hiểu ngôn ngữ gốc
- Cần phụ đề cho người khiếm thính
- Học ngôn ngữ (xem + đọc cùng ngôn ngữ)

**Translate khi:**
- Người xem không hiểu ngôn ngữ gốc
- Muốn chia sẻ quốc tế
- Cần subtitle tiếng Anh cho YouTube/social media

### ✅ Chọn model phù hợp:

**Testing/Preview:**
```
Use: tiny hoặc base
Fast results để kiểm tra
```

**Production/Final:**
```
Use: small, medium, hoặc large
Better accuracy cho bản cuối
```

**GPU available:**
```
Use: medium hoặc large
GPU xử lý nhanh, dùng model lớn
```

**CPU only:**
```
Use: tiny hoặc base
Tránh model lớn, sẽ rất chậm
```

### ✅ Workflow thông minh:

**1. Quick test với tiny/base:**
```
Load video
→ Transcribe/Translate với model tiny
→ Xem kết quả có OK không
→ Nếu OK, export
→ Nếu không, thử model lớn hơn
```

**2. Batch processing:**
```
Load playlist nhiều video
→ Dùng model base cho tất cả
→ Export tất cả
→ Review sau
```

**3. High quality:**
```
Load important video
→ Dùng model large
→ Đợi lâu hơn
→ Kết quả tốt nhất
```

---

## 🎓 Ví dụ thực tế

### Case 1: Video tiếng Việt cho người Việt
```
Video: Hướng dẫn nấu ăn tiếng Việt
→ Chọn: 🎤 Transcribe
→ Model: base
→ Kết quả: Phụ đề tiếng Việt
→ Người Việt xem dễ hiểu hơn
```

### Case 2: Video tiếng Việt cho người nước ngoài
```
Video: Giới thiệu du lịch Việt Nam
→ Chọn: 🌐 Translate to English
→ Model: small
→ Kết quả: Phụ đề tiếng Anh
→ Khách du lịch hiểu được
```

### Case 3: Video tiếng Nhật học tiếng Nhật
```
Video: Anime tiếng Nhật
→ Chọn: 🎤 Transcribe
→ Model: medium
→ Kết quả: Phụ đề tiếng Nhật
→ Học từ vựng hiragana/katakana
```

### Case 4: Video tiếng Nhật xem hiểu nội dung
```
Video: Anime tiếng Nhật
→ Chọn: 🌐 Translate to English
→ Model: medium
→ Kết quả: Phụ đề tiếng Anh
→ Hiểu nội dung anime
```

---

## 🔧 Technical Details

### Whisper API Parameters

**Transcribe mode:**
```python
result = model.transcribe(
    audio=audio_path,
    task="transcribe",  # Keep original language
    language=None,      # Auto-detect
    verbose=False,
    fp16=True          # GPU acceleration
)
```

**Translate mode:**
```python
result = model.transcribe(
    audio=audio_path,
    task="translate",   # Translate to English
    # No language param needed - auto-detects source
    verbose=False,
    fp16=True          # GPU acceleration
)
```

### Language Detection

Whisper tự động nhận diện ngôn ngữ:
- 99+ ngôn ngữ được hỗ trợ
- Không cần chỉ định ngôn ngữ nguồn
- Kết quả trả về ngôn ngữ được detect

### Supported Languages (một số)

| Code | Language | Transcribe | Translate |
|------|----------|------------|-----------|
| vi | Vietnamese | ✅ | ✅ |
| en | English | ✅ | N/A |
| ja | Japanese | ✅ | ✅ |
| zh | Chinese | ✅ | ✅ |
| ko | Korean | ✅ | ✅ |
| th | Thai | ✅ | ✅ |
| fr | French | ✅ | ✅ |
| de | German | ✅ | ✅ |
| es | Spanish | ✅ | ✅ |
| it | Italian | ✅ | ✅ |

---

## 🐛 Troubleshooting

### Popup không hiện?
```
→ Kiểm tra đã load video chưa
→ Kiểm tra nút transcribe có enabled không
→ Restart app
```

### Translate không chính xác?
```
→ Thử model lớn hơn (medium/large)
→ Kiểm tra audio quality
→ Ngôn ngữ gốc có được Whisper hỗ trợ tốt không
```

### Transcribe sai ngôn ngữ?
```
→ Mode transcribe tự động detect
→ Nếu sai, có thể audio không rõ
→ Thử model lớn hơn
→ Hoặc dùng translate mode nếu muốn English
```

### Progress dialog không update?
```
→ Bình thường, đang xử lý
→ Đợi thêm
→ Nếu quá lâu (>10 phút), check console errors
```

---

## 🚀 Performance Tips

### GPU Acceleration
```
✅ Có GPU (CUDA):
- Model large: OK
- Processing: Fast
- Recommend: medium/large

❌ Không có GPU (CPU):
- Model large: Very slow
- Processing: Slow
- Recommend: tiny/base
```

### Model Speed Comparison (1 hour video)

| Model | GPU Time | CPU Time | Quality |
|-------|----------|----------|---------|
| tiny | ~2 min | ~10 min | ⭐⭐ |
| base | ~3 min | ~15 min | ⭐⭐⭐ |
| small | ~5 min | ~30 min | ⭐⭐⭐⭐ |
| medium | ~10 min | ~60 min | ⭐⭐⭐⭐⭐ |
| large | ~20 min | ~120 min | ⭐⭐⭐⭐⭐ |

---

## 🎉 Summary

### Tính năng mới:
✅ Popup chọn mode trước khi transcribe
✅ Mode Transcribe (giữ ngôn ngữ gốc)
✅ Mode Translate (dịch sang tiếng Anh)
✅ Auto-detect source language
✅ Progress messages rõ ràng
✅ Works với mọi ngôn ngữ Whisper hỗ trợ

### Benefits:
- **Linh hoạt**: Chọn output language phù hợp
- **Dễ dùng**: 2 click để chọn mode
- **Thông minh**: Auto-detect ngôn ngữ
- **Mạnh mẽ**: 99+ ngôn ngữ được hỗ trợ
- **Chuyên nghiệp**: Whisper AI state-of-the-art

---

**Enjoy creating subtitles in any language! 🎤🌐✨**
