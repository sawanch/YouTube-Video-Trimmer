from moviepy.video.io.VideoFileClip import VideoFileClip

# Path to the downloaded video
video_path = "/Users/sawan/Documents/1-Coding-Practise-RW/Video-Trimming-Practise/YouTube-Video-Trimmer/downloaded_video.mp4"

# Convert times to seconds
start_time = 12 * 60 + 42  # 44 minutes and 40 seconds
end_time = 12 * 60 + 53    # 45 minutes and 35 seconds

# Load the video and trim
try:
    clip = VideoFileClip(video_path)

    # Manually create a subclip if the method name has changed
    if hasattr(clip, "subclip"):
        trimmed_clip = clip.subclip(start_time, end_time)
    elif hasattr(clip, "subclipped"):  # In case of renamed method
        trimmed_clip = clip.subclipped(start_time, end_time)
    else:
        raise AttributeError("The 'subclip' method is missing in this MoviePy version.")

    # Save the trimmed video
    output_path = "/Users/sawan/Documents/1-Coding-Practise-RW/Video-Trimming-Practise/YouTube-Video-Trimmer/trimmed_video.mp4"
    trimmed_clip.write_videofile(output_path, codec="libx264")

    print(f"Trimmed video saved to {output_path}")
except Exception as e:
    print(f"An error occurred: {e}")
