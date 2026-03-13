🎨 Hand Gesture Paint GUI

Draw on a virtual canvas using just your hand gestures! Select colors, erase mistakes, and create art in real-time—no touchscreen required. Perfect for showcasing computer vision, hand tracking, and interactive UI skills.

Get Started
 • Demo Video
 • Documentation

🖌️ Overview

The Hand Gesture Paint App is a real-time gesture-based drawing application built with Python, OpenCV, and MediaPipe. Using your webcam, it tracks your hand movements and lets you:

Draw naturally with your index finger

Change colors or erase with simple gestures

Automatically record your drawing session as a video

This project is ideal for portfolios, academic projects, or interactive demos.

✨ Key Features
🎨 Gesture-Based Drawing

Draw freely using your index finger

Smooth, responsive lines that follow hand movement

🖌 Color & Eraser Selection

Raise two fingers (index + middle) to enter selection mode

Choose from multiple colors or black for erasing

Selection limited to the header to prevent accidental changes

🖼 Virtual Canvas

Drawings appear on a separate canvas over the live webcam feed

Merge canvas with video feed for a natural painting experience

💾 Video Recording

Sessions are automatically recorded as drawing_output.avi

Easy playback and sharing of your creations

⚡ Real-Time Performance

MediaPipe Hands for accurate landmark detection

Smooth performance on modern CPUs with minimal lag

🖥 Screenshots

Header with Color Palette
 ![img1](https://github.com/user-attachments/assets/128f9630-20f6-4f99-9f53-808297b3c1d0)


🚀 Getting Started
Prerequisites

Python 3.8+

Webcam

Virtual Environment (recommended)

Installation

Clone the repository:

git clone https://github.com/yourusername/HandGesturePaint.git
cd HandGesturePaint

Create and activate a virtual environment:

python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate

Run the app:

python main.py

Controls:

Gesture	Action
Two fingers up in header	Select color / eraser
Index finger only	Draw on canvas
Black color	Erase previous lines

Press ESC to exit. 

🏗 Technology Stack

Python

OpenCV — Video capture & drawing utilities

MediaPipe — Hand tracking and landmark detection

NumPy — Canvas & image processing

📊 File Structure
HandGesturePaint/
│
├─ images/               # Color palette headers
├─ main.py               # Main application script
├─ htm.py                # Hand tracking module
├─ drawing_output.avi    # Recorded drawing session
├─ run_app.bat           # command to execute
└─ README.md             # Project documentation
🎥 Demo Video

Check out the app in action: drawing_output.avi

Shows real-time drawing, color selection, and erasing functionality.

🤝 Contributing

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m "Add feature")

Push to the branch (git push origin feature-name)

Open a Pull Request

🙏 Acknowledgments

MediaPipe Hands — Hand tracking

OpenCV — Computer vision and drawing utilities

Inspired by gesture-based drawing apps and interactive UI design
