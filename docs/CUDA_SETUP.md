# 🎮 CUDA/GPU Setup Guide

## 🚀 GPU Acceleration cho Whisper AI

Dự án này được optimize để sử dụng **NVIDIA GPU** làm platform chính, CPU chỉ là fallback.

---

## ✅ Current Setup (Detected)

```
GPU: NVIDIA GeForce RTX 4070 SUPER
CUDA: 12.4
Driver: 581.57
GPU Memory: 12 GB
PyTorch: 2.6.0+cu124
Status: ✅ GPU Acceleration ENABLED
```

---

## 📊 Performance Comparison

| Model | CPU Time | GPU Time | Speedup |
|-------|----------|----------|---------|
| tiny | ~2 min | ~15 sec | **8x** |
| base | ~3 min | ~20 sec | **9x** |
| small | ~8 min | ~40 sec | **12x** |
| medium | ~20 min | ~90 sec | **13x** |
| large | ~40 min | ~3 min | **13x** |

*For 5-minute video*

---

## 🔧 Requirements

### Hardware:
- **NVIDIA GPU** với CUDA support (GTX 900 series trở lên)
- Minimum **4GB VRAM** (8GB+ recommended)
- Driver Version: 450+ (latest recommended)

### Software:
- **NVIDIA GPU Driver** (latest)
- **CUDA Toolkit** 11.8+ (included with PyTorch)
- **cuDNN** (included with PyTorch)

---

## 📦 Installation

### Step 1: Verify GPU
```powershell
# Check if NVIDIA GPU exists
nvidia-smi
```

### Step 2: Install Dependencies
```powershell
# Run setup (will auto-detect GPU)
.\setup.ps1

# Or manual:
.\.venv\Scripts\Activate.ps1

# Install base packages
pip install -r requirements-cuda.txt

# Install PyTorch with CUDA 12.4
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

### Step 3: Verify CUDA
```powershell
# Test CUDA availability
python -c "import torch; print('CUDA:', torch.cuda.is_available())"

# Or run full test
python test_setup.py
```

---

## 🎯 CUDA Versions

| CUDA Version | PyTorch Index URL |
|-------------|-------------------|
| **12.4** (Recommended) | `https://download.pytorch.org/whl/cu124` |
| 12.1 | `https://download.pytorch.org/whl/cu121` |
| 11.8 | `https://download.pytorch.org/whl/cu118` |

To change CUDA version:
```powershell
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url <URL>
```

---

## 🔍 Verify GPU Usage

### In App:
When you start transcription, you'll see:
```
🎮 Using GPU: NVIDIA GeForce RTX 4070 SUPER
⚡ CUDA Version: 12.4
🚀 Transcribing with GPU acceleration...
💡 This should be much faster than CPU!
```

### Monitor GPU:
```powershell
# Real-time GPU monitoring
nvidia-smi -l 1

# Watch GPU usage while transcribing
nvidia-smi dmon
```

---

## 🎓 Optimization Tips

### 1. **Choose Right Model**
- RTX 4070 (12GB) → Can handle **large** model
- RTX 3060 (8GB) → **medium** model comfortable
- GTX 1660 (6GB) → **small** model recommended

### 2. **FP16 Mode**
App automatically uses FP16 on GPU for **2x speed** with minimal quality loss.

### 3. **Batch Processing**
For multiple videos, GPU shines:
- CPU: Linear time increase
- GPU: Minimal overhead per video

### 4. **Free GPU Memory**
```powershell
# Close GPU-heavy apps before transcribing
# Check GPU usage:
nvidia-smi
```

---

## 🐛 Troubleshooting

### ❌ "CUDA not available"

**Check 1: GPU Driver**
```powershell
nvidia-smi
# Should show GPU info
```

**Check 2: PyTorch CUDA**
```powershell
python -c "import torch; print(torch.version.cuda)"
# Should show: 12.4 (not None)
```

**Check 3: Reinstall PyTorch**
```powershell
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

### ❌ "Out of memory"

**Solutions:**
1. Use smaller model (medium → small → base)
2. Close other GPU apps
3. Restart PC to clear GPU memory
4. Reduce video resolution before transcribing

**Check memory:**
```powershell
nvidia-smi
# Look at "Memory-Usage"
```

### ❌ Slower than expected

**Check:**
1. GPU utilization in `nvidia-smi` (should be 90-100%)
2. Other processes using GPU
3. Power mode (should be "Performance" not "Power Saver")
4. Thermal throttling (check temps in `nvidia-smi`)

---

## 📈 Expected Performance

### RTX 4070 SUPER (12GB):
- **tiny:** ~10-15 sec/min video (real-time 4-6x)
- **base:** ~15-20 sec/min video (real-time 3-4x)
- **small:** ~25-35 sec/min video (real-time 2x)
- **medium:** ~45-60 sec/min video (real-time 1x)
- **large:** ~90-120 sec/min video (real-time 0.5x)

### CPU Fallback (i7/Ryzen 7):
- **tiny:** ~2 min/min video
- **base:** ~3-4 min/min video
- **small:** ~8-10 min/min video
- **medium:** ~20-30 min/min video (not recommended)
- **large:** 40+ min/min video (very slow)

---

## 🎊 Benefits of GPU

✅ **10-15x faster** transcription
✅ Can use **larger models** (better accuracy)
✅ **Real-time** or faster processing
✅ **Smooth UI** (no freezing)
✅ Can process **multiple videos** efficiently

---

## 💡 Recommendations

| GPU VRAM | Recommended Model | Quality |
|----------|------------------|---------|
| 4GB | tiny, base | Good |
| 6GB | base, small | Better |
| 8GB | small, medium | Great |
| 10GB+ | medium, large | **Best** |

**For Your RTX 4070 (12GB):**
→ Use **large** model for best results!

---

## 🔄 Switching Between GPU/CPU

App automatically uses GPU if available. To force CPU:
```python
# Edit core/whisper_transcriber.py line 22:
device = "cpu"  # Force CPU
```

But why would you? GPU is way faster! 🚀

---

## 📚 Additional Resources

- [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit)
- [PyTorch CUDA Support](https://pytorch.org/get-started/locally/)
- [Whisper GPU Requirements](https://github.com/openai/whisper#setup)

---

**With GPU: Transcribe faster, work smarter! 🎮⚡**
