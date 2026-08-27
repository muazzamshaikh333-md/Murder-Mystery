# Murder-Mystery

# Murder Mystery Escape Room 🔎

A text-based murder mystery escape room game built in Python. Explore rooms, collect clues, check suspects, and accuse the killer before it's too late!

## 🎮 How to Play

Run the game and use the following commands:

| Command | Description |
|---|---|
| `look` | Look around the current room and see available clues |
| `move [room]` | Move to another room (e.g. `move kitchen`) |
| `take [item]` | Pick up a clue from the current room (e.g. `take torn letter`) |
| `inventory` | View all the clues you've collected so far |
| `suspects` | View the list of suspects with their motive and alibi |
| `accuse [suspect]` | Accuse a suspect of the murder (e.g. `accuse muazzam`) |
| `quit` | Exit the game |

## 🗺️ Rooms

- **Study** — Where the body was found. Contains key physical evidence.
- **Kitchen** — Signs of a struggle.
- **Library** — Hides the victim's diary.

## 🕵️ Suspects

- **Faiza**
- **Rumana**
- **Muazzam**

Each suspect has a motive and an alibi. Collect clues around the mansion to figure out who's telling the truth — and who the real killer is.

## 🚀 Running the Game

```bash
python escape.py
```

Make sure you have Python 3 installed.

## 🛠️ Built With

- Python (dictionaries, functions, loops, conditionals)

## 📌 Status

Work in progress — built as a learning project while going through Python basics.

## 📝 Future Improvements

- Hint system for clue collection
- Limited number of accusation attempts
- Colored terminal output for suspense
