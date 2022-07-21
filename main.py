from gamerooms import *

# Set The Foyer As The Current Room On Game Start
current_room = foyer

# Create Player and NPC Inventories
inventory = Bag()
player_conditions = []


# Action Command Definitions

@when('enter ROOM')
def enter(room: str):
    global current_room

    room_split = room.split()

    for r in current_room.connections:
        for word in room_split:
            if r == word and word in room_keys:
                current_room = current_room.connections[word]
                set_context(current_room.context)
                say(current_room)


@when('attack')
def attack():
    if get_context() == 'cane':
        print("You attack with your cane.")
    else:
        print('You attack.')


# Talk to Character / Dialogue

@when("talk to CHARACTER")
def talk_to(character: str):
    global current_room

    char = current_room.chars_in_room.find(character)

    # If the character is not in the room
    if not char:
        print(f"You do not see {character} in this room.")

    # If the character is in the room
    else:
        # Start the Dialogue Interaction
        set_context(char.context)
        say(char.greeting)

        for option in char.dialogue_options.values():
            print(option)

# Getting Information About The Room (Looking)

# Inspecting Items


@when('inspect ITEM')
@when('look at ITEM')
@when('study ITEM')
def inspect(item):
    print(f"You inspect the {item}.")


# Picking Up Items


@when('take THING')
@when('grab THING')
@when('pick up THING')
def take(thing):
    if thing in current_room.items_in_room:
        say(f"You take the {thing} and add it to your inventory.")
        inventory.add(thing)
        set_context(thing)


# Using Items


@when('shoot gun')
def shoot_gun():
    if get_context() == 'gun':
        say('You shoot the gun.')
    else:
        say("You don't have a gun.")





start()
