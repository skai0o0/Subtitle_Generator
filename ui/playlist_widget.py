"""
Playlist Widget - Hiển thị danh sách phát
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QPushButton, QLabel, QMenu
)
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QAction
import os


class PlaylistWidget(QWidget):
    """Widget hiển thị playlist"""
    
    # Signals
    file_selected = Signal(str)  # Khi user chọn file
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_index = -1
        self._create_ui()
        
    def _create_ui(self):
        """Tạo UI"""
        layout = QVBoxLayout(self)
        
        # Header
        header_layout = QHBoxLayout()
        header_label = QLabel("🎵 Playlist")
        header_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        header_layout.addWidget(header_label)
        
        self.count_label = QLabel("0 files")
        self.count_label.setStyleSheet("color: #666;")
        header_layout.addWidget(self.count_label)
        header_layout.addStretch()
        layout.addLayout(header_layout)
        
        # List widget
        self.list_widget = QListWidget()
        self.list_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_widget.customContextMenuRequested.connect(self._show_context_menu)
        self.list_widget.itemDoubleClicked.connect(self._on_item_double_clicked)
        layout.addWidget(self.list_widget)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.remove_button = QPushButton("🗑️ Remove")
        self.remove_button.clicked.connect(self.remove_selected)
        self.remove_button.setEnabled(False)
        button_layout.addWidget(self.remove_button)
        
        self.clear_button = QPushButton("🧹 Clear All")
        self.clear_button.clicked.connect(self.clear_all)
        button_layout.addWidget(self.clear_button)
        
        layout.addLayout(button_layout)
        
        # Connect signals
        self.list_widget.itemSelectionChanged.connect(self._on_selection_changed)
        
    def set_playlist(self, file_paths, current_index=-1):
        """
        Set danh sách file
        
        Args:
            file_paths: List các file path
            current_index: Index file đang phát
        """
        self.list_widget.clear()
        self.current_index = current_index
        
        for i, file_path in enumerate(file_paths):
            item = QListWidgetItem(self._format_filename(file_path))
            item.setData(Qt.ItemDataRole.UserRole, file_path)
            
            # Highlight file đang phát
            if i == current_index:
                font = item.font()
                font.setBold(True)
                item.setFont(font)
                item.setForeground(Qt.GlobalColor.blue)
                
            self.list_widget.addItem(item)
            
        self.count_label.setText(f"{len(file_paths)} files")
        
    def update_current_index(self, index):
        """
        Cập nhật file đang phát
        
        Args:
            index: Index mới
        """
        # Reset old item
        if 0 <= self.current_index < self.list_widget.count():
            old_item = self.list_widget.item(self.current_index)
            font = old_item.font()
            font.setBold(False)
            old_item.setFont(font)
            old_item.setForeground(Qt.GlobalColor.black)
            
        # Highlight new item
        self.current_index = index
        if 0 <= index < self.list_widget.count():
            new_item = self.list_widget.item(index)
            font = new_item.font()
            font.setBold(True)
            new_item.setFont(font)
            new_item.setForeground(Qt.GlobalColor.blue)
            
    def get_selected_file(self):
        """Lấy file đang được chọn"""
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            return selected_items[0].data(Qt.ItemDataRole.UserRole)
        return None
        
    def get_selected_index(self):
        """Lấy index của file đang được chọn"""
        return self.list_widget.currentRow()
        
    @Slot()
    def remove_selected(self):
        """Xóa file đã chọn"""
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            self.list_widget.takeItem(current_row)
            self.count_label.setText(f"{self.list_widget.count()} files")
            
    @Slot()
    def clear_all(self):
        """Xóa tất cả"""
        self.list_widget.clear()
        self.count_label.setText("0 files")
        
    @Slot()
    def _on_selection_changed(self):
        """Khi selection thay đổi"""
        has_selection = len(self.list_widget.selectedItems()) > 0
        self.remove_button.setEnabled(has_selection)
        
    @Slot(QListWidgetItem)
    def _on_item_double_clicked(self, item):
        """Khi double-click item"""
        file_path = item.data(Qt.ItemDataRole.UserRole)
        if file_path:
            self.file_selected.emit(file_path)
            
    @Slot(object)
    def _show_context_menu(self, pos):
        """Hiển thị context menu"""
        item = self.list_widget.itemAt(pos)
        if not item:
            return
            
        menu = QMenu(self)
        
        play_action = QAction("▶️ Play", self)
        play_action.triggered.connect(lambda: self._on_item_double_clicked(item))
        menu.addAction(play_action)
        
        menu.addSeparator()
        
        remove_action = QAction("🗑️ Remove", self)
        remove_action.triggered.connect(self.remove_selected)
        menu.addAction(remove_action)
        
        menu.exec(self.list_widget.mapToGlobal(pos))
        
    def _format_filename(self, file_path):
        """Format tên file để hiển thị"""
        return os.path.basename(file_path)
