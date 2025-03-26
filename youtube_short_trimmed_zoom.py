from moviepy.editor import VideoFileClip

# Load the video
clip = VideoFileClip("trimmed_video.mp4")

# Original video size
w, h = clip.size

# Final Shorts video dimensions
target_w = 720
target_h = 1280

# --- 🔧 Adjustable Parameters ---
zoom = 0.85            # 1.0 = exact fit, >1 = zoom out, <1 = zoom in
x_shift = 0.45        # Horizontal focus: 0.5 = center, <0.5 = shift left, >0.5 = shift right
y_shift = 0.35        # Vertical focus: 0.5 = center, <0.5 = up, >0.5 = down
# --------------------------------

# Calculate the crop size based on zoom
crop_width = target_w * zoom
crop_height = target_h * zoom

# Calculate crop center
x_center = w * x_shift
y_center = h * y_shift

# Crop and resize
cropped_clip = clip.crop(
    x_center=x_center,
    y_center=y_center,
    width=crop_width,
    height=crop_height
).resize((target_w, target_h))

# Export video
cropped_clip.write_videofile("youtube_shorts_batsman_focus.mp4", fps=30)
