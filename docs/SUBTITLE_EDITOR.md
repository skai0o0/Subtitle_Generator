# 📝 Subtitle Editor Feature Guide

## 🎉 New Features Added!

### ✨ What's New:

1. **📝 Subtitle Editor Panel** - Edit subtitles in real-time
2. **➕ Add/Edit/Delete** - Full CRUD operations
3. **📥 Import SRT** - Load existing subtitle files
4. **📤 Export TXT** - Plain text export
5. **🎯 Click to Seek** - Select subtitle to jump to that position
6. **✏️ Double-click Edit** - Quick editing

---

## 🎨 UI Layout

```
┌─────────────────────────────────────────────────────┐
│ Menu: File | Transcribe | Subtitle | View | Help   │
├──────────────────────┬──────────────────────────────┤
│                      │                              │
│   Video Player       │   📝 Subtitle Editor         │
│   Area               │   ┌──────────────────────┐   │
│                      │   │ # | Start | End | Text│  │
│   [Video Display]    │   ├──────────────────────┤   │
│                      │   │ 1 | 00:00 | 00:03 | ..│  │
│   [Subtitle Text]    │   │ 2 | 00:03 | 00:07 | ..│  │
│                      │   │ 3 | 00:07 | 00:12 | ..│  │
│   [Timeline ─●───]   │   └──────────────────────┘   │
│                      │                              │
│   [▶️ ⏸️ ⏹️ 🔊 🎤]    │   [➕ Add] [✏️ Edit] [🗑️ Del] │
│                      │                              │
└──────────────────────┴──────────────────────────────┘
```

---

## 📖 How to Use

### 1️⃣ After Transcription
When transcription completes, subtitles automatically appear in the editor:
```
✅ Transcription complete
✅ Subtitle editor populated
✅ Ready to edit!
```

### 2️⃣ Edit Subtitle
**Method 1: Double-click**
- Double-click any row in the table
- Edit dialog opens

**Method 2: Select & Click Edit**
- Click on a row
- Click **✏️ Edit** button

**Edit Dialog:**
```
┌───────────────────────────┐
│ Edit Subtitle             │
├───────────────────────────┤
│ Start Time: [00:00:03.500]│
│ End Time:   [00:00:07.200]│
│                           │
│ Subtitle Text:            │
│ ┌───────────────────────┐ │
│ │ Enter text here...    │ │
│ └───────────────────────┘ │
│                           │
│        [OK] [Cancel]      │
└───────────────────────────┘
```

### 3️⃣ Add New Subtitle
1. Click **➕ Add** button
2. Edit dialog opens with default values
3. Set start/end time and text
4. Click OK
5. New subtitle added and sorted by time

### 4️⃣ Delete Subtitle
1. Select subtitle row
2. Click **🗑️ Delete** button
3. Confirm deletion
4. Subtitle removed

### 5️⃣ Clear All
1. Click **🧹 Clear All** button
2. Confirm action
3. All subtitles removed

### 6️⃣ Jump to Subtitle
- Click on any subtitle row
- Video automatically seeks to that time
- Perfect for reviewing specific parts!

---

## 📥 Import SRT File

### Steps:
1. Menu: **Subtitle → Import SRT...**
2. Choose .srt file
3. Subtitles loaded into editor
4. ✅ Ready to edit or playback

**Supported Format:**
```srt
1
00:00:00,000 --> 00:00:03,500
First subtitle text

2
00:00:03,500 --> 00:00:07,200
Second subtitle text
```

---

## 📤 Export Options

### 1. Export as SRT (SubRip)
```
Subtitle → Export as SRT
Format: Standard SRT with timestamps
Use: Video players, YouTube, etc.
```

### 2. Export as VTT (WebVTT)
```
Subtitle → Export as VTT
Format: Web-compatible format
Use: HTML5 video, web players
```

### 3. Export as TXT (Plain Text) ⭐ NEW
```
Subtitle → Export as TXT
Format: Simple text, no timestamps
Use: Scripts, transcripts, documentation
```

