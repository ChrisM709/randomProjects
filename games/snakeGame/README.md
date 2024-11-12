# Snake Game

A classic Snake game implemented using JavaScript, HTML5, and CSS. The game involves controlling a snake that grows longer each time it eats food, while avoiding collisions with the walls and itself. The game keeps track of your score and displays the highest score achieved across sessions.

## Features
- **Snake Movement:** Use arrow keys to control the snake's direction.
- **Dynamic Difficulty:** The snake changes color with every food eaten.
- **High Score Persistence:** The highest score is saved to `localStorage` and remains between sessions.
- **Game Over Screen:** The game shows a "YOU LOSE!" message when the snake collides with the walls or itself.
- **Play Again Button:** Restart the game after a game over by clicking the "Play Again" button.

## Installation
To get started with this game, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/snake-game.git
```

Once you’ve cloned the repository, open the `index.html` file in your browser to start playing.

## Usage
1. Open the `index.html` file in any modern browser (Chrome, Firefox, etc.).
2. Click the **Start** button to begin the game.
3. Use the **Arrow Keys** (Up, Down, Left, Right) to control the snake.
4. The game will end when the snake collides with the wall or its own body.
5. Once the game is over, you can click the **Play Again** button to restart.

## How It Works
- **Snake Movement:** The snake moves in a grid-like fashion based on keyboard input (arrow keys). It moves in a set direction (horizontal or vertical) and changes direction based on player input.
- **Growth:** Each time the snake eats food, it grows by one segment, and the score increases.
- **High Score:** The high score is updated if the current score exceeds the previous high score and is saved to `localStorage` for future sessions.

## High Score Feature
- The game tracks the highest score achieved, and it will be displayed on the game page.

## Contributing
Feel free to fork the repository and create a pull request if you'd like to contribute. Here’s how to get started:

## License
This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments
- The classic Snake game inspired the design and gameplay.
- Thanks to [Doto](https://fonts.google.com/specimen/Doto) for the font used in the game.
