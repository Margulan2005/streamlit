import streamlit as st
import cv2
import tempfile
import numpy as np
from pathlib import Path
from yt_dlp import YoutubeDL
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import time

class Project2:
    def __init__(self):
        self.cap = None

    def app(self):
        st.title('Video Stream in Streamlit')

        source_option = st.selectbox(
            "Pick the source of the video stream",
            ("Mobile camera", "YouTube link", "Local drive", "Web-camera", "RTSP")
        )

        video_url = None
        img_file = None
        temp_file = None

        if source_option == "Mobile camera":
            img_file = st.camera_input("Take a photo")

        elif source_option == "YouTube link":
            youtube_url = st.text_input("Enter a YouTube link")
            if youtube_url:
                with st.spinner("Fetching video..."):
                    try:
                        ydl_opts = {"format": "best[ext=mp4]/best", "noplaylist": True}
                        with YoutubeDL(ydl_opts) as ydl:
                            info_dict = ydl.extract_info(youtube_url, download=False)
                            video_url = info_dict.get("url", None)
                    except Exception as e:
                        st.error(f"Error: {e}")

                if video_url:
                    st.video(video_url)

        elif source_option == "Local drive":
            video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
            if video_file:
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=Path(video_file.name).suffix)
                temp_file.write(video_file.read())
                video_url = temp_file.name
                st.video(video_url)

        elif source_option == "Web-camera":
            st.write("Launching webcam...")
            webrtc_streamer(key="webcam", mode=WebRtcMode.SENDRECV)

        elif source_option == "RTSP":
            rtsp_url = st.text_input("Enter an RTSP link")
            if rtsp_url:
                video_url = rtsp_url

        run_button = st.button("Run Stream")
        stop_button = st.button("Stop Stream", disabled=True)
        frame_place = st.empty()

        if source_option == "Mobile camera" and img_file is not None:
            file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
            frame = cv2.imdecode(file_bytes, 1)
            st.image(frame, channels="BGR")

        elif run_button and video_url and source_option in ["Local drive", "RTSP"]:
            self.cap = cv2.VideoCapture(video_url)
            if not self.cap.isOpened():
                st.error("Unable to open the video source.")
            else:
                st.write("Streaming started...")
                stop_button = st.button("Stop Stream", key="stop")
                while self.cap.isOpened():
                    ret, frame = self.cap.read()
                    if not ret:
                        st.error("Failed to retrieve frames. Stream ended.")
                        break

                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_place.image(frame, channels="RGB")

                    # Break if stop button is pressed
                    if stop_button:
                        st.write("Stream stopped.")
                        break

                    time.sleep(0.03)  # Adjust for frame rate

                self.cap.release()

        if temp_file:
            temp_file.close()

app = Project2()
app.app()
