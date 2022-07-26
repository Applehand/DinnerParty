import requests
from gamerooms import *


# Generate List of 50 Random Quotes from API

@when('quote')
def quote():
    request = requests.get('https://zenquotes.io/api/quotes')
    data = request.json()
    quotes = [q['q'] for q in data]



# Shows Current Room's Connections


def show_connections():
    global current_room
    print('This room is connected to:')
    for r in current_room.connections:
        print(current_room.connections[r].name)


# Set The Front Yard As The Current Room And Prints Its Description/Connections On Game Start

current_room = front_yard
print('')
print(current_room)
print('')
show_connections()


# TODO: Create special actions like looting a body, etc.

# Changing Rooms


@when('go ROOM')
@when('go to the ROOM')
@when('go to ROOM')
@when('enter ROOM')
def enter(room: str):
    global current_room

    room_split = room.split()

    entered_or_locked = False
    is_same_room = True

    for r in current_room.connections:
        for word in room_split:
            if r == word and word in room_keys:
                target_room = current_room.connections[word]
                if not target_room:
                    print("You are already in that room.")
                elif target_room.locked:
                    say(target_room.locked_descr)
                    entered_or_locked = True
                    is_same_room = False
                else:
                    current_room = target_room
                    entered_or_locked = True
                    is_same_room = False
                    set_context(current_room.context)

                    if not current_room.visited:
                        say(current_room)
                        show_connections()

                    else:
                        say(current_room.short_descr)
                        show_connections()

    if not entered_or_locked and not is_same_room:
        print('You hesitate, unsure where to go.')

    current_room.visited = True


# TODO: Create Character Responses When Attacked

@when('assassinate CHARACTER')
@when('kill CHARACTER')
@when('attack CHARACTER')
def attack(character: str):
    global current_room

    char = current_room.chars.find(character)
    print(char)


# Talk to Character / Dialogue

def dialogue(char):
    global current_room
    print('')
    set_context(char.context)
    say(f"{char} says:{char.greeting}")
    print('')

    dialogue_index = []
    n = 0

    # TODO: Expand Dialogue Functionality (Allow Conditions To Be Altered if Certain Dialogue Reached, Continue Dialogue
    #  After Choosing Option)

    print("YOUR RESPONSE:")
    for option in char.dialogue_options.values():
        n += 1
        dialogue_index.append(n)

        print(f'{dialogue_index[n - 1]}> {option}\n')
    choice = 'response' + input('Choose a number\n>')
    print('')
    print(f"{char} says: {char.dialogue_responses[choice]}")

    set_context(None)


@when("talk to CHARACTER")
def talk_to(character: str):
    global current_room

    char = current_room.chars.find(character)

    # If the character is not in the room
    if not char:
        print(f"You do not see {character} in this room.")

    # If the character is in the room
    else:
        dialogue(char)  # Start the Dialogue Interaction


# Getting Information About The Room (Looking)

@when('where')
@when('room')
def room():
    print(current_room)
    print('')
    print('This room is connected to:\n')
    for r in current_room.connections:
        print(current_room.connections[r].name)
        print('')
    print('These characters are in the room:')
    for p in current_room.chars:
        print(p)
    print('')
    print('These items are in the room:')
    for i in current_room.items:
        print(i)


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

    if obj:
        player_inventory.add(obj)
        say(f"{thing} has been added to your inventory.")
    else:
        say(f"{thing} is not in the vicinity.")


# TODO: Create More Special Items and Their Actions
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
