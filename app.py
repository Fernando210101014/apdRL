import os

import cv2
from flask import Flask, Response, render_template
from ultralytics import YOLO

app = Flask(__name__)

model = YOLO("best.pt")
VIDEO_PATH = "mp4/video.mp4"  # Sesuaikan path video

def generate_frames():
    cap = cv2.VideoCapture(VIDEO_PATH)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)
        result_frame = results[0].plot()

        _, buffer = cv2.imencode('.jpg', result_frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
