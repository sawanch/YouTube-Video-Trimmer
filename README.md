```markdown
# YouTube Video Downloader and Trimmer

This project provides a Python script to download a YouTube video of the highest quality using `yt-dlp` and trim it to a specific timeframe using `MoviePy`. It is designed to work on macOS and assumes `brew` is available for managing packages.

---

## Features

- Download YouTube videos in the highest quality using `yt-dlp`.
- Trim the downloaded video to a specific start and end time using `MoviePy`.
- Save the trimmed video in the desired location.

---

## Requirements

Ensure the following are installed on your system:

- **Homebrew** (macOS package manager): [Install Homebrew](https://brew.sh/)
- **Python** (>= 3.7)
- **ffmpeg** (required by `MoviePy`)
- `yt-dlp` (YouTube downloader)
- `MoviePy` (for video trimming)

---

## Installation

Follow these steps to set up the project on your machine:

### Install Python using Homebrew:
```bash
brew install python
```

### Install ffmpeg:
```bash
brew install ffmpeg
```

### Install `yt-dlp`:
```bash
brew install yt-dlp
```

### Install the required Python package `MoviePy`:
```bash
pip install moviepy==1.0.3
```

---

## Usage

### Step 1: Download a YouTube Video

1. Open your terminal and navigate to the directory where you want to save the downloaded video.
2. Use the following command to download a YouTube video of the highest quality:
   ```bash
   yt-dlp -o "downloaded_video.mp4" "https://www.youtube.com/watch?v=ZL14jkX39G0"
   ```
   Replace `"https://www.youtube.com/watch?v=ZL14jkX39G0"` with the URL of the desired video.

### Step 2: Trim the Video

1. Update the `video_path`, `start_time`, and `end_time` variables in the `trim_video.py` script:
   ```python
   # Path to the downloaded video
   video_path = "/Users/sawan/Desktop/cricket-video/downloaded_video.mp4"

   # Start and end times (in seconds)
   start_time = 44 * 60 + 40  # 44 minutes and 40 seconds
   end_time = 45 * 60 + 35    # 45 minutes and 35 seconds
   ```

2. Run the trimming script:
   ```bash
   python trim_video.py
   ```

3. The trimmed video will be saved to the location specified by `output_path` in the script. Example:
   ```bash
   /Users/sawan/Desktop/cricket-video/trimmed_video.mp4
   ```

---

## Script Details

### `trim_video.py`

This script uses the `MoviePy` library to trim a video file between specified start and end times. It validates the presence of the `subclip` method in the installed version of `MoviePy` to ensure compatibility.

---

## Troubleshooting

### `yt-dlp` command not found
Ensure you have installed `yt-dlp` using Homebrew. Try running:
```bash
brew install yt-dlp
```

### Error in `MoviePy` script
Ensure `MoviePy` and `ffmpeg` are correctly installed:
```bash
pip install moviepy==1.0.3
brew install ffmpeg
```

### Permission Denied
Ensure the script has write permissions for the specified output directory.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contribution

Feel free to open an issue or submit a pull request for any bugs, features, or suggestions!

---

### Happy Coding! 🎥
```
