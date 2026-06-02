# MiniMax

MiniMax is a small Python/Pygame strategy game prototype where a thief tries to avoid three police agents on a node-based map.  
The police use a minimax-based decision step to choose their moves after each player action.

## How it works

- The board is a 21x21 grid.
- Only selected cells are playable nodes.
- The red token is the thief (player).
- Blue tokens are police agents (AI).
- On each turn:
  1. You click a reachable neighboring node to move the thief.
  2. Police agents respond with an AI move.
- The game ends when the thief has no legal moves left.

## Requirements

- Python 3.10+
- `pygame`

Install dependency:

```bash
python -m pip install pygame
```

## Run the game

From the repository root:

```bash
python /tmp/workspace/MandaLuc/MiniMax/Test.py
```

## Controls

- **Mouse click**: move the thief to a valid adjacent node.
- **Close window**: quit the game.

## Project files

- `/tmp/workspace/MandaLuc/MiniMax/Test.py`: main runnable script (board setup + game loop start)
- `/tmp/workspace/MandaLuc/MiniMax/Plateau.py`: game loop, rendering, and turn management
- `/tmp/workspace/MandaLuc/MiniMax/Police.py`: police entity and minimax logic
- `/tmp/workspace/MandaLuc/MiniMax/Thief.py`: thief entity
- `/tmp/workspace/MandaLuc/MiniMax/Node.py`: node model and drawing
- `/tmp/workspace/MandaLuc/MiniMax/Entity.py`: shared movement logic
- `/tmp/workspace/MandaLuc/MiniMax/Position.py`: position helper class

## Notes

- Background music (`music.mp3`) plays during the game.
- `Game.py` is currently not a runnable entrypoint; use `Test.py`.
