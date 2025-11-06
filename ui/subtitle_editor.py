"""
Subtitle Editor Widget - Chỉnh sửa subtitle
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLabel, QHeaderView, QMessageBox, QTimeEdit, QTextEdit,
    QDialog, QDialogButtonBox
)
from PySide6.QtCore import Qt, QTime, Signal, Slot
from PySide6.QtGui import QColor


class SubtitleEditDialog(QDialog):
    """Dialog để edit một subtitle entry"""
    
    def __init__(self, subtitle_data, parent=None):
        super().__init__(parent)
        self.subtitle_data = subtitle_data.copy()
        self.setWindowTitle("Edit Subtitle")
        self.setModal(True)
        self.resize(500, 300)
        
        self._create_ui()
        self._load_data()
        
    def _create_ui(self):
        """Tạo UI"""
        layout = QVBoxLayout(self)
        
        # Start time
        start_layout = QHBoxLayout()
        start_layout.addWidget(QLabel("Start Time:"))
        self.start_time_edit = QTimeEdit()
        self.start_time_edit.setDisplayFormat("HH:mm:ss.zzz")
        start_layout.addWidget(self.start_time_edit)
        layout.addLayout(start_layout)
        
        # End time
        end_layout = QHBoxLayout()
        end_layout.addWidget(QLabel("End Time:"))
        self.end_time_edit = QTimeEdit()
        self.end_time_edit.setDisplayFormat("HH:mm:ss.zzz")
        end_layout.addWidget(self.end_time_edit)
        layout.addLayout(end_layout)
        
        # Text
        layout.addWidget(QLabel("Subtitle Text:"))
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Enter subtitle text...")
        layout.addWidget(self.text_edit)
        
        # Buttons
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
    def _load_data(self):
        """Load data vào form"""
        # Convert ms to QTime
        start_ms = self.subtitle_data['start']
        end_ms = self.subtitle_data['end']
        
        start_time = QTime(0, 0, 0, 0).addMSecs(start_ms)
        end_time = QTime(0, 0, 0, 0).addMSecs(end_ms)
        
        self.start_time_edit.setTime(start_time)
        self.end_time_edit.setTime(end_time)
        self.text_edit.setPlainText(self.subtitle_data['text'])
        
    def get_data(self):
        """Lấy data đã edit"""
        # Convert QTime to ms
        start_time = self.start_time_edit.time()
        end_time = self.end_time_edit.time()
        
        start_ms = (start_time.hour() * 3600000 + 
                   start_time.minute() * 60000 + 
                   start_time.second() * 1000 + 
                   start_time.msec())
        
        end_ms = (end_time.hour() * 3600000 + 
                 end_time.minute() * 60000 + 
                 end_time.second() * 1000 + 
                 end_time.msec())
        
        return {
            'start': start_ms,
            'end': end_ms,
            'text': self.text_edit.toPlainText()
        }


class SubtitleEditorWidget(QWidget):
    """Widget để edit danh sách subtitle"""
    
    # Signal khi subtitle được update
    subtitles_changed = Signal(list)
    subtitle_selected = Signal(int)  # Emit position in ms khi select subtitle
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.subtitles = []
        self._create_ui()
        
    def _create_ui(self):
        """Tạo UI"""
        layout = QVBoxLayout(self)
        
        # Header
        header_layout = QHBoxLayout()
        header_label = QLabel("📝 Subtitle Editor")
        header_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        header_layout.addWidget(header_label)
        
        self.subtitle_count_label = QLabel("0 subtitles")
        self.subtitle_count_label.setStyleSheet("color: #666;")
        header_layout.addWidget(self.subtitle_count_label)
        header_layout.addStretch()
        layout.addLayout(header_layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Start", "End", "Text"])
        
        # Set column widths
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.itemDoubleClicked.connect(self.edit_subtitle)
        self.table.itemSelectionChanged.connect(self._on_selection_changed)
        
        layout.addWidget(self.table)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.add_button = QPushButton("➕ Add")
        self.add_button.clicked.connect(self.add_subtitle)
        button_layout.addWidget(self.add_button)
        
        self.edit_button = QPushButton("✏️ Edit")
        self.edit_button.clicked.connect(self.edit_selected_subtitle)
        self.edit_button.setEnabled(False)
        button_layout.addWidget(self.edit_button)
        
        self.delete_button = QPushButton("🗑️ Delete")
        self.delete_button.clicked.connect(self.delete_selected_subtitle)
        self.delete_button.setEnabled(False)
        button_layout.addWidget(self.delete_button)
        
        button_layout.addStretch()
        
        self.clear_button = QPushButton("🧹 Clear All")
        self.clear_button.clicked.connect(self.clear_all)
        button_layout.addWidget(self.clear_button)
        
        layout.addLayout(button_layout)
        
    def set_subtitles(self, subtitles):
        """Set danh sách subtitle"""
        self.subtitles = subtitles.copy()
        self._refresh_table()
        
    def get_subtitles(self):
        """Lấy danh sách subtitle"""
        return self.subtitles.copy()
        
    def _refresh_table(self):
        """Refresh table display"""
        self.table.setRowCount(len(self.subtitles))
        
        for i, subtitle in enumerate(self.subtitles):
            # Start time
            start_time = self._format_time(subtitle['start'])
            start_item = QTableWidgetItem(start_time)
            start_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 0, start_item)
            
            # End time
            end_time = self._format_time(subtitle['end'])
            end_item = QTableWidgetItem(end_time)
            end_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 1, end_item)
            
            # Text
            text = subtitle['text'].replace('\n', ' ')
            if len(text) > 100:
                text = text[:97] + "..."
            text_item = QTableWidgetItem(text)
            self.table.setItem(i, 2, text_item)
            
        # Update count
        self.subtitle_count_label.setText(f"{len(self.subtitles)} subtitles")
        
    def _format_time(self, ms):
        """Format milliseconds to HH:MM:SS,mmm"""
        seconds = ms // 1000
        milliseconds = ms % 1000
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
        
    @Slot()
    def add_subtitle(self):
        """Thêm subtitle mới"""
        # Create empty subtitle
        new_subtitle = {
            'start': 0,
            'end': 1000,
            'text': "New subtitle"
        }
        
        dialog = SubtitleEditDialog(new_subtitle, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            self.subtitles.append(data)
            self.subtitles.sort(key=lambda x: x['start'])  # Sort by start time
            self._refresh_table()
            self.subtitles_changed.emit(self.subtitles)
            
    @Slot()
    def edit_subtitle(self, item):
        """Edit subtitle khi double-click"""
        row = item.row()
        if 0 <= row < len(self.subtitles):
            subtitle = self.subtitles[row]
            dialog = SubtitleEditDialog(subtitle, self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                data = dialog.get_data()
                self.subtitles[row] = data
                self.subtitles.sort(key=lambda x: x['start'])  # Resort
                self._refresh_table()
                self.subtitles_changed.emit(self.subtitles)
                
    @Slot()
    def edit_selected_subtitle(self):
        """Edit subtitle đã chọn"""
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            row = selected_rows[0].row()
            item = self.table.item(row, 0)
            self.edit_subtitle(item)
            
    @Slot()
    def delete_selected_subtitle(self):
        """Xóa subtitle đã chọn"""
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            row = selected_rows[0].row()
            
            reply = QMessageBox.question(
                self,
                "Delete Subtitle",
                f"Are you sure you want to delete subtitle #{row + 1}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                del self.subtitles[row]
                self._refresh_table()
                self.subtitles_changed.emit(self.subtitles)
                
    @Slot()
    def clear_all(self):
        """Xóa tất cả subtitle"""
        if not self.subtitles:
            return
            
        reply = QMessageBox.question(
            self,
            "Clear All Subtitles",
            f"Are you sure you want to delete all {len(self.subtitles)} subtitles?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.subtitles = []
            self._refresh_table()
            self.subtitles_changed.emit(self.subtitles)
            
    @Slot()
    def _on_selection_changed(self):
        """Khi selection thay đổi"""
        has_selection = len(self.table.selectionModel().selectedRows()) > 0
        self.edit_button.setEnabled(has_selection)
        self.delete_button.setEnabled(has_selection)
        
        # Emit signal để seek video
        if has_selection:
            row = self.table.selectionModel().selectedRows()[0].row()
            if 0 <= row < len(self.subtitles):
                position = self.subtitles[row]['start']
                self.subtitle_selected.emit(position)
                
    def highlight_current_subtitle(self, position_ms):
        """Highlight subtitle đang phát tại vị trí position_ms"""
        # Tìm subtitle tương ứng với vị trí hiện tại
        current_row = -1
        for i, subtitle in enumerate(self.subtitles):
            if subtitle['start'] <= position_ms <= subtitle['end']:
                current_row = i
                break
        
        # Highlight row
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                item = self.table.item(i, j)
                if item:
                    if i == current_row:
                        # Highlight với màu vàng/xanh
                        item.setBackground(QColor(255, 235, 59, 100))  # Vàng nhạt
                        font = item.font()
                        font.setBold(True)
                        item.setFont(font)
                    else:
                        # Reset về màu bình thường
                        item.setBackground(QColor(255, 255, 255))
                        font = item.font()
                        font.setBold(False)
                        item.setFont(font)
