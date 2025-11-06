"""
Subtitle Manager - Quản lý subtitle data và export
"""
import os
from datetime import timedelta


class SubtitleManager:
    """Manager for subtitle data and export"""
    
    def __init__(self):
        self.subtitles = []
        
    def set_subtitles(self, subtitles):
        """
        Set subtitle data
        
        Args:
            subtitles: List of dicts with 'start', 'end', 'text' keys (time in ms)
        """
        self.subtitles = subtitles
        
    def get_subtitles(self):
        """Get subtitle data"""
        return self.subtitles
        
    def get_subtitle_at_time(self, time_ms):
        """
        Get subtitle text at specific time
        
        Args:
            time_ms: Time in milliseconds
            
        Returns:
            Subtitle text or None
        """
        for subtitle in self.subtitles:
            if subtitle['start'] <= time_ms <= subtitle['end']:
                return subtitle['text']
        return None
        
    def export_srt(self, output_path):
        """
        Export subtitles to SRT format
        
        Args:
            output_path: Output file path
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                for i, subtitle in enumerate(self.subtitles, 1):
                    # Subtitle number
                    f.write(f"{i}\n")
                    
                    # Timestamp
                    start_time = self._format_srt_time(subtitle['start'])
                    end_time = self._format_srt_time(subtitle['end'])
                    f.write(f"{start_time} --> {end_time}\n")
                    
                    # Text
                    f.write(f"{subtitle['text']}\n\n")
                    
            return True
        except Exception as e:
            print(f"Error exporting SRT: {e}")
            return False
            
    def export_vtt(self, output_path):
        """
        Export subtitles to WebVTT format
        
        Args:
            output_path: Output file path
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                # WebVTT header
                f.write("WEBVTT\n\n")
                
                for i, subtitle in enumerate(self.subtitles, 1):
                    # Cue identifier (optional)
                    f.write(f"{i}\n")
                    
                    # Timestamp
                    start_time = self._format_vtt_time(subtitle['start'])
                    end_time = self._format_vtt_time(subtitle['end'])
                    f.write(f"{start_time} --> {end_time}\n")
                    
                    # Text
                    f.write(f"{subtitle['text']}\n\n")
                    
            return True
        except Exception as e:
            print(f"Error exporting VTT: {e}")
            return False
            
    def _format_srt_time(self, ms):
        """
        Format milliseconds to SRT time format (HH:MM:SS,mmm)
        
        Args:
            ms: Time in milliseconds
            
        Returns:
            Formatted time string
        """
        td = timedelta(milliseconds=ms)
        hours = td.seconds // 3600
        minutes = (td.seconds % 3600) // 60
        seconds = td.seconds % 60
        milliseconds = td.microseconds // 1000
        
        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
        
    def _format_vtt_time(self, ms):
        """
        Format milliseconds to WebVTT time format (HH:MM:SS.mmm)
        
        Args:
            ms: Time in milliseconds
            
        Returns:
            Formatted time string
        """
        td = timedelta(milliseconds=ms)
        hours = td.seconds // 3600
        minutes = (td.seconds % 3600) // 60
        seconds = td.seconds % 60
        milliseconds = td.microseconds // 1000
        
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        
    def import_srt(self, file_path):
        """
        Import subtitles from SRT file
        
        Args:
            file_path: SRT file path
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            subtitles = []
            blocks = content.strip().split('\n\n')
            
            for block in blocks:
                lines = block.strip().split('\n')
                if len(lines) >= 3:
                    # Parse timestamp line
                    timestamp_line = lines[1]
                    if '-->' in timestamp_line:
                        start_str, end_str = timestamp_line.split('-->')
                        start_ms = self._parse_srt_time(start_str.strip())
                        end_ms = self._parse_srt_time(end_str.strip())
                        
                        # Parse text (can be multiple lines)
                        text = '\n'.join(lines[2:])
                        
                        subtitles.append({
                            'start': start_ms,
                            'end': end_ms,
                            'text': text
                        })
                        
            self.subtitles = subtitles
            return True
            
        except Exception as e:
            print(f"Error importing SRT: {e}")
            return False
            
    def _parse_srt_time(self, time_str):
        """
        Parse SRT time string to milliseconds
        
        Args:
            time_str: Time string (HH:MM:SS,mmm)
            
        Returns:
            Time in milliseconds
        """
        # Format: HH:MM:SS,mmm
        time_str = time_str.replace(',', '.')
        parts = time_str.split(':')
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds_parts = parts[2].split('.')
        seconds = int(seconds_parts[0])
        milliseconds = int(seconds_parts[1]) if len(seconds_parts) > 1 else 0
        
        total_ms = (hours * 3600 + minutes * 60 + seconds) * 1000 + milliseconds
        return total_ms
