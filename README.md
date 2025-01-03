# Enhanced Pong Game

A modern implementation of the classic Pong game built with Python's Turtle graphics. This version includes multiple enhancements like power-ups, difficulty levels, and multiplayer features.
##Demo 
![image](https://github.com/user-attachments/assets/00055e40-e649-4f11-b954-958b8f133e0f)

## 🎮 Features

- **Multiplayer Support**
  - Two-player gameplay with customizable names
  - Player A (Red paddle) vs Player B (Blue paddle)
  - Individual score tracking

- **Game Mechanics**
  - Multiple difficulty levels (Easy, Medium, Hard)
  - Dynamic ball speed adjustments
  - Power-up system
  - Multi-ball feature
  - Score limit of 10 points to win

- **Enhanced Gameplay**
  - Pause functionality
  - Sound effects with toggle option
  - Countdown timer before game starts
  - Clear visual instructions
  - Paddle size power-ups
  - Border collision detection

## 🛠️ Requirements

- Python 3.x
- Turtle graphics module (built-in)
- winsound module (for Windows systems)

## 🎯 Installation

1. Clone this repository or download the source code
2. Ensure you have the required sound files in your project directory:
   - bounce.wav
   - score.wav
   - LevelPass.wav

## 🎲 How to Play

1. Run the game:
```bash
python PongGame.py
```

2. Enter player names when prompted
3. Select difficulty level (1-3)
4. Use the following controls:

### Controls
- **Player A (Left Paddle)**
  - W: Move Up
  - S: Move Down

- **Player B (Right Paddle)**
  - ↑ (Up Arrow): Move Up
  - ↓ (Down Arrow): Move Down

### Additional Controls
- P: Pause/Unpause game
- M: Toggle sound on/off
- 1: Easy difficulty
- 2: Medium difficulty
- 3: Hard difficulty

## 🎵 Sound Effects

- Paddle hit sound
- Scoring sound
- Victory sound
- Toggle-able sound system

## 🏆 Scoring System

- First player to reach 10 points wins
- Points are scored when the opponent misses the ball
- Multi-ball feature activates at specific score thresholds

## 🎨 Visual Features

- Color-coded paddles (Red for Player A, Blue for Player B)
- White ball(s)
- Black background
- Clear score display
- Helpful control instructions
- Victory screen with final score

## 🔧 Technical Details

- Window Size: 800x600 pixels
- Customizable paddle sizes
- Dynamic ball physics
- Multiple ball support
- Power-up system with timer
- Boundary collision detection

## 💫 Special Features

1. **Multi-ball Mode**
   - Activates at specific score thresholds
   - Adds extra challenge and excitement

2. **Power-up System**
   - Random power-up activations
   - Temporary effects lasting 10 seconds
   - Paddle size modifications

3. **Difficulty Levels**
   - Easy: Slower ball speed
   - Medium: Moderate ball speed
   - Hard: Fast ball speed

## 🤝 Contributing

Feel free to fork this project and submit pull requests. You can also open issues for bugs or feature suggestions.

## 📝 License

This project is open source and available under the MIT License.

## 🎮 Credits

Created by DuyMinh - A modern take on the classic Pong game with enhanced features and gameplay mechanics.
