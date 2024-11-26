# Blackjack Game
## Description
The Blackjack Game is a Python implementation of the classic casino card game. This program allows users to play against a computer dealer in an interactive terminal-based environment. The game follows the standard rules of Blackjack, including calculating scores, handling Blackjack conditions, and determining winners based on the closest score to 21 without exceeding it.

---

## Features
* **Interactive Gameplay**: The game prompts users to make decisions at each step.
* **Standard Blackjack Rules**:
  * Cards are drawn randomly.
  * Aces can count as 1 or 11, depending on the user's hand.
  * A Blackjack (21 with two cards) is an automatic win unless both the user and the dealer have it.
* **Dynamic Dealer AI**: The dealer will draw cards until their score is at least 17.
* **Replayable**: Users can play multiple rounds in one session.

---

## Files Included
* `blackjack.py`: The main script implementing the Blackjack game.
* `art.py`: Contains the ASCII art logo displayed during the game.

---
## Prerequisites
* Python 3.x installed on your system.

---

## How to Run
1. Clone or download this repository to your local machine:
    ```shell
    git clone https://github.com/shrabhay/Blackjack.git
    cd blackjack-game
    ```

2. Run the script:
    ```shell
    python3 blackjack.py
    ```

---

## How to Play
1. Launch the game, and you'll see the Blackjack logo.
2. Decide whether to play a round by typing y to start or n to exit.
3. During the game:
   * View your current hand and score.
   * See the dealer's first card.
   * Decide whether to draw another card (y) or pass (n).
4. The game ends when:
   * You or the dealer scores a Blackjack.
   * Your score exceeds 21.
   * You pass and the dealer finishes drawing cards.
5. The winner is determined based on the scores, following standard Blackjack rules.

---

## Example Gameplay
```
Do you want to play a game of Blackjack? Type 'y' or 'n': y

.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |
      `------'                           |__/

Your cards: [10, 7], current score: 17
Computer's first card: 9
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [10, 7], final score: 17
Dealer's final hand: [9, 7, 5], final score: 21
You lose 😤
```   

---

## Future Enhancements
* Add multiplayer functionality for more dynamic gameplay.
* Implement betting and chip management.
* Add a GUI for a more user-friendly experience.
* Introduce configurable rules for variations of Blackjack.

---

## License
This project is open-source and available under the MIT License.

---

## Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

## Acknowledgments
This project is inspired by the traditional Blackjack card game and demonstrates Python programming techniques, including lists, functions, and decision-making.

