"""
Fullscreen Overlay Widget - Controls overlay for fullscreen mode
"""
from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSlider, 
    QLabel, QStyle
)
from PySide6.QtCore import Qt, QTimer, Signal, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPalette, QColor


class FullscreenOverlay(QWidget):
    """Overlay controls for fullscreen mode"""
    
    # Signals
    play_pause_clicked = Signal()
    stop_clicked = Signal()
    seek_backward_clicked = Signal()
    seek_forward_clicked = Signal()
    previous_clicked = Signal()
    next_clicked = Signal()
    volume_changed = Signal(int)
    position_changed = Signal(int)
    exit_fullscreen = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        # Don't use FramelessWindowHint - just make it a normal widget
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setMouseTracking(True)  # Enable mouse tracking
        
        # Auto-hide timer
        self.hide_timer = QTimer()
        self.hide_timer.setSingleShot(True)
        self.hide_timer.timeout.connect(self._auto_hide)
        self.auto_hide_delay = 3000  # 3 seconds
        
        # Track visibility state
        self._is_controls_visible = True
        
        self._create_ui()
        self._setup_animation()
        
    def _create_ui(self):
        """Create UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Top bar with exit button
        top_bar = QWidget()
        top_bar.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 180);
            }
        """)
        top_layout = QHBoxLayout(top_bar)
        
        self.title_label = QLabel("Fullscreen Mode")
        self.title_label.setStyleSheet("color: white; font-size: 16px; padding: 10px;")
        top_layout.addWidget(self.title_label)
        
        top_layout.addStretch()
        
        # Esc hint
        esc_hint = QLabel("Press Esc to exit")
        esc_hint.setStyleSheet("color: rgba(255, 255, 255, 150); font-size: 12px; padding: 10px;")
        top_layout.addWidget(esc_hint)
        
        self.exit_button = QPushButton("✕ Exit Fullscreen")
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 0, 0, 150);
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: rgba(255, 0, 0, 200);
            }
        """)
        self.exit_button.clicked.connect(self.exit_fullscreen.emit)
        top_layout.addWidget(self.exit_button)
        
        layout.addWidget(top_bar)
        
        # Middle section for subtitle
        middle_widget = QWidget()
        middle_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        middle_layout = QVBoxLayout(middle_widget)
        middle_layout.addStretch()
        
        # Subtitle label
        self.subtitle_label = QLabel("")
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setStyleSheet("""
            QLabel {
                background-color: rgba(0, 0, 0, 180);
                color: white;
                font-size: 24px;
                font-weight: bold;
                padding: 15px 30px;
                border-radius: 8px;
            }
        """)
        self.subtitle_label.hide()  # Hidden by default
        middle_layout.addWidget(self.subtitle_label)
        
        middle_layout.addSpacing(100)  # Space above bottom bar
        
        layout.addWidget(middle_widget)
        
        # Bottom control bar
        bottom_bar = QWidget()
        bottom_bar.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 180);
            }
        """)
        bottom_layout = QVBoxLayout(bottom_bar)
        bottom_layout.setContentsMargins(20, 10, 20, 10)
        
        # Timeline
        timeline_layout = QHBoxLayout()
        
        self.time_label = QLabel("00:00:00")
        self.time_label.setStyleSheet("color: white; font-size: 14px;")
        timeline_layout.addWidget(self.time_label)
        
        self.timeline_slider = QSlider(Qt.Orientation.Horizontal)
        self.timeline_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 8px;
                background: rgba(255, 255, 255, 50);
                margin: 2px 0;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: white;
                border: 2px solid #2196F3;
                width: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }
            QSlider::handle:horizontal:hover {
                background: #2196F3;
            }
        """)
        self.timeline_slider.sliderMoved.connect(self.position_changed.emit)
        timeline_layout.addWidget(self.timeline_slider)
        
        self.duration_label = QLabel("00:00:00")
        self.duration_label.setStyleSheet("color: white; font-size: 14px;")
        timeline_layout.addWidget(self.duration_label)
        
        bottom_layout.addLayout(timeline_layout)
        
        # Control buttons
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(10)
        
        # Previous button
        self.previous_button = QPushButton("⏮️")
        self.previous_button.setToolTip("Previous file")
        self.previous_button.clicked.connect(self.previous_clicked.emit)
        self._style_button(self.previous_button)
        controls_layout.addWidget(self.previous_button)
        
        # Seek backward
        self.seek_backward_button = QPushButton("⏪ 5s")
        self.seek_backward_button.clicked.connect(self.seek_backward_clicked.emit)
        self._style_button(self.seek_backward_button)
        controls_layout.addWidget(self.seek_backward_button)
        
        # Play/Pause
        self.play_button = QPushButton("▶️")
        self.play_button.clicked.connect(self.play_pause_clicked.emit)
        self._style_button(self.play_button, large=True)
        controls_layout.addWidget(self.play_button)
        
        # Stop
        self.stop_button = QPushButton("⏹️")
        self.stop_button.clicked.connect(self.stop_clicked.emit)
        self._style_button(self.stop_button)
        controls_layout.addWidget(self.stop_button)
        
        # Seek forward
        self.seek_forward_button = QPushButton("5s ⏩")
        self.seek_forward_button.clicked.connect(self.seek_forward_clicked.emit)
        self._style_button(self.seek_forward_button)
        controls_layout.addWidget(self.seek_forward_button)
        
        # Next button
        self.next_button = QPushButton("⏭️")
        self.next_button.setToolTip("Next file")
        self.next_button.clicked.connect(self.next_clicked.emit)
        self._style_button(self.next_button)
        controls_layout.addWidget(self.next_button)
        
        controls_layout.addStretch()
        
        # Volume control
        volume_label = QLabel("🔊")
        volume_label.setStyleSheet("color: white; font-size: 20px;")
        controls_layout.addWidget(volume_label)
        
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(70)
        self.volume_slider.setMaximumWidth(150)
        self.volume_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 6px;
                background: rgba(255, 255, 255, 50);
                margin: 2px 0;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: white;
                border: 2px solid #4CAF50;
                width: 14px;
                margin: -4px 0;
                border-radius: 7px;
            }
        """)
        self.volume_slider.valueChanged.connect(self.volume_changed.emit)
        controls_layout.addWidget(self.volume_slider)
        
        self.volume_label = QLabel("70%")
        self.volume_label.setStyleSheet("color: white; font-size: 14px; min-width: 40px;")
        controls_layout.addWidget(self.volume_label)
        
        bottom_layout.addLayout(controls_layout)
        
        layout.addWidget(bottom_bar)
        
    def _style_button(self, button, large=False):
        """Apply style to button"""
        size = "50px" if large else "40px"
        font_size = "24px" if large else "16px"
        
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: rgba(255, 255, 255, 30);
                color: white;
                font-size: {font_size};
                min-width: {size};
                min-height: {size};
                border: 2px solid rgba(255, 255, 255, 50);
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: rgba(255, 255, 255, 50);
                border: 2px solid rgba(255, 255, 255, 100);
            }}
            QPushButton:pressed {{
                background-color: rgba(255, 255, 255, 70);
            }}
        """)
        
    def _setup_animation(self):
        """Setup fade animation"""
        self.fade_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_animation.setDuration(300)
        self.fade_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        
    def show_overlay(self):
        """Show overlay with fade in"""
        if not self._is_controls_visible:
            self._is_controls_visible = True
            self.show()
            self.setWindowOpacity(1.0)
            self.raise_()  # Bring to front
        self.hide_timer.start(self.auto_hide_delay)
        
    def _auto_hide(self):
        """Auto hide overlay"""
        if self._is_controls_visible:
            self._is_controls_visible = False
            self.fade_animation.setStartValue(1.0)
            self.fade_animation.setEndValue(0.0)
            # Disconnect previous connections to avoid multiple calls
            try:
                self.fade_animation.finished.disconnect()
            except:
                pass
            self.fade_animation.finished.connect(self._hide_after_fade)
            self.fade_animation.start()
            
    def _hide_after_fade(self):
        """Hide widget after fade animation completes"""
        # Don't actually hide, just make transparent so we can still detect mouse events
        # self.hide()
        pass
        
    def update_position(self, position_ms, duration_ms):
        """Update timeline position"""
        if duration_ms > 0:
            self.timeline_slider.setRange(0, duration_ms)
            self.timeline_slider.setValue(position_ms)
            self.time_label.setText(self._format_time(position_ms))
            self.duration_label.setText(self._format_time(duration_ms))
            
    def update_play_icon(self, is_playing):
        """Update play/pause icon"""
        self.play_button.setText("⏸️" if is_playing else "▶️")
        
    def update_volume(self, value):
        """Update volume display"""
        self.volume_slider.setValue(value)
        self.volume_label.setText(f"{value}%")
        
    def set_title(self, title):
        """Set title"""
        self.title_label.setText(title)
        
    def set_navigation_enabled(self, has_previous, has_next):
        """Enable/disable navigation buttons"""
        self.previous_button.setEnabled(has_previous)
        self.next_button.setEnabled(has_next)
        
    def update_subtitle(self, text):
        """Update subtitle text"""
        if text:
            self.subtitle_label.setText(text)
            self.subtitle_label.show()
        else:
            self.subtitle_label.hide()
        
    def _format_time(self, ms):
        """Format milliseconds to HH:MM:SS"""
        seconds = ms // 1000
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
    def enterEvent(self, event):
        """Mouse enter - show overlay"""
        self.hide_timer.stop()
        if self.windowOpacity() < 1.0 or not self._is_controls_visible:
            self.show_overlay()
        super().enterEvent(event)
        
    def leaveEvent(self, event):
        """Mouse leave - start hide timer"""
        self.hide_timer.start(self.auto_hide_delay)
        super().leaveEvent(event)
        
    def mouseMoveEvent(self, event):
        """Mouse move - show overlay"""
        self.show_overlay()
        super().mouseMoveEvent(event)
