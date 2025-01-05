
```markdown
# 🎥 YouTube-Video-Trimmer 🚀

A simple and efficient script to **download YouTube videos** and **trim them** to specific time ranges. This tool leverages the power of `yt-dlp` for video downloading and `MoviePy` for seamless video editing.

---

## ✨ Features
- 📥 **Download YouTube videos** in the highest quality using `yt-dlp`.
- ✂️ **Trim videos** to specified start and end times with precision.
- 🖥️ **Mac-compatible** (also works on other systems with minor adjustments).

---

## 🛠️ Prerequisites
Ensure you have the following installed on your system:
- 🍎 macOS (tested; other OSes may require adjustments)
- 🧰 [Homebrew](https://brew.sh/) package manager installed

---

## 📦 Installation
1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/yt-video-trimmer.git
   cd yt-video-trimmer
   ```

2. **Install dependencies**:
   ```bash
   brew install python
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

### 1️⃣ Download a YouTube Video
Run the following command in your terminal, replacing the URL with the video you want to download:
```bash
yt-dlp -o "downloaded_video.mp4" "https://www.youtube.com/watch?v=ZL14jkX39G0"
```

### 2️⃣ Trim the Video
Update the `trim_video.py` file with:
- The path to your downloaded video.
- Start and end times (in seconds or `MM:SS` format).

Then execute the script:
```bash
python trim_video.py
```

🎉 **Output:** A trimmed video file saved at the specified location.

---

## 📝 Example
- Input Video: `/Users/sawan/Desktop/cricket-video/downloaded_video.mp4`
- Trim Start: `44:40` (44 minutes and 40 seconds)
- Trim End: `45:35` (45 minutes and 35 seconds)
- Output Video: `/Users/sawan/Desktop/cricket-video/trimmed_video.mp4`

---

## 🔧 Notes
- Ensure `ffmpeg` is installed as it’s required by `MoviePy`.
- Double-check the paths and time ranges before running the script.
- If you encounter issues, refer to the logs printed by the script.


---

## 💡 Contributing
Contributions are welcome! Feel free to:
- 🌟 Fork the repository
- 🛠️ Submit pull requests with enhancements or bug fixes
- 📧 Share your feedback or ideas

---

## 🤝 Acknowledgments
- Special thanks to the developers of `yt-dlp`, `MoviePy`, and `ffmpeg` for their incredible tools.


### Highlights:
- Used colorful emojis to make the sections engaging.
- Structured the `README.md` for clarity and ease of use.
- Included example inputs and outputs for better user understanding.

Let me know if you want any further tweaks or additions! 😊
