
# Minesweeper Game 🎮  

A **classic Minesweeper game** built using **Python (Tkinter)**.  
This project brings back the nostalgic game with a clean graphical interface, difficulty levels, and a **save/load game state feature** to continue your progress anytime.

---

## 🚀 Features
- 🎨 **Graphical User Interface (GUI)** built with **Tkinter** for a smooth and interactive gameplay experience.  
- ⚡ **Three difficulty levels:**  
  - Easy (8×8 grid, 10 mines)  
  - Normal (16×16 grid, 40 mines)  
  - Hard (16×30 grid, 99 mines)  
- 💾 **Save and Load Game State**:
  - Automatically saves progress to a JSON file named after the player.  
  - Resume your game later by entering the same username.  
- 🏆 Automatic **Win and Game Over detection**.  
- 🚩 **Right-click to place or remove flags** on suspected mines.  
- 🔄 **Restart and Main Menu navigation** without restarting the program.

---

## 🛠️ Technologies Used
- **Python 3.x**  
- **Tkinter** – for the graphical user interface  
- **JSON** – for game state persistence

---

## 📂 Project Structure
```

minesweeper-game/
│
├── minesweeper-game.py   # Main game code
├── README.md             # Project documentation
└── <username>.json       # Saved game data (generated during gameplay)

````

---

## ⚙️ Installation & Setup
Follow these steps to run the game on your machine:

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/minesweeper-game.git
   cd minesweeper-game
````

2. **Run the game**

   ```bash
   python minesweeper-game.py
   ```

> **Note:** Make sure you have **Python 3.x** installed.

---

## 🎮 How to Play

1. Launch the game by running `minesweeper-game.py`.
2. Enter your **name** when prompted.
3. Choose a **difficulty level**:

   * Easy
   * Normal
   * Hard
4. **Controls:**

   * **Left-click** a cell to reveal it.
   * **Right-click** a cell to **place or remove a flag**.
5. Win by **revealing all non-mine cells**.
6. If you reveal a mine — **Game Over** 💥.

---

## 💾 Save and Load Feature

* The game **automatically saves your progress** to a JSON file named after your username.
* You can **resume the game later** by entering the same username on startup.
* Saved games are automatically **deleted** when:

  * You **win the game**.
  * You **lose the game**.

---

## 🔄 Restarting the Game

* After winning or losing, you can:

  * **Restart immediately** with the same settings.
  * **Return to the main menu** to select a new difficulty.

---

## 🧩 Example JSON Save File

Here’s an example of what the saved game file looks like:

```json
{
  "rows": 8,
  "columns": 8,
  "mines": 10,
  "game_state": "playing",
  "name": "player1",
  "cells": [
    [
      {
        "value": 0,
        "revealed": false,
        "flagged": false
      }
    ]
  ]
}
```

---

## 💡 Future Improvements

* Add a **timer** to track how long the game takes.
* Create a **leaderboard** for fastest completions.
* Enhance the UI with **custom graphics and themes**.
* Add **sound effects** for cell reveals, flags, and game over events.
* Enable **custom board sizes and mine counts**.

---

## 🤝 Contributing

Contributions are welcome!
To contribute:

1. **Fork the repository**
2. Create a new feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add new feature"
   ```
4. Push your branch:

   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a **pull request**.

---

## 📧 Contact

For any questions or collaboration opportunities:

* **Developer:** Belal Mohamed Fathy Sayed Nasr
* **Email:** [belalnasract@gmail.com](mailto:belalnasract@gmail.com)
* **GitHub:** [Belal6205](https://github.com/Belal6205)

---

## 🌟 Support

If you enjoy this project, please consider giving it a ⭐ on GitHub to help it grow!

```
