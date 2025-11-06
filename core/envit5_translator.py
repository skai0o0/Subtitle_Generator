"""
EnViT5 Translator - Dịch phụ đề từ tiếng Anh sang tiếng Việt
Sử dụng model VietAI/envit5-base từ Hugging Face
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from PySide6.QtCore import QObject, Signal, QThread
import torch
import re
from typing import List, Dict


class TranslationWorker(QThread):
    """Worker thread for translation to avoid blocking UI"""
    
    # Signals
    progress = Signal(str, int)  # Progress message, percentage
    finished = Signal(list)      # List of translated subtitle segments
    error = Signal(str)          # Error message
    
    def __init__(self, subtitles: List[Dict], batch_size: int = 8):
        super().__init__()
        self.subtitles = subtitles
        self.batch_size = batch_size
        self.model = None
        self.tokenizer = None
        
    def run(self):
        """Run translation in background thread"""
        try:
            self.progress.emit("Loading EnViT5-base model...", 0)
            
            # Load model and tokenizer
            model_name = "VietAI/envit5-base"
            
            # Check if GPU is available
            if torch.cuda.is_available():
                device = "cuda"
                gpu_name = torch.cuda.get_device_name(0)
                self.progress.emit(f"🎮 Using GPU: {gpu_name}", 5)
            else:
                device = "cpu"
                self.progress.emit("💻 Using CPU (translation will be slower)", 5)
            
            # Load tokenizer and model
            self.progress.emit("Loading tokenizer...", 10)
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                use_fast=False  # Use slow tokenizer for better Vietnamese support
            )
            
            self.progress.emit("Loading translation model...", 20)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            
            # Move model to device
            if device == "cuda":
                self.model.cuda()
                self.progress.emit("⚡ Model loaded on GPU", 30)
            else:
                self.progress.emit("📦 Model loaded on CPU", 30)
            
            # Translate subtitles in batches with sliding window context
            translated_subtitles = []
            total_subtitles = len(self.subtitles)
            
            self.progress.emit(f"🔄 Translating {total_subtitles} subtitle segments with context...", 35)
            
            # Process each subtitle individually with context
            for idx in range(total_subtitles):
                current_sub = self.subtitles[idx]
                
                # Build context: include 1-2 previous sentences for better translation
                context_window = []
                
                # Add previous sentence (if exists)
                if idx > 0:
                    prev_sub = self.subtitles[idx - 1]
                    context_window.append(prev_sub['text'])
                
                # Add current sentence
                context_window.append(current_sub['text'])
                
                # Combine with space between sentences
                full_text = " ".join(context_window)
                
                # Add prefix for model
                input_text = f"en: {full_text}"
                
                # Tokenize
                inputs = self.tokenizer(
                    input_text,
                    return_tensors="pt",
                    truncation=True,
                    max_length=512
                )
                
                # Move to device
                if device == "cuda":
                    inputs = {k: v.cuda() for k, v in inputs.items()}
                
                # Generate translation
                with torch.no_grad():
                    outputs = self.model.generate(
                        inputs['input_ids'],
                        max_length=512,
                        min_length=1,
                        num_beams=5,
                        early_stopping=True,
                        no_repeat_ngram_size=3,
                        repetition_penalty=1.2,
                        length_penalty=1.0,
                        do_sample=False  # Disable sampling for more stable output
                    )
                
                # Decode translation with proper handling
                full_translation = self.tokenizer.decode(
                    outputs[0], 
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=True
                )
                
                # Clean up the translation
                full_translation = full_translation.strip()
                
                # Extract only the translation of current sentence
                # If we had context, the translation will have multiple sentences
                # We take the last sentence as it corresponds to current_sub
                if idx > 0 and len(context_window) > 1:
                    # Try to split by Vietnamese sentence endings
                    # Common patterns: . ! ? ... 
                    # Split by sentence endings but keep the delimiter
                    parts = re.split(r'([.!?…]+\s*)', full_translation)
                    
                    # Reconstruct sentences
                    sentences = []
                    for i in range(0, len(parts)-1, 2):
                        sentence = parts[i] + (parts[i+1] if i+1 < len(parts) else '')
                        if sentence.strip():
                            sentences.append(sentence.strip())
                    if len(parts) % 2 == 1 and parts[-1].strip():
                        sentences.append(parts[-1].strip())
                    
                    # Take the last sentence (corresponds to current subtitle)
                    translation = sentences[-1] if sentences else full_translation
                else:
                    translation = full_translation
                
                # Additional cleanup: remove weird characters
                translation = translation.replace('\u200b', '')  # Zero-width space
                translation = translation.replace('\ufeff', '')  # BOM
                translation = ' '.join(translation.split())  # Normalize spaces
                
                # Create translated subtitle segment
                translated_sub = {
                    'start': current_sub['start'],
                    'end': current_sub['end'],
                    'text': translation.strip()
                }
                translated_subtitles.append(translated_sub)
                
                # Update progress
                progress_pct = 35 + int((idx + 1) / total_subtitles * 60)
                self.progress.emit(
                    f"Translated {idx + 1}/{total_subtitles} segments",
                    progress_pct
                )
            
            self.progress.emit(
                f"✅ Translation complete! {total_subtitles} segments translated to Vietnamese",
                100
            )
            self.finished.emit(translated_subtitles)
            
        except Exception as e:
            self.error.emit(f"Translation error: {str(e)}")


class EnViT5Translator(QObject):
    """EnViT5 translator manager"""
    
    # Signals
    progress = Signal(str, int)  # message, percentage
    finished = Signal(list)      # translated subtitles
    error = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.worker = None
        
    def translate_subtitles(self, subtitles: List[Dict], batch_size: int = 8):
        """
        Translate English subtitles to Vietnamese
        
        Args:
            subtitles: List of subtitle dicts with 'start', 'end', 'text' keys
            batch_size: Number of subtitles to translate at once (default: 8)
        """
        if self.worker and self.worker.isRunning():
            self.error.emit("Translation already in progress!")
            return
        
        if not subtitles:
            self.error.emit("No subtitles to translate!")
            return
        
        # Start translation in worker thread
        self.worker = TranslationWorker(subtitles, batch_size)
        self.worker.progress.connect(self.progress)
        self.worker.finished.connect(self.finished)
        self.worker.error.connect(self.error)
        self.worker.start()
        
    def stop(self):
        """Stop translation"""
        if self.worker and self.worker.isRunning():
            self.worker.terminate()
            self.worker.wait()
