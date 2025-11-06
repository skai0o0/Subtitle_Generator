"""
Video Player Core - Xử lý logic video/audio player
"""
from PySide6.QtCore import QObject, Signal, Slot, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import os


class VideoPlayer(QObject):
    """Video player logic wrapper"""
    
    # Signals
    position_changed = Signal(int)
    duration_changed = Signal(int)
    state_changed = Signal(QMediaPlayer.PlaybackState)
    error_occurred = Signal(str)
    
    def __init__(self):
        super().__init__()
        
        # Media player
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        
        # Connect signals
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.media_player.playbackStateChanged.connect(self.state_changed)
        self.media_player.errorOccurred.connect(self._on_error)
        
        # State
        self.current_file = None
        
    def load_media(self, file_path):
        """Load media file"""
        if not os.path.exists(file_path):
            self.error_occurred.emit(f"File not found: {file_path}")
            return False
            
        self.current_file = file_path
        self.media_player.setSource(QUrl.fromLocalFile(file_path))
        return True
        
    def play(self):
        """Play media"""
        self.media_player.play()
        
    def pause(self):
        """Pause media"""
        self.media_player.pause()
        
    def stop(self):
        """Stop media"""
        self.media_player.stop()
        
    def seek(self, position_ms):
        """Seek to position in milliseconds"""
        self.media_player.setPosition(position_ms)
        
    def set_volume(self, volume):
        """Set volume (0.0 to 1.0)"""
        self.audio_output.setVolume(volume)
        
    def get_position(self):
        """Get current position in milliseconds"""
        return self.media_player.position()
        
    def get_duration(self):
        """Get duration in milliseconds"""
        return self.media_player.duration()
        
    def is_playing(self):
        """Check if media is playing"""
        return self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState
        
    @Slot(QMediaPlayer.Error, str)
    def _on_error(self, error, error_string):
        """Handle media error"""
        self.error_occurred.emit(error_string)
