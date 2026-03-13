🎨 Hand Gesture Paint App

Get Started • Features • Screenshots • Demo Video • Documentation

Draw on a virtual canvas using your hand gestures! Select colors, erase mistakes, and create art in real-time without touching the screen. Perfect for showcasing computer vision and hand tracking skills.

Get Started
 | View Demo Video

🖌️ Overview

The Hand Gesture Paint App is a real-time gesture-based drawing application built with Python, OpenCV, and MediaPipe. It tracks your hand movements using a webcam and allows you to draw, change colors, and erase on a virtual canvas.

Clean UI and smooth drawing experience.

Select different colors or erase using simple gestures.

Automatically records your drawing session as a video.

This project is ideal for academic projects, portfolios, or interactive demos.

✨ Key Features
🎨 Gesture-Based Drawing

Draw freely using your index finger.

Smooth and responsive lines that follow your hand movement.

🖌 Color & Eraser Selection

Two fingers up to enter selection mode.

Select from multiple colors or choose black as an eraser.

Selection is limited to the header area, preventing accidental color changes while drawing.

🖼 Virtual Canvas

Your drawings appear on a separate canvas over the live webcam feed.

Merge canvas with video feed for a natural painting experience.

💾 Video Recording

Automatically records your drawing session.

Saved as drawing_output.avi for easy playback and sharing.

⚡ Real-Time Performance

Uses MediaPipe Hands for accurate hand landmark detection.

Runs smoothly on modern CPUs with minimal lag.

🖥 Screenshots

Header with Color Palette


Drawing Mode


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
.\.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux / Mac

Install required packages:

pip install -r requirements.txt
Usage

Run the main script:

python main.py

Controls:

Gesture	Action
Two fingers up (index + middle) in header	Select color / eraser
Index finger only	Draw on canvas
Black color	Erase previous lines

Press ESC to exit the application.

Your drawing session is automatically recorded as drawing_output.avi.

🏗 Technology Stack

Python

OpenCV — Video capture and drawing utilities

MediaPipe — Hand tracking and landmark detection

NumPy — Canvas and image processing

📊 File Structure
HandGesturePaint/
│
├─ images/               # Color palette headers
├─ main.py               # Main application script
├─ htm.py                # Hand tracking module
├─ drawing_output.avi    # Recorded drawing session
├─ requirements.txt      # Python dependencies
└─ README.md             # Project documentation
🎥 Demo Video

Check out a demonstration of the app in action:

drawing_output.avi

Shows real-time drawing, color selection, and erasing functionality.

🤝 Contributing

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m 'Add feature')

Push the branch (git push origin feature-name)

Open a Pull Request

🙏 Acknowledgments

MediaPipe Hands for hand tracking

OpenCV for computer vision and drawing utilities

Inspired by gesture-based drawing applications and interactive UI design
