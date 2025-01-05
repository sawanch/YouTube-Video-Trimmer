2️⃣ Install Python
🐍 Python is necessary to run the script:

bash
Copy code
brew install python
3️⃣ Install yt-dlp (YouTube Downloader)
📥 Install yt-dlp to download YouTube videos:

bash
Copy code
brew install yt-dlp
4️⃣ Install ffmpeg (for video processing)
🎞️ Install ffmpeg as it’s required by MoviePy:

bash
Copy code
brew install ffmpeg
5️⃣ Install Python Dependencies
📦 Install Python libraries from the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
🛠️ Usage
1️⃣ Download a YouTube Video
Use the following command to download a YouTube video in the highest quality. Replace the URL with the video you want to download:

bash
Copy code
yt-dlp -o "downloaded_video.mp4" "https://www.youtube.com/watch?v=ZL14jkX39G0"
-o: Specifies the output file name and format.
2️⃣ Trim the Video
Open the trim_video.py file.

Update the following:

video_path: Path to the downloaded video.
start_time and end_time: Specify the start and end times in seconds or as MM:SS format.
output_path: Path where the trimmed video will be saved.
Run the script:

bash
Copy code
python trim_video.py
🎯 Example
Here’s an example to demonstrate the process:

Input:
Video Path: /Users/sawan/Desktop/cricket-video/downloaded_video.mp4
Start Time: 44:40 (44 minutes and 40 seconds)
End Time: 45:35 (45 minutes and 35 seconds)
Output Path: /Users/sawan/Desktop/cricket-video/trimmed_video.mp4
Steps:
Download the video:

bash
Copy code
yt-dlp -o "downloaded_video.mp4" "https://www.youtube.com/watch?v=ZL14jkX39G0"
Set the video_path, start_time, end_time, and output_path in trim_video.py.

Run the script:

bash
Copy code
python trim_video.py
Output:
A trimmed video file saved at /Users/sawan/Desktop/cricket-video/trimmed_video.mp4.
📌 Notes
💡 ffmpeg is mandatory: Ensure it is installed correctly to avoid processing errors.
🖥️ File Paths: Double-check all file paths in the script to ensure accuracy.
🕒 Start and End Times: Use a consistent time format (either in seconds or MM:SS).
🛑 Error Handling: The script includes basic error handling; check logs for details if something goes wrong.
🛠️ Tested on macOS: The setup is designed for macOS but can work on other OSes with minor changes.
