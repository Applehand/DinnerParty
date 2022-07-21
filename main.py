from gamerooms import *

# Set The Starting Room as Current Room
current_room = foyer



# Movement Command Definitions

@when('enter ROOM')
def enter(room: str):
    global current_room

    room_split = room.split()

    for r in current_room.connections:
        for word in room_split:
            if r == word and word in room_keys:
                current_room = current_room.connections[word]
                print(current_room)


# Character Interaction


def dialogue():
    pass



@when("talk to CHARACTER")
def talk_to(character: str):
    global current_room

    char = current_room.chars_in_room.find(character)

    # If the character is not in the room
    if not char:
        print(f"You do not see {character} in this room. {current_room.chars_in_room} are here though.")

    # If the character is in the room
    else:
        # Set the context, and start the encounter
        set_context(char.context)
        say(char.greeting)
        dialogue()


# Getting Information About The Room (Looking)

# Inspecting Items

# Picking Up Objects

# Using Items


start()
