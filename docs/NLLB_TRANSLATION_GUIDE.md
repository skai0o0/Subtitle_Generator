# 🌐 NLLB-200 Translation Guide

## ✨ Tính năng dịch đa ngôn ngữ với NLLB-200

### 🎯 Tổng quan

**NLLB-200** (No Language Left Behind) là model dịch thuật của **Meta AI**:
- ✅ **200+ ngôn ngữ** được hỗ trợ
- ✅ Chất lượng cao, ít lỗi encoding
- ✅ Hỗ trợ cả ngôn ngữ low-resource
- ✅ State-of-the-art translation model

**So với EnViT5:**
- EnViT5: Chỉ EN ↔ VI (2 ngôn ngữ)
- NLLB-200: 200+ ngôn ngữ, bất kỳ cặp nào!

---

## 🚀 Hướng dẫn sử dụng

### Bước 1: Transcribe video

```
File → Open Video
↓
Transcribe → Start Transcription
↓
Chọn mode: "🌐 Translate to English"
↓
Chọn model: base/small
↓
Đợi Whisper xử lý → English subtitles
```

### Bước 2: Dịch sang ngôn ngữ mong muốn

```
Transcribe menu → "🌐 Translate Subtitles..."
```

**Dialog 1: Chọn ngôn ngữ đích**
```
┌────────────────────────────────────┐
│ Select Target Language             │
├────────────────────────────────────┤
│ Translate subtitles to:            │
│                                    │
│ ▼ Vietnamese (Tiếng Việt)          │  ← Default
│   English                          │
│   Chinese Simplified (简体中文)    │
│   Japanese (日本語)                │
│   Korean (한국어)                  │
│   Thai (ไทย)                       │
│   ... (200+ languages)             │
│                                    │
│         [OK]      [Cancel]         │
└────────────────────────────────────┘
```

**Dialog 2: Chọn model**
```
┌────────────────────────────────────┐
│ Select Translation Model           │
├────────────────────────────────────┤
│ Choose NLLB-200 model:             │
│ (Larger models = better quality    │
│  but slower)                       │
│                                    │
│ ▼ NLLB-200 Distilled 600M          │  ← Fastest
│   NLLB-200 Distilled 1.3B          │
│   NLLB-200 1.3B                    │
│   NLLB-200 3.3B                    │  ← Best
│                                    │
│         [OK]      [Cancel]         │
└────────────────────────────────────┘
```

**Dialog 3: Confirm**
```
┌────────────────────────────────────┐
│ Confirm Translation                │
├────────────────────────────────────┤
│ Translate subtitles to Vietnamese? │
│                                    │
│ Model: NLLB-200 Distilled 600M    │
│ Source: English                    │
│ Target: Vietnamese (Tiếng Việt)   │
│                                    │
│ NLLB-200 supports 200+ languages   │
│ with high quality.                 │
│                                    │
│ Translation time depends on:       │
│ • Model size (larger = better)     │
│ • GPU availability (10-20x faster) │
│ • First-time download (~600MB)     │
│                                    │
│         [Yes]        [No]          │
└────────────────────────────────────┘
```

**Progress:**
```
Translating to Vietnamese (Tiếng Việt)
───────────────────────────────────────
Loading NLLB-200 Distilled 600M...
🎮 Using GPU: NVIDIA GeForce RTX 3060
⚡ Model loaded on GPU
🔄 Translating 42 segments: 
   English → Vietnamese (Tiếng Việt)
Translated 8/42 segments
Translated 16/42 segments
...
✅ Translation complete!
───────────────────────────────────────
         [Cancel]
```

### Bước 3: Kết quả

**Success dialog:**
```
┌────────────────────────────────────┐
│ Translation Complete               │
├────────────────────────────────────┤
│ ✅ Successfully translated          │
│    subtitles!                      │
│                                    │
│ 📝 Total segments: 42              │
│ 🌐 Model: NLLB-200 (Meta AI)      │
│                                    │
│ Translated subtitles will display  │
│ during playback.                   │
│                                    │
│            [OK]                    │
└────────────────────────────────────┘
```

---

## 🌍 Ngôn ngữ được hỗ trợ

### Top 20 ngôn ngữ phổ biến:

