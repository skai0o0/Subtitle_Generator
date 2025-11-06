# 🎤🌐 New Feature: Transcribe & Translate Mode

## ✨ What's New?

When you click **"🎤 Transcribe with Whisper AI"**, you now get a popup to choose:

### 🎤 Transcribe Mode
- Generates subtitles in the **original language** of the video
- Vietnamese video → Vietnamese subtitles
- Japanese video → Japanese subtitles
- Auto-detects the language

### 🌐 Translate Mode
- Generates subtitles in **English**
- Vietnamese video → English subtitles
- Japanese video → English subtitles
- Any language → English subtitles
- Perfect for international audiences

---

## 🚀 Quick Start

1. **Load a video**: `File → Open Video/Audio` (Ctrl+O)

2. **Click Transcribe button**: `🎤 Transcribe with Whisper AI`

3. **Choose mode in popup**:
   ```
   ┌──────────────────────────────────┐
   │ Select transcription mode:       │
   │                                  │
   │ 🎤 Transcribe                    │
   │    (original language)           │
   │                                  │
   │ 🌐 Translate to English          │
   │    (any language → English)      │
   └──────────────────────────────────┘
   ```

4. **Choose model**: `base` (recommended) or others

5. **Wait for processing**: Progress dialog shows status

6. **Done!**: Subtitles appear and can be edited/exported

---

## 🎯 When to Use Each Mode?

### Use 🎤 Transcribe when:
✅ Viewers understand the original language  
✅ Need subtitles for deaf/hard-of-hearing  
✅ Learning the language (watch + read same language)  
✅ Want to preserve original language  

### Use 🌐 Translate when:
✅ Viewers don't understand the original language  
✅ Want to share internationally  
✅ Need English subtitles for YouTube/social media  
✅ Translating content for global audience  

---

## 📝 Examples

### Example 1: Vietnamese Tutorial
```
Video: Vietnamese cooking tutorial
Mode: 🎤 Transcribe
Result: Vietnamese subtitles
→ Vietnamese viewers can follow along
```

### Example 2: Vietnamese for Tourists
```
Video: Vietnam travel guide
Mode: 🌐 Translate to English
Result: English subtitles
→ International tourists understand
```

### Example 3: Japanese Anime Learning
```
Video: Japanese anime
Mode: 🎤 Transcribe
Result: Japanese subtitles (hiragana/katakana)
→ Learn Japanese vocabulary
```

### Example 4: Japanese Anime Watching
```
Video: Japanese anime
Mode: 🌐 Translate to English
Result: English subtitles
→ Understand the story
```

---

## 🔧 Technical Details

**Files Modified:**
- `ui/main_window.py` - Added mode selection dialog
- `core/whisper_transcriber.py` - Added translate support

**Whisper API:**
- `task="transcribe"` - Keep original language
- `task="translate"` - Translate to English
- Auto-detects source language in both modes

**Supported Languages:**
99+ languages including Vietnamese, English, Japanese, Chinese, Korean, Thai, French, German, Spanish, etc.

---

## 🧪 Testing

**Test the demo:**
```bash
python demo_transcribe_translate.py
```

**Test in main app:**
```bash
python main.py
```
1. Load a video
2. Click transcribe button
3. See the new popup
4. Choose mode and model
5. Process completes

---

## 📚 Full Documentation

See `TRANSCRIBE_TRANSLATE_GUIDE.md` for complete guide with:
- Detailed usage instructions
- Performance comparisons
- Best practices
- Troubleshooting
- Technical details

---

**Enjoy creating subtitles in any language! 🎤🌐✨**
