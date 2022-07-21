from gamerooms import *

# Create Character Inventories

player_inventory = Bag()

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
                current_room.visited = True
                say(current_room)
            else:
                say("You seem confused as to where you want to go.")


@when('attack')
def attack():
    if player_inventory:
        for item in player_inventory:
            if item.context == 'cane':
                say("You attack with your cane")
    else:
        say("You attack.")


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

        # TODO: Finish Dialogue Functionality (Allow Conditions To Be Altered if Certain Dialogue Reached)

        for option in char.dialogue_options.values():
            print(option)


# Getting Information About The Room (Looking)


@when("describe THING")
@when("examine THING")
@when("look at THING")
def look_at(thing):
    global player_inventory, current_room

    obj = current_room.items_in_room.find(thing)
    if not obj:
        obj = current_room.chars_in_room.find(thing)
        if not obj:
            say(f"You can't see {thing} anywhere.")
    else:
        say(f"You look closer at {thing}. {obj.description}")


# Inspecting Items


@when('inspect ITEM')
@when('look at ITEM')
@when('study ITEM')
def inspect(item):
    print(f"You inspect the {item}.")


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
