from gamerooms import *

# Set The Front Yard As The Current Room On Game Start
current_room = front_yard

# TODO: Create a Time Tracker Where Actions Add to time_passed Based On action_weight

# TODO: Create special actions like looting a body, etc.

# Changing Rooms

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


# TODO: Create Simple Combat System (Assassination if surprise attack.)

@when('attack')
def attack():
    obj = player_inventory.find('cane')
    if obj:
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

    char = current_room.chars.find(character)
    print(char.animate)

    # If the character is not in the room
    if not char:
        print(f"You do not see {character} in this room.")

    # If the character is in the room
    else:
        dialogue(char)  # Start the Dialogue Interaction


# Getting Information About The Room (Looking)

# TODO: Create looking_at system for getting information about the room,
#  it's connections, short_descr of the items in the room, and the people in the room

# Inspecting Items

@when("describe ITEM")
@when("examine ITEM")
@when("look at ITEM")
def examine(item):
    global player_inventory

    obj = player_inventory.find(item)
    print(player_inventory)

    if not obj:
        say(f"You don't have {item} in your inventory.")

    else:
        say(f"""You inspect the {item} closer. {obj.description}""")


# Picking Up Items


@when('get THING')
@when('take THING')
@when('grab THING')
@when('pick up THING')
def take(thing):
    global current_room

    obj = current_room.items.take(thing)
    print(current_room.items)

    if obj:
        player_inventory.add(obj)
        say(f"{thing} has been added to your inventory.")
    else:
        say(f"{thing} is not in the vicinity.")


# Using Special Items

@when('shoot gun')
@when('shoot')
def shoot():
    global player_inventory

    obj = player_inventory.find('gun')
    if obj:
        say("You shoot your gun and it is loud.")
    else:
        say("You don't have a gun, idiot.")


start()
