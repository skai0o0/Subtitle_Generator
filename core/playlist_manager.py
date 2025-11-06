"""
Playlist Manager - Quản lý danh sách phát
"""
import json
import os
from pathlib import Path


class PlaylistManager:
    """Quản lý playlist và history"""
    
    def __init__(self, history_file="playlist_history.json"):
        """
        Args:
            history_file: File để lưu history
        """
        self.playlist = []
        self.current_index = -1
        self.history_file = history_file
        self._load_history()
        
    def add_file(self, file_path):
        """
        Thêm file vào playlist
        
        Args:
            file_path: Đường dẫn file
            
        Returns:
            int: Index của file trong playlist
        """
        if not os.path.exists(file_path):
            return -1
            
        # Normalize path
        file_path = str(Path(file_path).resolve())
        
        # Nếu file đã có trong playlist, chuyển đến đó
        if file_path in self.playlist:
            self.current_index = self.playlist.index(file_path)
            return self.current_index
            
        # Thêm file mới
        self.playlist.append(file_path)
        self.current_index = len(self.playlist) - 1
        self._save_history()
        return self.current_index
        
    def remove_file(self, index):
        """
        Xóa file khỏi playlist
        
        Args:
            index: Index của file
            
        Returns:
            bool: True nếu xóa thành công
        """
        if 0 <= index < len(self.playlist):
            self.playlist.pop(index)
            
            # Adjust current index
            if self.current_index >= len(self.playlist):
                self.current_index = len(self.playlist) - 1
            elif self.current_index > index:
                self.current_index -= 1
                
            self._save_history()
            return True
        return False
        
    def clear_playlist(self):
        """Xóa toàn bộ playlist"""
        self.playlist = []
        self.current_index = -1
        self._save_history()
        
    def get_current_file(self):
        """
        Lấy file hiện tại
        
        Returns:
            str: Đường dẫn file hoặc None
        """
        if 0 <= self.current_index < len(self.playlist):
            return self.playlist[self.current_index]
        return None
        
    def get_next_file(self):
        """
        Lấy file kế tiếp
        
        Returns:
            str: Đường dẫn file hoặc None
        """
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            return self.playlist[self.current_index]
        return None
        
    def get_previous_file(self):
        """
        Lấy file trước đó
        
        Returns:
            str: Đường dẫn file hoặc None
        """
        if self.current_index > 0:
            self.current_index -= 1
            return self.playlist[self.current_index]
        return None
        
    def has_next(self):
        """Check có file kế tiếp không"""
        return self.current_index < len(self.playlist) - 1
        
    def has_previous(self):
        """Check có file trước đó không"""
        return self.current_index > 0
        
    def get_playlist(self):
        """
        Lấy toàn bộ playlist
        
        Returns:
            list: Danh sách các file path
        """
        return self.playlist.copy()
        
    def get_current_index(self):
        """Lấy index hiện tại"""
        return self.current_index
        
    def set_current_index(self, index):
        """
        Set index hiện tại
        
        Args:
            index: Index mới
            
        Returns:
            str: File path tại index đó hoặc None
        """
        if 0 <= index < len(self.playlist):
            self.current_index = index
            return self.playlist[self.current_index]
        return None
        
    def _save_history(self):
        """Lưu playlist history ra file"""
        try:
            data = {
                'playlist': self.playlist,
                'current_index': self.current_index
            }
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving playlist history: {e}")
            
    def _load_history(self):
        """Load playlist history từ file"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                # Filter out non-existent files
                self.playlist = [f for f in data.get('playlist', []) if os.path.exists(f)]
                self.current_index = data.get('current_index', -1)
                
                # Adjust current index if needed
                if self.current_index >= len(self.playlist):
                    self.current_index = len(self.playlist) - 1
        except Exception as e:
            print(f"Error loading playlist history: {e}")
            self.playlist = []
            self.current_index = -1
