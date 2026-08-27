# Rooms dictionary
rooms = {
    "study": {
        "description": "Ek dusty study room hai. Ek almirah aur table hai. Rahul ki lash yahi mili thi.",
        "clues": ["bloody knife", "torn letter", "handkerchief"]
    },
    "kitchen": {
        "description": "Kitchen me kuch bikhra hua hai, jaise koi jaldi me tha.",
        "clues": ["broken glass", "poison bottle"]
    },
    "library": {
        "description": "Purani kitabon se bhari library, ek diary chhupi hui hai.",
        "clues": ["victim's diary"]
    }
}

current_room = "study"
inventory = []

# Suspects dictionary
suspects = {
    "faiza": {
        "motive": "Rahul se paise udhaar liye the, wapas nahi karne the",
        "alibi": "Kaha raha ki wo party me thi"
    },
    "rumana": {
        "motive": "Rahul ne uska raaz jaan liya tha",
        "alibi": "Kaha raha ki wo so rahi thi"
    },
    "muazzam": {
        "motive": "Rahul se purani dushmani thi",
        "alibi": "Kaha raha ki wo ghar pe akela tha"
    }
}

victim = "rahul"
real_killer = "muazzam"

# Extra hints jab specific clues collect kare
clue_hints = {
    "torn letter": "Letter me likha hai: 'Rahul, tune meri izzat barbaad ki, iska hisaab dena hoga - M'",
    "victim's diary": "Diary me likha hai: 'Muazzam aaj bhi dhamki de raha tha, darr lag raha hai...'",
    "handkerchief": "Ye rumal khoon se bharaa hua hai, aur isme 'M' letter embroider hai."
}


def look(room_name):
    room = rooms[room_name]
    print(room["description"])
    print("Yaha ye clues hai:", room["clues"])


def move(room_name):
    global current_room
    if room_name in rooms:
        current_room = room_name
        look(current_room)
    else:
        print("Ye room exist nahi karta!")


def read_clue(item):
    if item in clue_hints:
        print(f"\n[Clue detail]: {clue_hints[item]}")


def take(item):
    room = rooms[current_room]
    if item in room["clues"]:
        inventory.append(item)
        room["clues"].remove(item)
        print(f"Tune '{item}' utha liya!")
        read_clue(item)
    else:
        print("Ye item yaha nahi hai.")


def show_suspects():
    print("\n--- Suspects ---")
    for name, info in suspects.items():
        print(f"{name.capitalize()}: Motive - {info['motive']}, Alibi - {info['alibi']}")


def accuse(suspect_name):
    if suspect_name == real_killer:
        print(f"\nSahi pakda! {suspect_name.capitalize()} hi asli killer tha. Case solved!")
        print("GAME OVER - TUNE JEET LIYA!")
        return True
    else:
        print(f"\nGalat! {suspect_name.capitalize()} innocent tha. Asli killer bach gaya.")
        print("GAME OVER - TU HAAR GAYA!")
        return True


# Game loop
print(f"=== MURDER MYSTERY: {victim.upper()} KA CASE ===")
print("Clues dhundo, suspects check karo, aur sahi killer pakdo!\n")

while True:
    command = input("\nKya karna hai? (look / move [room] / take [item] / inventory / suspects / accuse [suspect] / quit): ").strip().lower()

    if command == "look":
        look(current_room)
    elif command.startswith("move "):
        room_name = command.replace("move ", "")
        move(room_name)
    elif command.startswith("take "):
        item_name = command.replace("take ", "")
        take(item_name)
    elif command == "inventory":
        print("Tere paas hai:", inventory)
    elif command == "suspects":
        show_suspects()
    elif command.startswith("accuse "):
        suspect_name = command.replace("accuse ", "")
        if suspect_name in suspects:
            game_over = accuse(suspect_name)
            if game_over:
                break
        else:
            print("Ye suspect exist nahi karta.")
    elif command == "quit":
        print("Game khatam!")
        break
    else:
        print("Samajh nahi aaya, dubara try kar.")
