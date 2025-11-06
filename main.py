"""
Subtitle Generator - Main Entry Point
Ứng dụng tạo subtitle tự động cho video/audio sử dụng Whisper AI
"""
import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("Subtitle Generator")
    app.setOrganizationName("SubtitleGen")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