**TXT Example:**
```
First subtitle text

Second subtitle text

Third subtitle text
```

---

## 👁️ View Controls

### Show/Hide Editor
- **Menu:** View → Show Subtitle Editor
- **Checkmark** indicates visibility
- **Keyboard:** (can add shortcut)

**Why hide?**
- Focus on video playback
- More screen space for video
- Presentation mode

---

## 🎯 Workflow Examples

### Workflow 1: Transcribe & Fine-tune
```
1. Load video
2. Click Transcribe
3. Wait for completion
4. Review in editor
5. Edit any mistakes
6. Export SRT
```

### Workflow 2: Import & Edit
```
1. Load video
2. Import existing SRT
3. Play and review
4. Edit timestamps/text
5. Export updated SRT
```

### Workflow 3: Manual Creation
```
1. Load video
2. Click Add for each subtitle
3. Set times by playing video
4. Enter text
5. Export
```

---

## 🎓 Tips & Tricks

### ✅ Quick Editing
- **Double-click** = Fastest way to edit
- **Tab** = Navigate between fields
- **Enter** = Save and close dialog

### ✅ Review Workflow
1. Select subtitle in editor
2. Video jumps to that time
3. Watch and verify
4. Edit if needed
5. Move to next

### ✅ Time Format
```
HH:MM:SS,mmm
Hours : Minutes : Seconds , Milliseconds

Example:
00:01:23,500 = 1 min 23.5 seconds
```

### ✅ Multi-line Text
- Press **Enter** in text editor
- Create multi-line subtitles
- Will display properly on screen

### ✅ Sorting
- Subtitles auto-sort by start time
- Add/Edit anywhere, always stays ordered
- No manual sorting needed!

---

## 🔧 Keyboard Shortcuts (Planned)

| Action | Shortcut | Status |
|--------|----------|--------|
| Add Subtitle | Ctrl+N | 🔜 Coming |
| Edit Selected | Ctrl+E | 🔜 Coming |
| Delete Selected | Del | 🔜 Coming |
| Import SRT | Ctrl+I | 🔜 Coming |
| Export SRT | Ctrl+S | 🔜 Coming |

---

## 📊 Editor Features

### Table Columns:
1. **#** - Sequential number
2. **Start** - Start timestamp (HH:MM:SS,mmm)
3. **End** - End timestamp
4. **Text** - Subtitle content (truncated if long)

### Button States:
- **➕ Add** - Always enabled
- **✏️ Edit** - Enabled when subtitle selected
- **🗑️ Delete** - Enabled when subtitle selected
- **🧹 Clear All** - Enabled when subtitles exist

### Counter:
- Shows total subtitle count
- Updates in real-time
- Example: "125 subtitles"

---

## 🎬 Use Cases

### 1. Content Creation
- Transcribe YouTube videos
- Edit for accuracy
- Add custom formatting
- Export for upload

### 2. Translation
- Import English SRT
- Edit text to Vietnamese
- Keep same timestamps
- Export translated version

### 3. Accessibility
- Create closed captions
- Fine-tune timing
- Ensure readability
- Export multiple formats

### 4. Archive/Documentation
- Transcribe meetings
- Export as TXT for notes
- Keep SRT for video
- Easy to search/reference

---

## 🐛 Troubleshooting

### Editor not showing?
→ View → Show Subtitle Editor ✓

### Can't edit?
→ Select a row first, then click Edit

### Subtitles not syncing?
→ Check start/end times in editor
→ Use click-to-seek to verify

### Import failed?
→ Check SRT format
→ Must have proper timestamps

### Changes not saved?
→ Click OK in edit dialog
→ Check status bar for confirmation

---

## 🎉 Summary

### You Can Now:
✅ Edit subtitles visually
✅ Add/delete entries
✅ Import existing SRT
✅ Export TXT format
✅ Jump to any subtitle
✅ See all subtitles at once
✅ Real-time updates
✅ Professional workflow

---

**Master your subtitles with the new editor! 📝✨**