| Language | Code | Script |
|----------|------|--------|
| Vietnamese | vie_Latn | Latin |
| English | eng_Latn | Latin |
| Chinese (Simplified) | zho_Hans | Han |
| Chinese (Traditional) | zho_Hant | Han |
| Japanese | jpn_Jpan | Japanese |
| Korean | kor_Hang | Hangul |
| Thai | tha_Thai | Thai |
| Indonesian | ind_Latn | Latin |
| French | fra_Latn | Latin |
| German | deu_Latn | Latin |
| Spanish | spa_Latn | Latin |
| Portuguese | por_Latn | Latin |
| Russian | rus_Cyrl | Cyrillic |
| Arabic | arb_Arab | Arabic |
| Hindi | hin_Deva | Devanagari |
| Khmer | khm_Khmr | Khmer |
| Lao | lao_Laoo | Lao |
| Burmese | mya_Mymr | Myanmar |
| Tagalog | tgl_Latn | Latin |
| Malay | zsm_Latn | Latin |

**Tổng cộng: 200+ ngôn ngữ!**

---

## 🎛️ Chọn model phù hợp

### Model Options:

| Model | Size | Speed | Quality | Recommend |
|-------|------|-------|---------|-----------|
| **600M Distilled** | ~600MB | ⚡⚡⚡ Fast | ⭐⭐⭐ Good | ✅ Default |
| **1.3B Distilled** | ~1.3GB | ⚡⚡ Medium | ⭐⭐⭐⭐ Better | Testing |
| **1.3B** | ~1.3GB | ⚡⚡ Medium | ⭐⭐⭐⭐ Better | Production |
| **3.3B** | ~3.3GB | ⚡ Slow | ⭐⭐⭐⭐⭐ Best | High quality |

### Khi nào dùng model nào?

**600M Distilled - Fast & Good:**
```
Use when:
✅ Quick translation needed
✅ Testing/preview
✅ Limited GPU memory (<6GB)
✅ Many videos to process
```

**1.3B - Balanced:**
```
Use when:
✅ Production use
✅ Good GPU (6-8GB VRAM)
✅ Quality matters more than speed
```

**3.3B - Best Quality:**
```
Use when:
✅ Final/published content
✅ Professional use
✅ High-end GPU (10GB+ VRAM)
✅ Quality is critical
```

---

## 📊 Performance

### Translation Speed (GPU RTX 3060)

| Model | Segments/sec | 50 segments | 100 segments |
|-------|--------------|-------------|--------------|
| 600M | ~2.5 seg/s | ~20 sec | ~40 sec |
| 1.3B | ~1.5 seg/s | ~33 sec | ~66 sec |
| 3.3B | ~0.8 seg/s | ~62 sec | ~125 sec |

**CPU (Intel i7):**
- 600M: ~0.3 seg/s (10x slower)
- 1.3B: ~0.15 seg/s (20x slower)
- 3.3B: ~0.08 seg/s (30x slower)

### Memory Requirements

| Model | VRAM (GPU) | RAM | Disk |
|-------|------------|-----|------|
| 600M | ~2GB | ~4GB | ~600MB |
| 1.3B | ~4GB | ~6GB | ~1.3GB |
| 3.3B | ~8GB | ~10GB | ~3.3GB |

---

## 🎯 Use Cases

### Case 1: Video tiếng Việt → Phụ đề tiếng Anh

```
Video: Vietnamese tutorial
↓
Whisper: Translate to English
↓
Result: English subtitles
(Done! No need NLLB)
```

### Case 2: Video tiếng Việt → Phụ đề tiếng Việt

```
Video: Vietnamese vlog
↓
Whisper: Translate to English
↓
NLLB: English → Vietnamese
↓
Result: Vietnamese subtitles (high quality!)
```

### Case 3: Video tiếng Anh → Phụ đề tiếng Trung

```
Video: English podcast
↓
Whisper: Transcribe (English)
↓
NLLB: English → Chinese Simplified
↓
Result: Chinese subtitles
```

### Case 4: Video tiếng Nhật → Phụ đề tiếng Việt

```
Video: Japanese anime
↓
Whisper: Translate to English
↓
NLLB: English → Vietnamese
↓
Result: Vietnamese subtitles
```

### Case 5: Multi-language distribution

```
Video: English tutorial
↓
Whisper: Transcribe (English)
↓
NLLB: English → Vietnamese (save .srt)
NLLB: English → Chinese (save .srt)
NLLB: English → Japanese (save .srt)
NLLB: English → Korean (save .srt)
↓
Result: 4 subtitle files for different audiences!
```

