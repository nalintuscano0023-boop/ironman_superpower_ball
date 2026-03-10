Iron Man Wavy Energy Ball 

Author: Nalin Tuscano

This project is a hand-gesture controlled interactive energy ball built using Python, OpenCV, and MediaPipe. The system uses your webcam to detect your hand in real time and generates a glowing wavy plasma ball that follows your hand movement.

The idea behind this project was to experiment with computer vision + creative visual effects, turning simple hand tracking into something that feels like controlling an Iron Man–style energy orb.



Project Concept

Instead of using a mouse or keyboard, this program uses hand gestures captured by a webcam.

When the camera detects your hand:

 The energy ball follows your hand movement
 The size of the ball changes based on your hand gesture
 The ball has a wavy animated boundary that creates a   plasma like energy effect
 A glow layer with blur gives the ball a strong neon glow

Even in a darker room, the ball still appears bright due to the glow rendering effect.



Features

• Real time hand tracking using MediaPipe
• Gesture based control of the energy ball
• Animated wavy plasma boundary
• Strong glowing neon effect
• Smooth hand following motion
• Fully implemented using Python + OpenCV rendering



Technologies Used

 Python
 OpenCV
 MediaPipe
 NumPy
 Computer Vision concepts

These technologies allow the project to combine AI based hand detection with dynamic graphical effects.



How It Works

1. The webcam captures live video using OpenCV.
2. MediaPipe detects the hand and extracts landmark positions.
3. The palm position determines where the energy ball appears.
4. The distance between finger landmarks controls the ball size.
5. A sin wave distortion algorithm creates the animated wavy boundary.
6. A blurred glow layer produces the bright energy aura.



Installation

Install the required Python libraries:


pip install opencv-python mediapipe numpy




Running the Project

Navigate to the project folder and run:


python main.py


Make sure your webcam is enabled.

Press ESC to exit the program.



Controls

 Gesture        Action                        
 
 Move hand      Energy ball follows your hand 
 Open hand      Ball becomes larger           
 Close hand     Ball becomes smaller          


Learning Outcome

Building this project helped explore:

• Real time hand tracking with MediaPipe
• Computer vision based interaction
• Procedural graphics using mathematical wave functions
• Creating glow and visual effects using OpenCV image processing

It also shows how simple computer vision techniques can create interactive visual experiences.



Future Improvements

Possible future enhancements include:

• Energy particle system
• Lightning effects around the ball
• Repulsor beam attack gesture
• Target shooting game mode
• Iron Man style HUD interface



Always exploring new ideas in AI, computer vision, and creative coding.

#Python #ComputerVision #OpenCV #MediaPipe #AIProjects #NalinTuscano
