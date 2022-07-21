from gamerooms import *

# TODO: Create a Time Tracker Where Actions Add to time_passed Based On Weight


# Create Character Inventories

player_inventory = Bag()
elder_inventory = Bag()
general_inventory = Bag()
debutante_inventory = Bag()
fool_inventory = Bag()
noble_inventory = Bag()

# Action Command Definitions


@when('go to ROOM')
@when('enter ROOM')
def enter(room: str):
    global current_room

    room_split = room.split()

    for r in current_room.connections:
        for word in room_split:
            if r == word and word in room_keys:
                current_room = current_room.connections[word]
                set_context(current_room.context)
                if not current_room.visited:
                    say(current_room)
                else:
                    say(current_room.short_descr)

                current_room.visited = True


# TODO: Create Simple Combat/Assassination System

@when('attack')
def attack():
    if player_inventory:
        for item in player_inventory:
            if item.context == 'cane':
                say("You attack with your cane.")
    else:
        say("You attack.")


# Talk to Character / Dialogue


def dialogue(char):
    set_context(char.context)
    say(char.greeting)

    # TODO: Expand Dialogue Functionality (Allow Conditions To Be Altered if Certain Dialogue Reached)

    for option in char.dialogue_options.values():
        print(option)

@when("talk to CHARACTER")
def talk_to(character: str):
    global current_room

    char = current_room.chars_in_room.find(character)

    # If the character is not in the room
    if not char:
        print(f"You do not see {character} in this room.")

    # If the character is in the room
    else:
        dialogue(char)  # Start the Dialogue Interaction


# Getting Information About The Room (Looking)
# TODO: Create looking_at system for getting information about the room, it's connections, and the people inside

# Inspecting Items


@when("describe ITEM")
@when("examine ITEM")
@when("look at ITEM")
def examine(item):
    global player_inventory, current_room

    obj = current_room.items_in_room.find(item)
    if not obj:
        obj = current_room.chars_in_room.find(item)
        if not obj:
            obj = player_inventory.find(item)
            if not obj:
                say(f"You don't see a {item} anywhere.")

    else:
        say(f"You look closer at {item}. {obj.description}")


# Picking Up Items


@when('get THING')
@when('take THING')
@when('grab THING')
@when('pick up THING')
def take(thing):
    obj = current_room.items_in_room.take(thing)

    if obj:
        say(f"You take the {thing}.")
        player_inventory.add(obj)
    else:
        print(f"You don't see a {thing} here.")


# Using Special Items

@when('shoot gun')
@when('shoot')
def shoot():
    if player_inventory:
        for item in player_inventory:
            if item.context == 'gun':
                say("You shoot the gun.")
    else:
        say("You don't have a gun.")


start()
