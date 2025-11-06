# 🎵 Playlist Feature Guide

## 🎉 New Playlist Features!

### ✨ What's New:

1. **🎵 Playlist Tab** - Manage multiple media files
2. **⏮️⏭️ Navigation** - Previous/Next file buttons
3. **⏪⏩ Seek Control** - Jump ±5 seconds
4. **💾 History** - Auto-save playlist between sessions
5. **🔄 Auto-load** - Restore playlist on startup

---

## 🎨 UI Layout

```
┌────────────────────────────────────────────────────┐
│ Menu Bar                                           │
├──────────────────────┬─────────────────────────────┤
│                      │ 📝 Subtitle Editor │ 🎵 Playlist
│   Video Player       │ ┌───────────────────────┐   │
│                      │ │ video1.mp4            │   │
│   [Video Display]    │ │ video2.mp4 (playing)  │   │
│                      │ │ audio.mp3             │   │
│   [Subtitle Text]    │ └───────────────────────┘   │
│                      │ [🗑️ Remove] [🧹 Clear]    │
│ [⏮️][⏪5s][▶️][⏹️][5s⏩][⏭️] │                          │
│                      │                              │
└──────────────────────┴──────────────────────────────┘
```

---

## 📖 How to Use

### 1️⃣ Open Files
**Method 1: File Menu**
```
File → Open Video/Audio
→ Select file
→ Auto-added to playlist
```

**Method 2: Drag & Drop** (if supported)
```
Drag file to window
→ Auto-added to playlist
```

### 2️⃣ Playlist Management

**View Playlist:**
- Click **🎵 Playlist** tab
- See all loaded files
- Current file highlighted in **blue & bold**

**Play File:**
- **Double-click** any file in list
- Or right-click → **▶️ Play**

**Remove File:**
- Select file
- Click **🗑️ Remove** button
- Or right-click → **🗑️ Remove**

**Clear All:**
- Click **🧹 Clear All**
- Removes all files from playlist

---

## 🎮 Navigation Controls

### ⏮️ Previous File
```
Button: ⏮️ (Left of play controls)
Shortcut: (can add later)
Action: Load and play previous file in playlist
```

### ⏭️ Next File
```
Button: ⏭️ (Right of play controls)
Shortcut: (can add later)
Action: Load and play next file in playlist
```

**Note:** Buttons auto-disable when at start/end of playlist

---

## ⏪⏩ Seek Controls

### ⏪ Seek Backward 5s
```
Button: ⏪ 5s
Action: Jump back 5 seconds
Use Case: Review subtitle timing
```

### ⏩ Seek Forward 5s
```
Button: 5s ⏩
Action: Jump forward 5 seconds
Use Case: Skip parts quickly
```

**Tip:** Perfect for fine-tuning subtitle timing!

---

## 💾 Playlist History

### Auto-Save
- Playlist saved to `playlist_history.json`
- Saved when:
  - Add file
  - Remove file
  - Clear playlist
  - Change current file

### Auto-Load
- On startup, automatically loads previous playlist
- Filters out non-existent files
- Restores last playing position

### History File Location
```
subtitle-generator-ver2/
├── playlist_history.json  ← Auto-generated
├── main.py
└── ...
```

**Format:**
```json
{
  "playlist": [
    "C:/Videos/video1.mp4",
    "C:/Videos/video2.mp4",
    "C:/Music/audio.mp3"
  ],
  "current_index": 1
}
```

---

## 🎯 Workflow Examples

### Workflow 1: Batch Processing
```
1. Open multiple videos
2. Transcribe first video
3. Export subtitle
4. Click ⏭️ Next
5. Repeat for all files
```

### Workflow 2: Review & Edit
```
1. Load playlist from history
2. Jump between files with ⏮️⏭️
3. Use ⏪⏩ for precise timing
4. Edit subtitles
5. Export all
```

### Workflow 3: Project Management
```
1. Add all project videos
2. Work on each incrementally
3. Playlist persists between sessions
4. Resume where you left off
```

---

## 🎓 Tips & Tricks

### ✅ Quick Navigation
- **Keyboard focus** on playlist → Arrow keys to select
- **Enter** to play selected file
- **Delete** to remove (if implemented)

### ✅ Playlist Organization
- Files appear in order added
- Current file always highlighted
- See file count in header

### ✅ Seek Shortcuts
```
⏪ 5s = Quick review
⏩ 5s = Skip ahead
Perfect for:
- Finding subtitle start/end
- Reviewing timing
- Quick navigation
```

### ✅ Auto-Play
- When navigating with ⏮️⏭️
- File loads and auto-plays
- Subtitle cleared for new file

### ✅ History Persistence
- Close app anytime
- Reopen → playlist restored
- Continue where you left off!

---

## 🔧 Controls Reference

| Button | Icon | Action | Enabled When |
|--------|------|--------|--------------|
| Previous File | ⏮️ | Play previous | Has previous file |
| Seek Backward | ⏪ 5s | Jump back 5s | Video loaded |
| Play/Pause | ▶️/⏸️ | Toggle playback | Video loaded |
| Stop | ⏹️ | Stop playback | Video loaded |
| Seek Forward | 5s ⏩ | Jump forward 5s | Video loaded |
| Next File | ⏭️ | Play next | Has next file |

---

## 📊 Playlist Features

### Display
- **File name** shown (not full path)
- **Current file** in blue & bold
- **File count** in header
- **Scrollable** for many files

### Context Menu (Right-click)
```
▶️ Play       - Load and play file
🗑️ Remove     - Remove from playlist
```

### Keyboard Support
- Arrow keys for selection
- Double-click to play
- Enter to play (if focused)

---

## 🐛 Troubleshooting

### Playlist not saving?
→ Check write permissions in folder
→ Look for `playlist_history.json`

### Files missing on reload?
→ History filters deleted files
→ Only existing files loaded

### Can't navigate to next/previous?
→ Check button enabled state
→ Need multiple files in playlist

### Seek not working?
→ Ensure video is loaded
→ Check video has valid duration

### Current file not highlighted?
→ Check playlist tab
→ Should be blue & bold

---

## 🎬 Use Cases

### 1. YouTube Series
```
Load all episodes
Transcribe each
Export subtitles
Navigate with ⏮️⏭️
```

### 2. Podcast Episodes
```
Add all audio files
Batch transcribe
Use seek for review
Export transcripts
```

### 3. Course Videos
```
Import lecture videos
Transcribe sequentially
Edit timing with ⏪⏩
Export for upload
```

### 4. Multi-language Project
```
Load source videos
Transcribe all
Import translations
Review with playlist
```

---

## 🎉 Summary

### You Can Now:
✅ Manage multiple files in playlist
✅ Navigate between files with ⏮️⏭️
✅ Seek ±5 seconds with ⏪⏩
✅ Auto-save playlist history
✅ Restore playlist on startup
✅ See current file highlighted
✅ Remove/clear playlist files
✅ Quick file switching

---

## 🚀 Future Enhancements

Potential features:
- [ ] Drag & drop file support
- [ ] Keyboard shortcuts (Ctrl+Left/Right)
- [ ] Playlist import/export
- [ ] Sort playlist options
- [ ] Jump to timestamp
- [ ] Custom seek intervals
- [ ] Loop current file
- [ ] Shuffle playlist

---

**Manage your media library efficiently! 🎵✨**
