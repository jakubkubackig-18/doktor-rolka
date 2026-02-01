
import cv2
import os

videos = ['rolka1.mp4', 'rolka2.mp4', 'rolka3.mp4', 'rolka4.mp4']

for video in videos:
    if not os.path.exists(video):
        print(f"File {video} not found.")
        continue
        
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        print(f"Error opening video stream {video}")
        continue
    
    # Get total frame count
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Try to capture at 1 second mark (usually 30 or 60 frames in)
    frame_to_capture = int(fps) # 1 second in
    
    if frame_to_capture >= total_frames:
      frame_to_capture = 0 # Fallback to first frame if video is super short
      
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_to_capture)
    
    ret, frame = cap.read()
    if ret:
        output_filename = video.replace('.mp4', '.jpg')
        cv2.imwrite(output_filename, frame)
        print(f"Saved {output_filename}")
    else:
        print(f"Could not read frame for {video}")
        
    cap.release()
