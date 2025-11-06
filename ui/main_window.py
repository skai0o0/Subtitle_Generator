"""
Main Window - Giao diện chính của ứng dụng
"""
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QSlider, QLabel, QFileDialog, QMenuBar,
    QMenu, QStatusBar, QMessageBox, QStyle, QProgressDialog, QInputDialog,
    QSplitter, QTabWidget
)
from PySide6.QtCore import Qt, QUrl, QTimer, Slot, QEvent
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QAction, QKeySequence, QShortcut
import os

# Import core modules
from core.whisper_transcriber import WhisperTranscriber
from core.subtitle_manager import SubtitleManager
from core.playlist_manager import PlaylistManager
from core.nllb_translator import NLLBTranslator
from ui.subtitle_editor import SubtitleEditorWidget
from ui.playlist_widget import PlaylistWidget
from ui.fullscreen_overlay import FullscreenOverlay


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Subtitle Generator - Whisper AI")
        self.setGeometry(100, 100, 1200, 800)
        
        # Media player components
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        
        self.video_widget = QVideoWidget()
        self.video_widget.setMouseTracking(True)  # Enable mouse tracking
        self.media_player.setVideoOutput(self.video_widget)
        
        # Current media info
        self.current_media_path = None
        
        # Core modules
        self.transcriber = WhisperTranscriber()
        self.translator = NLLBTranslator()
        self.subtitle_manager = SubtitleManager()
        self.playlist_manager = PlaylistManager()
        
        # Progress dialog
        self.progress_dialog = None
        
        # Track last transcription task
        self.last_transcription_task = None
        
        # Fullscreen state
        self.is_fullscreen = False
        self.fullscreen_overlay = None
        
        # Setup UI
        self._create_menu_bar()
        self._create_ui()
        self._create_status_bar()
        self._connect_signals()
        self._connect_transcriber_signals()
        self._setup_fullscreen()
        
    def _create_menu_bar(self):
        """Tạo menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        open_action = QAction("&Open Video/Audio", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_media)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Transcribe menu
        transcribe_menu = menubar.addMenu("&Transcribe")
        
        transcribe_action = QAction("&Start Transcription", self)
        transcribe_action.setShortcut("Ctrl+T")
        transcribe_action.triggered.connect(self.start_transcription)
        transcribe_menu.addAction(transcribe_action)
        
        transcribe_menu.addSeparator()
        
        translate_action = QAction("� Translate Subtitles...", self)
        translate_action.setToolTip("Translate subtitles to any language using NLLB-200 (200+ languages)")
        translate_action.triggered.connect(self.translate_subtitles)
        transcribe_menu.addAction(translate_action)
        
        # Subtitle menu
        subtitle_menu = menubar.addMenu("&Subtitle")
        
        export_srt_action = QAction("Export as &SRT", self)
        export_srt_action.triggered.connect(self.export_srt)
        subtitle_menu.addAction(export_srt_action)
        
        export_vtt_action = QAction("Export as &VTT", self)
        export_vtt_action.triggered.connect(self.export_vtt)
        subtitle_menu.addAction(export_vtt_action)
        
        export_txt_action = QAction("Export as &TXT", self)
        export_txt_action.triggered.connect(self.export_txt)
        subtitle_menu.addAction(export_txt_action)
        
        subtitle_menu.addSeparator()
        
        import_srt_action = QAction("&Import SRT...", self)
        import_srt_action.triggered.connect(self.import_srt)
        subtitle_menu.addAction(import_srt_action)
        
        # View menu
        view_menu = menubar.addMenu("&View")
        
        fullscreen_action = QAction("&Fullscreen", self)
        fullscreen_action.setShortcut("F11")
        fullscreen_action.triggered.connect(self.toggle_fullscreen)
        view_menu.addAction(fullscreen_action)
        
        view_menu.addSeparator()
        
        self.toggle_editor_action = QAction("Show Right &Panel", self)
        self.toggle_editor_action.setCheckable(True)
        self.toggle_editor_action.setChecked(True)
        self.toggle_editor_action.triggered.connect(self.toggle_editor)
        view_menu.addAction(self.toggle_editor_action)
        
        # Help menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def _create_ui(self):
        """Tạo giao diện chính"""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout with splitter
        main_layout = QVBoxLayout(central_widget)
        
        # Create splitter for video area and editor
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left side: Video player area
        video_container = QWidget()
        video_layout = QVBoxLayout(video_container)
        
        # Video widget (chiếm phần lớn không gian)
        self.video_widget.setMinimumHeight(400)
        video_layout.addWidget(self.video_widget, stretch=3)
        
        # Subtitle display area
        self.subtitle_label = QLabel("Subtitle sẽ hiển thị ở đây")
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle_label.setStyleSheet("""
            QLabel {
                background-color: rgba(0, 0, 0, 150);
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
        """)
        self.subtitle_label.setMaximumHeight(80)
        video_layout.addWidget(self.subtitle_label)
        
        # Timeline slider
        timeline_layout = QHBoxLayout()
        
        self.time_label = QLabel("00:00:00")
        timeline_layout.addWidget(self.time_label)
        
        self.timeline_slider = QSlider(Qt.Orientation.Horizontal)
        self.timeline_slider.setRange(0, 0)
        self.timeline_slider.sliderMoved.connect(self.seek_position)
        timeline_layout.addWidget(self.timeline_slider)
        
        self.duration_label = QLabel("00:00:00")
        timeline_layout.addWidget(self.duration_label)
        
        video_layout.addLayout(timeline_layout)
        
        # Media controls
        controls_layout = QHBoxLayout()
        
        # Previous file button
        self.previous_button = QPushButton("⏮️")
        self.previous_button.setToolTip("Previous file in playlist")
        self.previous_button.setEnabled(False)
        self.previous_button.clicked.connect(self.play_previous_file)
        controls_layout.addWidget(self.previous_button)
        
        # Seek backward button
        self.seek_backward_button = QPushButton("⏪ 5s")
        self.seek_backward_button.setToolTip("Seek backward 5 seconds")
        self.seek_backward_button.clicked.connect(self.seek_backward)
        controls_layout.addWidget(self.seek_backward_button)
        
        # Play/Pause button
        self.play_button = QPushButton()
        self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.play_button.clicked.connect(self.toggle_play_pause)
        controls_layout.addWidget(self.play_button)
        
        # Stop button
        self.stop_button = QPushButton()
        self.stop_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaStop))
        self.stop_button.clicked.connect(self.stop_media)
        controls_layout.addWidget(self.stop_button)
        
        # Seek forward button
        self.seek_forward_button = QPushButton("5s ⏩")
        self.seek_forward_button.setToolTip("Seek forward 5 seconds")
        self.seek_forward_button.clicked.connect(self.seek_forward)
        controls_layout.addWidget(self.seek_forward_button)
        
        # Next file button
        self.next_button = QPushButton("⏭️")
        self.next_button.setToolTip("Next file in playlist")
        self.next_button.setEnabled(False)
        self.next_button.clicked.connect(self.play_next_file)
        controls_layout.addWidget(self.next_button)
        
        controls_layout.addStretch()
        
        # Volume control
        volume_label = QLabel("Volume:")
        controls_layout.addWidget(volume_label)
        
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(70)
        self.volume_slider.setMaximumWidth(150)
        self.volume_slider.valueChanged.connect(self.change_volume)
        controls_layout.addWidget(self.volume_slider)
        
        self.volume_label_value = QLabel("70%")
        controls_layout.addWidget(self.volume_label_value)
        
        controls_layout.addStretch()
        
        # Fullscreen button
        self.fullscreen_button = QPushButton("⛶")
        self.fullscreen_button.setToolTip("Fullscreen (F11)")
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen)
        self.fullscreen_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                min-width: 40px;
                min-height: 40px;
                border-radius: 5px;
            }
        """)
        controls_layout.addWidget(self.fullscreen_button)
        
        # Transcribe button
        self.transcribe_button = QPushButton("🎤 Transcribe with Whisper AI")
        self.transcribe_button.setEnabled(False)
        self.transcribe_button.clicked.connect(self.start_transcription)
        self.transcribe_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        controls_layout.addWidget(self.transcribe_button)
        
        # Toggle editor button
        self.toggle_editor_button = QPushButton("📝 Hide Panel")
        self.toggle_editor_button.clicked.connect(self.toggle_editor)
        self.toggle_editor_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        controls_layout.addWidget(self.toggle_editor_button)
        
        video_layout.addLayout(controls_layout)
        
        # Add video container to splitter
        self.splitter.addWidget(video_container)
        
        # Right side: Tab widget for editor and playlist
        self.right_tab_widget = QTabWidget()
        
        # Subtitle editor tab
        self.subtitle_editor = SubtitleEditorWidget()
        self.subtitle_editor.subtitles_changed.connect(self.on_subtitles_edited)
        self.subtitle_editor.subtitle_selected.connect(self.seek_to_subtitle)
        self.right_tab_widget.addTab(self.subtitle_editor, "📝 Subtitle Editor")
        
        # Playlist tab
        self.playlist_widget = PlaylistWidget()
        self.playlist_widget.file_selected.connect(self.load_from_playlist)
        self.right_tab_widget.addTab(self.playlist_widget, "🎵 Playlist")
        
        self.splitter.addWidget(self.right_tab_widget)
        
        # Set splitter sizes (60% video, 40% right panel)
        self.splitter.setSizes([600, 400])
        
        # Load playlist history
        self._refresh_playlist()
        
        # Add splitter to main layout
        main_layout.addWidget(self.splitter)
        
        # Set initial volume
        self.change_volume(70)
        
        # Timer for updating position
        self.position_timer = QTimer()
        self.position_timer.setInterval(100)
        self.position_timer.timeout.connect(self.update_position)
        self.position_timer.start()
        
    def _create_status_bar(self):
        """Tạo status bar"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready - Load a video/audio file to start")
        
    def _connect_signals(self):
        """Kết nối signals"""
        self.media_player.playbackStateChanged.connect(self.on_playback_state_changed)
        self.media_player.durationChanged.connect(self.on_duration_changed)
        self.media_player.errorOccurred.connect(self.on_error_occurred)
        
    def _connect_transcriber_signals(self):
        """Kết nối transcriber signals"""
        self.transcriber.progress.connect(self.on_transcription_progress)
        self.transcriber.finished.connect(self.on_transcription_finished)
        self.transcriber.error.connect(self.on_transcription_error)
        
        # Connect translator signals
        self.translator.progress.connect(self.on_translation_progress)
        self.translator.finished.connect(self.on_translation_finished)
        self.translator.error.connect(self.on_translation_error)
        
    @Slot()
    def open_media(self):
        """Mở file media"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Video/Audio File",
            "",
            "Media Files (*.mp4 *.avi *.mkv *.mov *.mp3 *.wav *.m4a);;All Files (*.*)"
        )
        
        if file_path:
            self.load_media(file_path)
            
    def load_media(self, file_path):
        """Load media file"""
        if not os.path.exists(file_path):
            QMessageBox.warning(self, "Error", "File not found!")
            return
            
        # Add to playlist
        self.playlist_manager.add_file(file_path)
        self._refresh_playlist()
        
        self.current_media_path = file_path
        self.media_player.setSource(QUrl.fromLocalFile(file_path))
        self.transcribe_button.setEnabled(True)
        
        file_name = os.path.basename(file_path)
        self.status_bar.showMessage(f"Loaded: {file_name}")
        self.setWindowTitle(f"Subtitle Generator - {file_name}")
        
        # Clear previous subtitles
        self.subtitle_manager.set_subtitles([])
        self.subtitle_editor.set_subtitles([])
        self.subtitle_label.setText("No subtitles yet - Click 'Transcribe with Whisper AI'")
        
    @Slot()
    def toggle_play_pause(self):
        """Toggle play/pause"""
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()
            
    @Slot()
    def stop_media(self):
        """Stop media"""
        self.media_player.stop()
        
    @Slot(int)
    def seek_position(self, position):
        """Seek to position"""
        self.media_player.setPosition(position)
        
    @Slot(int)
    def change_volume(self, value):
        """Change volume"""
        self.audio_output.setVolume(value / 100.0)
        self.volume_label_value.setText(f"{value}%")
        
    @Slot()
    def update_position(self):
        """Update timeline position"""
        if self.media_player.duration() > 0:
            position = self.media_player.position()
            duration = self.media_player.duration()
            
            self.timeline_slider.setValue(position)
            self.time_label.setText(self._format_time(position))
            
            # Update subtitle display
            self._update_subtitle_display(position)
            
            # Highlight current subtitle in editor
            if self.subtitle_editor.isVisible():
                self.subtitle_editor.highlight_current_subtitle(position)
                
            # Update fullscreen overlay
            if self.is_fullscreen and self.fullscreen_overlay:
                self.fullscreen_overlay.update_position(position, duration)
            
    @Slot(int)
    def on_duration_changed(self, duration):
        """When duration changes"""
        self.timeline_slider.setRange(0, duration)
        self.duration_label.setText(self._format_time(duration))
        
    @Slot(QMediaPlayer.PlaybackState)
    def on_playback_state_changed(self, state):
        """When playback state changes"""
        is_playing = state == QMediaPlayer.PlaybackState.PlayingState
        
        if is_playing:
            self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        else:
            self.play_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
            
        # Update fullscreen overlay
        if self.is_fullscreen and self.fullscreen_overlay:
            self.fullscreen_overlay.update_play_icon(is_playing)
            
    @Slot(QMediaPlayer.Error, str)
    def on_error_occurred(self, error, error_string):
        """When error occurs"""
        QMessageBox.critical(self, "Media Error", f"Error: {error_string}")
        self.status_bar.showMessage(f"Error: {error_string}")
        
    def _format_time(self, ms):
        """Format milliseconds to HH:MM:SS"""
        seconds = ms // 1000
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
    def _update_subtitle_display(self, position_ms):
        """Update subtitle display based on current position"""
        subtitle_text = self.subtitle_manager.get_subtitle_at_time(position_ms)
        
        if subtitle_text:
            self.subtitle_label.setText(subtitle_text)
        else:
            self.subtitle_label.setText("")
            
        # Update fullscreen overlay subtitle
        if self.is_fullscreen and self.fullscreen_overlay:
            self.fullscreen_overlay.update_subtitle(subtitle_text if subtitle_text else "")
        
    @Slot()
    def start_transcription(self):
        """Start transcription with Whisper AI"""
        if not self.current_media_path:
            QMessageBox.warning(self, "Warning", "Please load a media file first!")
            return
        
        # Step 1: Ask user to choose mode (Transcribe or Translate)
        mode_dialog = QMessageBox(self)
        mode_dialog.setWindowTitle("Choose Mode")
        mode_dialog.setText("Select transcription mode:")
        mode_dialog.setInformativeText(
            "🎤 Transcribe: Generate subtitles in the original language of the video\n\n"
            "🌐 Translate: Generate subtitles in English (translates from any language)"
        )
        
        transcribe_button = mode_dialog.addButton("🎤 Transcribe", QMessageBox.ButtonRole.AcceptRole)
        translate_button = mode_dialog.addButton("🌐 Translate to English", QMessageBox.ButtonRole.AcceptRole)
        cancel_button = mode_dialog.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)
        
        mode_dialog.setDefaultButton(transcribe_button)
        mode_dialog.exec()
        
        clicked_button = mode_dialog.clickedButton()
        
        if clicked_button == cancel_button:
            return
        
        # Determine task type
        task = "transcribe" if clicked_button == transcribe_button else "translate"
        
        # Step 2: Ask user to choose Whisper model
        models = ["tiny", "base", "small", "medium", "large"]
        model_descriptions = [
            "tiny (fastest, least accurate)",
            "base (balanced)",
            "small (good quality)",
            "medium (better quality, slower)",
            "large (best quality, very slow)"
        ]
        
        model, ok = QInputDialog.getItem(
            self,
            "Select Whisper Model",
            "Choose transcription model:\n(larger models are more accurate but slower)",
            model_descriptions,
            1,  # Default to "base"
            False
        )
        
        if not ok:
            return
            
        # Extract model name
        model_name = models[model_descriptions.index(model)]
        
        # Create progress dialog
        mode_text = "Translating to English" if task == "translate" else "Transcribing"
        self.progress_dialog = QProgressDialog(
            f"Initializing {mode_text.lower()}...",
            "Cancel",
            0, 0,
            self
        )
        self.progress_dialog.setWindowTitle(f"{mode_text} with Whisper AI")
        self.progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progress_dialog.canceled.connect(self.cancel_transcription)
        self.progress_dialog.show()
        
        # Disable transcribe button
        self.transcribe_button.setEnabled(False)
        
        # Save task type for potential follow-up translation
        self.last_transcription_task = task
        
        # Start transcription with task parameter
        self.transcriber.transcribe_video(self.current_media_path, model_name, task=task)
        
    @Slot()
    def cancel_transcription(self):
        """Cancel transcription"""
        self.transcriber.stop()
        if self.progress_dialog:
            self.progress_dialog.close()
        self.transcribe_button.setEnabled(True)
        self.status_bar.showMessage("Transcription cancelled")
        
    @Slot(str)
    def on_transcription_progress(self, message):
        """Update transcription progress"""
        if self.progress_dialog:
            self.progress_dialog.setLabelText(message)
        self.status_bar.showMessage(message)
        
    @Slot(list)
    def on_transcription_finished(self, subtitles):
        """When transcription is finished"""
        if self.progress_dialog:
            self.progress_dialog.close()
            
        self.transcribe_button.setEnabled(True)
        
        # Store subtitles
        self.subtitle_manager.set_subtitles(subtitles)
        
        # Update editor
        self.subtitle_editor.set_subtitles(subtitles)
        
        # Show success message
        QMessageBox.information(
            self,
            "Transcription Complete",
            f"Successfully transcribed audio!\n\n"
            f"Found {len(subtitles)} subtitle segments.\n\n"
            f"Subtitles will now display during playback.\n"
            f"You can edit them in the Subtitle Editor panel.\n"
            f"Export using the Subtitle menu."
        )
        
        self.status_bar.showMessage(f"Transcription complete - {len(subtitles)} segments")
        self.subtitle_label.setText("▶ Play video to see subtitles")
        
    @Slot(str)
    def on_transcription_error(self, error_msg):
        """When transcription error occurs"""
        if self.progress_dialog:
            self.progress_dialog.close()
            
        self.transcribe_button.setEnabled(True)
        
        QMessageBox.critical(self, "Transcription Error", error_msg)
        self.status_bar.showMessage(f"Error: {error_msg}")
        
    @Slot()
    def export_srt(self):
        """Export subtitles as SRT"""
        if not self.subtitle_manager.get_subtitles():
            QMessageBox.warning(self, "Warning", "No subtitles to export!")
            return
            
        # Ask for save location
        default_name = os.path.splitext(os.path.basename(self.current_media_path))[0] + ".srt"
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Subtitles as SRT",
            default_name,
            "SRT Files (*.srt);;All Files (*.*)"
        )
        
        if file_path:
            if self.subtitle_manager.export_srt(file_path):
                QMessageBox.information(self, "Success", f"Subtitles exported successfully!\n\n{file_path}")
                self.status_bar.showMessage(f"Exported: {file_path}")
            else:
                QMessageBox.critical(self, "Error", "Failed to export subtitles!")
        
    @Slot()
    def export_vtt(self):
        """Export subtitles as VTT"""
        if not self.subtitle_manager.get_subtitles():
            QMessageBox.warning(self, "Warning", "No subtitles to export!")
            return
            
        # Ask for save location
        default_name = os.path.splitext(os.path.basename(self.current_media_path))[0] + ".vtt"
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Subtitles as WebVTT",
            default_name,
            "WebVTT Files (*.vtt);;All Files (*.*)"
        )
        
        if file_path:
            if self.subtitle_manager.export_vtt(file_path):
                QMessageBox.information(self, "Success", f"Subtitles exported successfully!\n\n{file_path}")
                self.status_bar.showMessage(f"Exported: {file_path}")
            else:
                QMessageBox.critical(self, "Error", "Failed to export subtitles!")
        
    @Slot()
    def export_txt(self):
        """Export subtitles as plain TXT"""
        if not self.subtitle_manager.get_subtitles():
            QMessageBox.warning(self, "Warning", "No subtitles to export!")
            return
            
        # Ask for save location
        default_name = os.path.splitext(os.path.basename(self.current_media_path))[0] + ".txt"
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Subtitles as TXT",
            default_name,
            "Text Files (*.txt);;All Files (*.*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    for subtitle in self.subtitle_manager.get_subtitles():
                        # Simple format: just the text
                        f.write(subtitle['text'] + '\n\n')
                        
                QMessageBox.information(self, "Success", f"Subtitles exported successfully!\n\n{file_path}")
                self.status_bar.showMessage(f"Exported: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export: {str(e)}")
                
    @Slot()
    def import_srt(self):
        """Import subtitles from SRT file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Import SRT File",
            "",
            "SRT Files (*.srt);;All Files (*.*)"
        )
        
        if file_path:
            if self.subtitle_manager.import_srt(file_path):
                subtitles = self.subtitle_manager.get_subtitles()
                self.subtitle_editor.set_subtitles(subtitles)
                QMessageBox.information(
                    self,
                    "Success",
                    f"Imported {len(subtitles)} subtitles successfully!"
                )
                self.status_bar.showMessage(f"Imported: {file_path}")
                self.subtitle_label.setText("▶ Play video to see imported subtitles")
            else:
                QMessageBox.critical(self, "Error", "Failed to import SRT file!")
                
    @Slot()
    def toggle_editor(self):
        """Toggle right panel visibility"""
        is_visible = self.right_tab_widget.isVisible()
        self.right_tab_widget.setVisible(not is_visible)
        self.toggle_editor_action.setChecked(not is_visible)
        
        # Update button text
        if is_visible:
            self.toggle_editor_button.setText("📝 Show Panel")
        else:
            self.toggle_editor_button.setText("📝 Hide Panel")
        
    @Slot(list)
    def on_subtitles_edited(self, subtitles):
        """When subtitles are edited in editor"""
        self.subtitle_manager.set_subtitles(subtitles)
        self.status_bar.showMessage(f"Subtitles updated - {len(subtitles)} segments")
        
    @Slot(int)
    def seek_to_subtitle(self, position_ms):
        """Seek video to subtitle position"""
        self.media_player.setPosition(position_ms)
        
    @Slot()
    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(
            self,
            "About Subtitle Generator",
            "<h2>Subtitle Generator</h2>"
            "<p>Version 2.0</p>"
            "<p>Tạo subtitle tự động cho video/audio sử dụng Whisper AI</p>"
            "<p><b>Features:</b></p>"
            "<ul>"
            "<li>GPU-accelerated transcription</li>"
            "<li>Real-time subtitle editing</li>"
            "<li>Playlist management</li>"
            "<li>Export SRT/VTT/TXT formats</li>"
            "<li>Import existing SRT files</li>"
            "</ul>"
            "<p><b>Technologies:</b></p>"
            "<ul>"
            "<li>PySide6 - GUI Framework</li>"
            "<li>Whisper AI - Speech-to-Text</li>"
            "<li>FFmpeg - Media Processing</li>"
            "<li>CUDA - GPU Acceleration</li>"
            "</ul>"
        )
    
    # ========== Translation Methods ==========
    
    @Slot()
    def translate_subtitles(self):
        """Translate subtitles to any language using NLLB-200"""
        # Check if we have subtitles
        if not self.subtitle_manager.get_subtitles():
            QMessageBox.warning(
                self,
                "No Subtitles",
                "Please transcribe or load subtitles first!\n\n"
                "Use: Transcribe → Start Transcription"
            )
            return
        
        # Step 1: Select target language
        languages = self.translator.get_available_languages()
        
        # Find Vietnamese as default
        default_lang_idx = languages.index("Vietnamese (Tiếng Việt)") if "Vietnamese (Tiếng Việt)" in languages else 0
        
        target_language, ok = QInputDialog.getItem(
            self,
            "Select Target Language",
            "Translate subtitles to:",
            languages,
            default_lang_idx,
            False
        )
        
        if not ok:
            return
        
        # Step 2: Select NLLB model
        models = self.translator.get_available_models()
        
        model_choice, ok = QInputDialog.getItem(
            self,
            "Select Translation Model",
            "Choose NLLB-200 model:\n(Larger models = better quality but slower)",
            models,
            0,  # Default to fastest model
            False
        )
        
        if not ok:
            return
        
        # Get model name and language codes
        model_name = self.translator.get_model_name(model_choice)
        target_lang_code = self.translator.get_language_code(target_language)
        
        # Assume source is English (from Whisper translate mode)
        source_lang_code = "eng_Latn"
        
        # Ask for confirmation
        confirm_dialog = QMessageBox(self)
        confirm_dialog.setWindowTitle("Confirm Translation")
        confirm_dialog.setIcon(QMessageBox.Icon.Question)
        confirm_dialog.setText(f"Translate subtitles to {target_language}?")
        confirm_dialog.setInformativeText(
            f"Model: {model_choice}\n"
            f"Source: English\n"
            f"Target: {target_language}\n\n"
            f"NLLB-200 supports 200+ languages with high quality.\n\n"
            f"Translation time depends on:\n"
            f"• Model size (larger = slower but better)\n"
            f"• Number of subtitle segments\n"
            f"• GPU availability (10-20x faster)\n"
            f"• First-time model download (~600MB-13GB)\n\n"
            f"Continue?"
        )
        confirm_dialog.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        confirm_dialog.setDefaultButton(QMessageBox.StandardButton.Yes)
        
        if confirm_dialog.exec() != QMessageBox.StandardButton.Yes:
            return
        
        # Get current subtitles
        subtitles = self.subtitle_manager.get_subtitles()
        
        # Create progress dialog
        self.progress_dialog = QProgressDialog(
            f"Initializing {model_choice}...",
            "Cancel",
            0, 100,
            self
        )
        self.progress_dialog.setWindowTitle(f"Translating to {target_language}")
        self.progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progress_dialog.canceled.connect(self.cancel_translation)
        self.progress_dialog.show()
        
        # Disable transcribe button during translation
        self.transcribe_button.setEnabled(False)
        
        # Start translation
        self.translator.translate_subtitles(
            subtitles, 
            model_name,
            source_lang_code,
            target_lang_code
        )
    
    @Slot()
    def cancel_translation(self):
        """Cancel translation"""
        self.translator.stop()
        if self.progress_dialog:
            self.progress_dialog.close()
        self.transcribe_button.setEnabled(True)
        self.status_bar.showMessage("Translation cancelled")
    
    @Slot(str, int)
    def on_translation_progress(self, message, percentage):
        """Update translation progress"""
        if self.progress_dialog:
            self.progress_dialog.setLabelText(message)
            self.progress_dialog.setValue(percentage)
        self.status_bar.showMessage(message)
    
    @Slot(list)
    def on_translation_finished(self, translated_subtitles):
        """When translation is finished"""
        if self.progress_dialog:
            self.progress_dialog.close()
        
        self.transcribe_button.setEnabled(True)
        
        # Store translated subtitles
        self.subtitle_manager.set_subtitles(translated_subtitles)
        
        # Update editor
        self.subtitle_editor.set_subtitles(translated_subtitles)
        
        # Show success message
        QMessageBox.information(
            self,
            "Translation Complete",
            f"✅ Successfully translated subtitles!\n\n"
            f"📝 Total segments: {len(translated_subtitles)}\n"
            f"🌐 Model: NLLB-200 (Meta AI)\n\n"
            f"Translated subtitles will display during playback.\n"
            f"You can edit them in the Subtitle Editor panel.\n"
            f"Export using the Subtitle menu."
        )
        
        self.status_bar.showMessage(f"Translation complete - {len(translated_subtitles)} segments")
        self.subtitle_label.setText("▶ Play video to see translated subtitles")
    
    @Slot(str)
    def on_translation_error(self, error_msg):
        """When translation error occurs"""
        if self.progress_dialog:
            self.progress_dialog.close()
        
        self.transcribe_button.setEnabled(True)
        
        QMessageBox.critical(
            self,
            "Translation Error",
            f"Failed to translate subtitles:\n\n{error_msg}\n\n"
            f"Possible causes:\n"
            f"• Model download failed (check internet connection)\n"
            f"• Out of memory (try smaller model or close other apps)\n"
            f"• CUDA errors (try CPU-only mode)\n"
            f"• Unsupported language combination\n\n"
            f"Try a smaller NLLB model (600M) or check console for details."
        )
        self.status_bar.showMessage(f"Translation error: {error_msg}")
        
    # ========== Playlist Methods ==========
    
    def _refresh_playlist(self):
        """Refresh playlist display"""
        playlist = self.playlist_manager.get_playlist()
        current_index = self.playlist_manager.get_current_index()
        self.playlist_widget.set_playlist(playlist, current_index)
        self._update_navigation_buttons()
        
    def _update_navigation_buttons(self):
        """Update prev/next button states"""
        self.previous_button.setEnabled(self.playlist_manager.has_previous())
        self.next_button.setEnabled(self.playlist_manager.has_next())
        
    @Slot(str)
    def load_from_playlist(self, file_path):
        """Load file từ playlist khi user chọn"""
        # Update playlist manager
        index = self.playlist_manager.get_playlist().index(file_path)
        self.playlist_manager.set_current_index(index)
        
        # Load file
        self._load_media_file(file_path)
        
        # Update UI
        self._refresh_playlist()
        
    @Slot()
    def play_previous_file(self):
        """Play file trước trong playlist"""
        file_path = self.playlist_manager.get_previous_file()
        if file_path:
            self._load_media_file(file_path)
            self._refresh_playlist()
            self.status_bar.showMessage(f"Playing previous: {os.path.basename(file_path)}")
            
    @Slot()
    def play_next_file(self):
        """Play file kế tiếp trong playlist"""
        file_path = self.playlist_manager.get_next_file()
        if file_path:
            self._load_media_file(file_path)
            self._refresh_playlist()
            self.status_bar.showMessage(f"Playing next: {os.path.basename(file_path)}")
            
    @Slot()
    def seek_backward(self):
        """Tua lui 5 giây"""
        current_position = self.media_player.position()
        new_position = max(0, current_position - 5000)  # 5 seconds = 5000 ms
        self.media_player.setPosition(new_position)
        
    @Slot()
    def seek_forward(self):
        """Tua tới 5 giây"""
        current_position = self.media_player.position()
        duration = self.media_player.duration()
        new_position = min(duration, current_position + 5000)  # 5 seconds = 5000 ms
        self.media_player.setPosition(new_position)
        
    def _load_media_file(self, file_path):
        """Helper method để load media file"""
        self.current_media_path = file_path
        self.media_player.setSource(QUrl.fromLocalFile(file_path))
        self.transcribe_button.setEnabled(True)
        self.subtitle_label.setText("🎬 Video loaded - Click Transcribe or Play")
        
        # Clear previous subtitles
        self.subtitle_manager.clear()
        self.subtitle_editor.set_subtitles([])
        
        # Auto play
        self.media_player.play()
        
    # ========== Fullscreen Methods ==========
    
    def _setup_fullscreen(self):
        """Setup fullscreen overlay"""
        self.fullscreen_overlay = FullscreenOverlay(self.video_widget)
        self.fullscreen_overlay.hide()
        
        # Connect overlay signals
        self.fullscreen_overlay.play_pause_clicked.connect(self.toggle_play_pause)
        self.fullscreen_overlay.stop_clicked.connect(self.stop_media)
        self.fullscreen_overlay.seek_backward_clicked.connect(self.seek_backward)
        self.fullscreen_overlay.seek_forward_clicked.connect(self.seek_forward)
        self.fullscreen_overlay.previous_clicked.connect(self.play_previous_file)
        self.fullscreen_overlay.next_clicked.connect(self.play_next_file)
        self.fullscreen_overlay.volume_changed.connect(self.change_volume)
        self.fullscreen_overlay.position_changed.connect(self.seek_position)
        self.fullscreen_overlay.exit_fullscreen.connect(self.exit_fullscreen)
        
        # Install event filter for video widget
        self.video_widget.installEventFilter(self)
        
    @Slot()
    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        if self.is_fullscreen:
            self.exit_fullscreen()
        else:
            self.enter_fullscreen()
            
    def enter_fullscreen(self):
        """Enter fullscreen mode"""
        self.is_fullscreen = True
        
        # Hide main window elements
        self.menuBar().hide()
        self.status_bar.hide()
        self.right_tab_widget.hide()
        
        # Make video widget fullscreen
        self.video_widget.setParent(None)
        self.video_widget.showFullScreen()
        
        # Setup overlay - IMPORTANT: Set parent AFTER video widget is fullscreen
        self.fullscreen_overlay.setParent(self.video_widget)
        self.fullscreen_overlay.setWindowFlags(Qt.WindowType.Widget)  # Make sure it's a widget, not a window
        
        # Use QTimer to ensure video widget is rendered before showing overlay
        QTimer.singleShot(100, self._show_fullscreen_overlay)
        
    def _show_fullscreen_overlay(self):
        """Show fullscreen overlay after video widget is ready"""
        if not self.is_fullscreen:
            return
            
        # Set overlay geometry to match video widget
        self.fullscreen_overlay.setGeometry(0, 0, self.video_widget.width(), self.video_widget.height())
        self.fullscreen_overlay.raise_()  # Bring to front
        self.fullscreen_overlay.show()
        self.fullscreen_overlay.setWindowOpacity(1.0)
        
        # Update overlay state
        if self.current_media_path:
            filename = os.path.basename(self.current_media_path)
            self.fullscreen_overlay.set_title(filename)
            
        self.fullscreen_overlay.update_volume(self.volume_slider.value())
        self.fullscreen_overlay.set_navigation_enabled(
            self.playlist_manager.has_previous(),
            self.playlist_manager.has_next()
        )
        
        # Start hide timer
        self.fullscreen_overlay.hide_timer.start(self.fullscreen_overlay.auto_hide_delay)
        
    @Slot()
    def exit_fullscreen(self):
        """Exit fullscreen mode"""
        if not self.is_fullscreen:
            return
            
        self.is_fullscreen = False
        
        # Hide overlay
        self.fullscreen_overlay.hide()
        
        # Restore video widget to main window
        self.video_widget.showNormal()
        
        # Re-add video widget to layout
        # Find video container in splitter
        video_container = self.splitter.widget(0)
        if video_container:
            layout = video_container.layout()
            if layout:
                # Insert video widget back at position 0 (before subtitle label)
                layout.insertWidget(0, self.video_widget, stretch=3)
        
        # Show main window elements
        self.menuBar().show()
        self.status_bar.show()
        self.right_tab_widget.show()
        
    def eventFilter(self, obj, event):
        """Event filter for video widget"""
        if obj == self.video_widget:
            if event.type() == QEvent.Type.MouseMove and self.is_fullscreen:
                # Show overlay on mouse move
                if self.fullscreen_overlay and self.fullscreen_overlay.isVisible():
                    self.fullscreen_overlay.show_overlay()
            elif event.type() == QEvent.Type.MouseButtonDblClick and self.is_fullscreen:
                # Double-click to exit fullscreen
                self.exit_fullscreen()
                return True
            elif event.type() == QEvent.Type.Resize and self.is_fullscreen:
                # Resize overlay when video widget resizes
                if self.fullscreen_overlay and self.fullscreen_overlay.isVisible():
                    self.fullscreen_overlay.setGeometry(0, 0, self.video_widget.width(), self.video_widget.height())
                
        return super().eventFilter(obj, event)
        
    def keyPressEvent(self, event):
        """Handle key press events"""
        # F11 or Esc to toggle/exit fullscreen
        if event.key() == Qt.Key.Key_F11:
            self.toggle_fullscreen()
        elif event.key() == Qt.Key.Key_Escape and self.is_fullscreen:
            self.exit_fullscreen()
        else:
            super().keyPressEvent(event)
