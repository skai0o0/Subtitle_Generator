# 🤝 Contributing to Subtitle Generator Ver 2

Thank you for considering contributing to this project! 

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Coding Standards](#coding-standards)
- [Submitting Changes](#submitting-changes)

---

## 📜 Code of Conduct

This project follows a simple code of conduct:
- Be respectful and constructive
- Help others learn and grow
- Keep discussions professional
- Report any inappropriate behavior

---

## 🚀 How to Contribute

### Reporting Bugs 🐛
1. Check if the bug has already been reported in [Issues](https://github.com/YOUR_USERNAME/subtitle-generator-ver2/issues)
2. If not, create a new issue with:
   - Clear title describing the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - System info (OS, Python version, GPU/CPU)
   - Screenshots if applicable

### Suggesting Features 💡
1. Check existing feature requests
2. Create an issue with `[Feature Request]` prefix
3. Describe:
   - What problem does it solve?
   - How should it work?
   - Any alternative solutions considered?

### Improving Documentation 📚
- Fix typos, grammar, or unclear explanations
- Add examples or clarifications
- Translate docs to other languages
- Update outdated information

---

## 🛠️ Development Setup

### Prerequisites
- Python 3.8-3.11
- Git
- FFmpeg
- CUDA (optional, for GPU)

### Clone and Setup
```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/subtitle-generator-ver2.git
cd subtitle-generator-ver2

# 3. Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/subtitle-generator-ver2.git

# 4. Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Linux/Mac

# 5. Install dependencies
pip install -r requirements.txt

# 6. Test setup
python test_setup.py

# 7. Run app
python main.py
```

---

## 📁 Project Structure

```
subtitle-generator-ver2/
│
├── main.py                    # Entry point
│
├── core/                      # Core business logic
│   ├── video_player.py       # Video playback
│   ├── whisper_transcriber.py # AI transcription
│   ├── nllb_translator.py    # Translation (NLLB-200)
│   ├── subtitle_manager.py   # Subtitle management
│   └── playlist_manager.py   # Playlist features
│
├── ui/                        # User interface
│   ├── main_window.py        # Main GUI window
│   ├── fullscreen_overlay.py # Fullscreen controls
│   ├── subtitle_editor.py    # Subtitle editor dialog
│   └── playlist_widget.py    # Playlist widget
│
├── utils/                     # Utility functions
│
└── assets/                    # Resources (if any)
```

### Key Files
- **main.py**: Application entry point, initializes QApplication
- **ui/main_window.py**: Main window with all UI components (500+ lines)
- **core/whisper_transcriber.py**: Whisper AI integration with GPU support
- **core/nllb_translator.py**: NLLB-200 translation with 200+ languages

---

## 💻 Coding Standards

### Python Style
- Follow **PEP 8** style guide
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use descriptive variable names

### Example:
```python
class MyClass:
    """Class docstring explaining purpose"""
    
    def __init__(self, param1, param2):
        """Initialize with parameters"""
        self.param1 = param1
        self.param2 = param2
    
    def my_method(self):
        """Method docstring explaining what it does"""
        # Clear comments for complex logic
        result = self._helper_method()
        return result
    
    def _helper_method(self):
        """Private helper method (starts with _)"""
        pass
```

### Documentation
- Add docstrings to all classes and functions
- Use comments for complex logic
- Update relevant .md files when adding features

### Qt/PySide6 Guidelines
- Use signals for inter-component communication
- Keep UI logic in `ui/` folder
- Keep business logic in `core/` folder
- Use QThreads for long-running operations (don't block UI)

### Git Commit Messages
```
Type: Brief description (50 chars max)

More detailed explanation if needed (wrap at 72 chars).
- Bullet points are okay
- Reference issues: Fixes #123

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation only
- style: Code style changes (formatting)
- refactor: Code refactoring
- test: Adding tests
- chore: Maintenance tasks
```

Example:
```
feat: Add NLLB-200 translation with 200+ languages

- Integrated Meta's NLLB-200 model
- Added language selection UI (200+ languages)
- Implemented sliding window context for better translation
- Auto VRAM cleanup after translation

Fixes #45
```

---

## 🔄 Submitting Changes

### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/my-new-feature
   ```

2. **Make your changes**
   - Write clean, documented code
   - Follow coding standards
   - Test thoroughly

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: Add my new feature"
   ```

4. **Pull latest changes from upstream**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/my-new-feature
   ```

6. **Create Pull Request**
   - Go to GitHub
   - Click "New Pull Request"
   - Fill in the template:
     ```markdown
     ## Description
     Brief description of changes
     
     ## Type of Change
     - [ ] Bug fix
     - [ ] New feature
     - [ ] Documentation update
     - [ ] Code refactoring
     
     ## Testing
     - [ ] Tested on Windows
     - [ ] Tested on Linux/Mac
     - [ ] Tested with GPU
     - [ ] Tested with CPU-only
     
     ## Screenshots (if applicable)
     
     ## Related Issues
     Fixes #123
     ```

7. **Wait for review**
   - Address feedback if requested
   - Make changes in same branch
   - Push updates (will auto-update PR)

### PR Checklist
- ✅ Code follows project style guidelines
- ✅ Self-reviewed code
- ✅ Commented complex sections
- ✅ Updated documentation if needed
- ✅ Tested changes thoroughly
- ✅ No breaking changes (or clearly documented)
- ✅ Meaningful commit messages

---

## 🧪 Testing

### Manual Testing
```bash
# 1. Run setup test
python test_setup.py

# 2. Test main app
python main.py

# 3. Test specific features
python test_fullscreen.py
python demo_translation.py
```

### Test Cases to Consider
- ✅ Load different video formats (MP4, AVI, MKV)
- ✅ Test with/without GPU
- ✅ Test with different Whisper models
- ✅ Test transcribe vs translate modes
- ✅ Test translation with different languages
- ✅ Test fullscreen mode
- ✅ Test playlist features
- ✅ Test subtitle export/import

---

## 🆘 Getting Help

### Resources
- **Documentation**: Read all .md files in the repo
- **Issues**: Check existing issues for similar problems
- **Discussions**: Start a discussion for questions

### Contact
- Open an issue with `[Question]` prefix
- Be specific about what you need help with
- Include relevant code snippets or screenshots

---

## 📝 License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers this project.

---

## 🎉 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes for their contributions
- Given credit in relevant documentation

Thank you for contributing! 🙏

---

**Happy Coding! 🚀**