---

## 💡 Tips & Best Practices

### ✅ Workflow tối ưu:

**1. Whisper first:**
```
Always start with Whisper to get clean English subtitles
English is the best pivot language for NLLB
```

**2. Choose right model:**
```
Testing: 600M (fast)
Production: 1.3B (balanced)
Professional: 3.3B (best)
```

**3. Batch processing:**
```
Process multiple videos:
- Use 600M for speed
- Translate to multiple languages at once
```

### ✅ Quality tips:

**For better translations:**
```
1. Clean English subtitles (fix Whisper errors first)
2. Use larger NLLB model (1.3B or 3.3B)
3. Review and edit in Subtitle Editor
4. Export and use!
```

### ✅ Memory management:

**Low memory?**
```
- Use 600M model
- Close other applications
- Process in smaller batches
- Use CPU if GPU OOM
```

**Enough memory?**
```
- Use 1.3B or 3.3B
- Better quality
- Still fast on GPU
```

---

## 🐛 Troubleshooting

### "Out of memory" error

**GPU OOM:**
```
→ Try smaller model (600M)
→ Close other GPU apps
→ Reduce batch size (edit code)
→ Use CPU mode
```

**RAM OOM:**
```
→ Close browser/other apps
→ Use 600M model
→ Restart app
```

### Model download slow/failed

```
→ Check internet connection
→ Wait patiently (first time only)
→ Models are cached: ~/.cache/huggingface/
→ Download manually if needed
```

### Translation quality poor

```
→ Use larger model (1.3B or 3.3B)
→ Check source subtitles quality
→ Edit manually in Subtitle Editor
→ Some languages better than others
```

### Weird characters in output

**NLLB-200 should fix this!**
```
✅ Better encoding handling
✅ Proper Unicode support
✅ Clean output
```

If still happens:
```
→ Check if correct language selected
→ Try different model
→ Report issue (may be model bug)
```

---

## 🔄 Context Window

NLLB implementation uses **sliding window context**:

```python
# Each subtitle gets context from previous sentence
Context: "Hello, my name is John."
Current: "I am a teacher."
→ Input: "Hello, my name is John. I am a teacher."
→ Output: [Vietnamese translation with context]
→ Extract: Only translation of current sentence
```

**Benefits:**
- ✅ Better pronoun handling
- ✅ Consistent terminology
- ✅ More natural translations
- ✅ Context awareness

---

## 📚 Technical Details

### Model Architecture

**NLLB-200:**
- Type: Transformer encoder-decoder
- Training: Multilingual parallel corpus
- Languages: 200+
- Context: 512 tokens

### Language Codes

**Format: `{language}_{script}`**

Examples:
- `eng_Latn` - English (Latin script)
- `vie_Latn` - Vietnamese (Latin script)
- `zho_Hans` - Chinese Simplified (Han script)
- `jpn_Jpan` - Japanese (Japanese script)
- `kor_Hang` - Korean (Hangul script)

### API Usage

```python
from core.nllb_translator import NLLBTranslator

translator = NLLBTranslator()

# Get available options
languages = translator.get_available_languages()
models = translator.get_available_models()

# Translate
translator.translate_subtitles(
    subtitles=subtitles_list,
    model_name="facebook/nllb-200-distilled-600M",
    source_lang="eng_Latn",
    target_lang="vie_Latn"
)
```

---

## 🎉 Summary

### Advantages over EnViT5:

| Feature | EnViT5 | NLLB-200 |
|---------|--------|----------|
| Languages | EN ↔ VI only | 200+ languages |
| Quality | Good | Excellent |
| Encoding issues | Sometimes | Rare |
| Flexibility | Low | Very high |
| Model sizes | 1 option | 4 options |
| Support | EN-VI only | Any pair |

### Why NLLB-200 is better:

✅ **More languages** - 200+ vs 2  
✅ **Better quality** - State-of-the-art  
✅ **Fewer errors** - Better encoding  
✅ **More flexible** - Choose model size  
✅ **Future-proof** - Meta AI maintained  

### Perfect for:

- 🌍 **International content** - Reach global audience
- 🎬 **Multi-language subtitles** - One video, many languages
- 📚 **Educational content** - Translate tutorials
- 🎤 **Podcasts** - Transcribe and translate
- 📺 **YouTube** - Auto-generate multiple subtitle files

---

**Enjoy translating to 200+ languages! 🌐✨**
