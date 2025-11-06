"""
NLLB-200 Translator - Dịch phụ đề sang 200+ ngôn ngữ
Sử dụng model facebook/nllb-200 từ Hugging Face (Meta AI)
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from PySide6.QtCore import QObject, Signal, QThread
import torch
import gc
import re
from typing import List, Dict


# Language code mapping for NLLB-200
# Format: Display Name -> NLLB code
NLLB_LANGUAGES = {
    # Top languages (commonly used)
    "Vietnamese (Tiếng Việt)": "vie_Latn",
    "English": "eng_Latn",
    "Chinese Simplified (简体中文)": "zho_Hans",
    "Chinese Traditional (繁體中文)": "zho_Hant",
    "Japanese (日本語)": "jpn_Jpan",
    "Korean (한국어)": "kor_Hang",
    "Thai (ไทย)": "tha_Thai",
    "Indonesian (Bahasa Indonesia)": "ind_Latn",
    "French (Français)": "fra_Latn",
    "German (Deutsch)": "deu_Latn",
    "Spanish (Español)": "spa_Latn",
    "Portuguese (Português)": "por_Latn",
    "Russian (Русский)": "rus_Cyrl",
    "Arabic (العربية)": "arb_Arab",
    "Hindi (हिन्दी)": "hin_Deva",
    
    # Additional Asian languages
    "Khmer (ភាសាខ្មែរ)": "khm_Khmr",
    "Lao (ລາວ)": "lao_Laoo",
    "Burmese (မြန်မာ)": "mya_Mymr",
    "Tagalog (Filipino)": "tgl_Latn",
    "Malay (Bahasa Melayu)": "zsm_Latn",
    
    # European languages
    "Italian (Italiano)": "ita_Latn",
    "Dutch (Nederlands)": "nld_Latn",
    "Polish (Polski)": "pol_Latn",
    "Turkish (Türkçe)": "tur_Latn",
    "Swedish (Svenska)": "swe_Latn",
    "Danish (Dansk)": "dan_Latn",
    "Norwegian (Norsk)": "nob_Latn",
    "Finnish (Suomi)": "fin_Latn",
    "Czech (Čeština)": "ces_Latn",
    "Greek (Ελληνικά)": "ell_Grek",
    "Hebrew (עברית)": "heb_Hebr",
    "Ukrainian (Українська)": "ukr_Cyrl",
    
    # More languages (can add up to 200+)
}


# Model options with sizes
NLLB_MODELS = {
    "NLLB-200 Distilled 600M (Fast, Good Quality)": "facebook/nllb-200-distilled-600M",
    "NLLB-200 Distilled 1.3B (Balanced)": "facebook/nllb-200-distilled-1.3B",
    "NLLB-200 1.3B (Better Quality)": "facebook/nllb-200-1.3B",
    "NLLB-200 3.3B (Best Quality, Slow)": "facebook/nllb-200-3.3B",
}


class NLLBTranslationWorker(QThread):
    """Worker thread for NLLB translation"""
    
    # Signals
    progress = Signal(str, int)  # Progress message, percentage
    finished = Signal(list)      # List of translated subtitle segments
    error = Signal(str)          # Error message
    
    def __init__(self, subtitles: List[Dict], model_name: str, 
                 source_lang: str = "eng_Latn", target_lang: str = "vie_Latn"):
        super().__init__()
        self.subtitles = subtitles
        self.model_name = model_name
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.model = None
        self.tokenizer = None
        
    def run(self):
        """Run translation in background thread"""
        try:
            self.progress.emit(f"Loading {self.model_name.split('/')[-1]}...", 0)
            
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
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            
            # Set source and target languages for NLLB tokenizer
            self.tokenizer.src_lang = self.source_lang
            self.tokenizer.tgt_lang = self.target_lang
            
            self.progress.emit("Loading translation model...", 20)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            
            # Move model to device
            if device == "cuda":
                self.model.cuda()
                self.progress.emit("⚡ Model loaded on GPU", 30)
            else:
                self.progress.emit("📦 Model loaded on CPU", 30)
            
            # Get language names for display
            source_lang_name = [k for k, v in NLLB_LANGUAGES.items() if v == self.source_lang]
            target_lang_name = [k for k, v in NLLB_LANGUAGES.items() if v == self.target_lang]
            
            source_display = source_lang_name[0] if source_lang_name else self.source_lang
            target_display = target_lang_name[0] if target_lang_name else self.target_lang
            
            # Translate subtitles with sliding window context
            translated_subtitles = []
            total_subtitles = len(self.subtitles)
            
            self.progress.emit(
                f"🔄 Translating {total_subtitles} segments: {source_display} → {target_display}",
                35
            )
            
            # Process each subtitle with context from previous sentence
            for idx in range(total_subtitles):
                current_sub = self.subtitles[idx]
                
                # Build context: include previous sentence for better translation
                context_window = []
                
                # Add previous sentence (if exists)
                if idx > 0:
                    prev_sub = self.subtitles[idx - 1]
                    context_window.append(prev_sub['text'])
                
                # Add current sentence
                context_window.append(current_sub['text'])
                
                # Combine with space between sentences
                full_text = " ".join(context_window)
                
                # Tokenize (source language already set in tokenizer.src_lang)
                inputs = self.tokenizer(
                    full_text,
                    return_tensors="pt",
                    truncation=True,
                    max_length=512
                )
                
                # Move to device
                if device == "cuda":
                    inputs = {k: v.cuda() for k, v in inputs.items()}
                
                # Get target language token ID for forced decoding
                target_lang_id = self.tokenizer.convert_tokens_to_ids(self.target_lang)
                
                # Generate translation with target language
                with torch.no_grad():
                    translated_tokens = self.model.generate(
                        **inputs,
                        forced_bos_token_id=target_lang_id,
                        max_length=512,
                        num_beams=5,
                        early_stopping=True,
                        no_repeat_ngram_size=3
                    )
                
                # Decode translation
                full_translation = self.tokenizer.batch_decode(
                    translated_tokens, 
                    skip_special_tokens=True
                )[0]
                
                # Clean up the translation
                full_translation = full_translation.strip()
                
                # Extract only the translation of current sentence
                # If we had context, take the last sentence
                if idx > 0 and len(context_window) > 1:
                    # Split by sentence endings
                    parts = re.split(r'([.!?…。！？]+\s*)', full_translation)
                    
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
                f"✅ Translation complete! {total_subtitles} segments translated to {target_display}",
                95
            )
            
            # ========== EJECT MODEL FROM VRAM ==========
            # Free GPU memory for next use
            self.progress.emit("🧹 Unloading NLLB model from VRAM...", 97)
            del self.model
            del self.tokenizer
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                torch.cuda.synchronize()
            gc.collect()
            self.progress.emit("✅ VRAM cleared!", 100)
            # ==========================================
            
            self.finished.emit(translated_subtitles)
            
        except Exception as e:
            # Clean up model even on error
            if self.model is not None:
                del self.model
            if self.tokenizer is not None:
                del self.tokenizer
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            gc.collect()
            self.error.emit(f"Translation error: {str(e)}")


class NLLBTranslator(QObject):
    """NLLB-200 translator manager"""
    
    # Signals
    progress = Signal(str, int)  # message, percentage
    finished = Signal(list)      # translated subtitles
    error = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.worker = None
        
    def translate_subtitles(self, subtitles: List[Dict], model_name: str,
                          source_lang: str = "eng_Latn", target_lang: str = "vie_Latn"):
        """
        Translate subtitles using NLLB-200
        
        Args:
            subtitles: List of subtitle dicts with 'start', 'end', 'text' keys
            model_name: NLLB model name (e.g., "facebook/nllb-200-distilled-600M")
            source_lang: Source language code (e.g., "eng_Latn")
            target_lang: Target language code (e.g., "vie_Latn")
        """
        if self.worker and self.worker.isRunning():
            self.error.emit("Translation already in progress!")
            return
        
        if not subtitles:
            self.error.emit("No subtitles to translate!")
            return
        
        # Start translation in worker thread
        self.worker = NLLBTranslationWorker(subtitles, model_name, source_lang, target_lang)
        self.worker.progress.connect(self.progress)
        self.worker.finished.connect(self.finished)
        self.worker.error.connect(self.error)
        self.worker.start()
        
    def stop(self):
        """Stop translation"""
        if self.worker and self.worker.isRunning():
            self.worker.terminate()
            self.worker.wait()
    
    @staticmethod
    def get_available_languages():
        """Get list of available languages"""
        return list(NLLB_LANGUAGES.keys())
    
    @staticmethod
    def get_language_code(language_name: str) -> str:
        """Get NLLB language code from display name"""
        return NLLB_LANGUAGES.get(language_name, "vie_Latn")
    
    @staticmethod
    def get_available_models():
        """Get list of available NLLB models"""
        return list(NLLB_MODELS.keys())
    
    @staticmethod
    def get_model_name(model_display_name: str) -> str:
        """Get actual model name from display name"""
        return NLLB_MODELS.get(model_display_name, "facebook/nllb-200-distilled-600M")
