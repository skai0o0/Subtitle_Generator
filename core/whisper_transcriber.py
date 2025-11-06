"""
Whisper Transcriber - Tích hợp Whisper AI để transcribe audio
"""
import whisper
import os
import tempfile
import subprocess
from PySide6.QtCore import QObject, Signal, QThread
import torch
import gc


class TranscriptionWorker(QThread):
    """Worker thread for transcription to avoid blocking UI"""
    
    # Signals
    progress = Signal(str)  # Progress message
    finished = Signal(list)  # List of subtitle segments
    error = Signal(str)     # Error message
    
    def __init__(self, audio_path, model_name="base", task="transcribe", language=None):
        super().__init__()
        self.audio_path = audio_path
        self.model_name = model_name
        self.task = task  # "transcribe" or "translate"
        self.language = language  # None for auto-detect
        
    def run(self):
        """Run transcription in background thread"""
        try:
            self.progress.emit(f"Loading Whisper model '{self.model_name}'...")
            
            # Load Whisper model - prioritize CUDA/GPU
            if torch.cuda.is_available():
                device = "cuda"
                gpu_name = torch.cuda.get_device_name(0)
                self.progress.emit(f"🎮 Using GPU: {gpu_name}")
                self.progress.emit(f"⚡ CUDA Version: {torch.version.cuda}")
            else:
                device = "cpu"
                self.progress.emit(f"💻 Using CPU (No GPU detected)")
                self.progress.emit(f"⚠️  Transcription will be slower without GPU")
            
            model = whisper.load_model(self.model_name, device=device)
            
            # Transcribe with GPU acceleration
            if device == "cuda":
                if self.task == "translate":
                    self.progress.emit("🚀 Translating to English with GPU acceleration...")
                else:
                    self.progress.emit("🚀 Transcribing with GPU acceleration...")
                self.progress.emit("💡 This should be much faster than CPU!")
            else:
                if self.task == "translate":
                    self.progress.emit("⏳ Translating to English with CPU... Please be patient.")
                else:
                    self.progress.emit("⏳ Transcribing with CPU... Please be patient.")
            
            # Prepare transcription parameters
            transcribe_params = {
                'audio': self.audio_path,
                'task': self.task,
                'verbose': False,
                'fp16': (device == "cuda")  # Use FP16 on GPU for faster processing
            }
            
            # Add language parameter only if specified and task is transcribe
            # For translate task, Whisper auto-detects source language
            if self.language and self.task == "transcribe":
                transcribe_params['language'] = self.language
                self.progress.emit(f"🌐 Language: {self.language}")
            elif self.task == "translate":
                self.progress.emit("🌐 Auto-detecting source language and translating to English...")
            
            # Transcribe/Translate
            result = model.transcribe(**transcribe_params)
            
            # ========== EJECT MODEL FROM VRAM ==========
            # Free GPU memory for next model (e.g., NLLB-200)
            self.progress.emit("🧹 Unloading Whisper model from VRAM...")
            del model
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                torch.cuda.synchronize()
            gc.collect()
            self.progress.emit("✅ VRAM cleared - ready for translation models!")
            # ==========================================
            
            # Convert to subtitle format
            subtitles = []
            for segment in result['segments']:
                subtitle = {
                    'start': int(segment['start'] * 1000),  # Convert to ms
                    'end': int(segment['end'] * 1000),      # Convert to ms
                    'text': segment['text'].strip()
                }
                subtitles.append(subtitle)
            
            # Show completion message based on task
            if self.task == "translate":
                self.progress.emit(f"✅ Translation complete! Found {len(subtitles)} segments in English.")
                if 'language' in result:
                    detected_lang = result['language']
                    self.progress.emit(f"🌐 Detected source language: {detected_lang}")
            else:
                self.progress.emit(f"✅ Transcription complete! Found {len(subtitles)} segments.")
                
            self.finished.emit(subtitles)
            
        except Exception as e:
            self.error.emit(f"Transcription error: {str(e)}")


class WhisperTranscriber(QObject):
    """Whisper AI transcriber manager"""
    
    # Signals
    progress = Signal(str)
    finished = Signal(list)
    error = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.worker = None
        self.temp_audio_file = None
        
    def transcribe_video(self, video_path, model_name="base", task="transcribe", language=None):
        """
        Transcribe or translate video file
        
        Args:
            video_path: Path to video/audio file
            model_name: Whisper model size (tiny, base, small, medium, large)
            task: "transcribe" (original language) or "translate" (to English)
            language: Language code for transcription (e.g., "vi", "en", "ja")
                     None for auto-detection. Only used when task="transcribe"
        """
        if self.worker and self.worker.isRunning():
            self.error.emit("Transcription already in progress!")
            return
            
        # Extract audio from video first
        if task == "translate":
            self.progress.emit("📤 Extracting audio for translation...")
        else:
            self.progress.emit("📤 Extracting audio for transcription...")
        audio_path = self._extract_audio(video_path)
        
        if not audio_path:
            self.error.emit("Failed to extract audio from video!")
            return
            
        # Start transcription in worker thread
        self.worker = TranscriptionWorker(audio_path, model_name, task=task, language=language)
        self.worker.progress.connect(self.progress)
        self.worker.finished.connect(self._on_finished)
        self.worker.error.connect(self.error)
        self.worker.start()
        
    def _extract_audio(self, video_path):
        """Extract audio from video using FFmpeg"""
        try:
            # Create temp audio file
            temp_dir = tempfile.gettempdir()
            audio_filename = os.path.splitext(os.path.basename(video_path))[0] + "_audio.wav"
            audio_path = os.path.join(temp_dir, audio_filename)
            
            # Use FFmpeg to extract audio
            # -vn: no video, -acodec pcm_s16le: PCM audio, -ar 16000: 16kHz sample rate
            cmd = [
                'ffmpeg',
                '-i', video_path,
                '-vn',  # No video
                '-acodec', 'pcm_s16le',  # PCM audio
                '-ar', '16000',  # 16kHz (Whisper's preferred rate)
                '-ac', '1',  # Mono
                '-y',  # Overwrite
                audio_path
            ]
            
            # Run FFmpeg
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
            
            if result.returncode == 0 and os.path.exists(audio_path):
                self.temp_audio_file = audio_path
                return audio_path
            else:
                return None
                
        except Exception as e:
            self.error.emit(f"Audio extraction error: {str(e)}")
            return None
            
    def _on_finished(self, subtitles):
        """Clean up and emit finished signal"""
        # Clean up temp audio file
        if self.temp_audio_file and os.path.exists(self.temp_audio_file):
            try:
                os.remove(self.temp_audio_file)
            except:
                pass
                
        self.finished.emit(subtitles)
        
    def stop(self):
        """Stop transcription"""
        if self.worker and self.worker.isRunning():
            self.worker.terminate()
            self.worker.wait()
