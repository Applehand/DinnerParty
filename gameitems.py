from advlib import *

# TODO: Create At Least 3 Novelty Items, 3 Weapons, and 3 Gear For Each Room


# Item Creation

cane = Item('cane', 'wooden cane', 'walking cane')  # Starts In Foyer, Belongs to General
cane.description = 'A sturdy wooden cane with a rough, misshaped handle made from the antler of some unknown animal.'
cane.pickup = True
cane.wearable = True
cane.edible = False

gun = Item('gun', 'pistol', 'handgun')  # Starts In Bedroom, Belongs to Host
gun.description = "A black 9mm pistol with it's identification markings scrubbed clean."
gun.pickup = True
gun.wearable = False
gun.edible = False

rock = Item('rock', 'stone')  # Starts in front yard.
rock.description = 'A heavy rock.'
rock.pickup = True
rock.wearable = False
rock.edible = False

watch = Item('watch', 'pocket watch', 'golden pocket watch')  # The Noble's Golden Pocket watch
watch.description = 'A fine golden pocket watch with a large orange fuel truck engraved on the back.'
watch.pickup = True
watch.wearable = True
watch.edible = False

# Room Inventory Lists

front_yard_items = [rock]
foyer_items = [cane]
main_hall_items = []
grand_showroom_items = []
dining_room_items = []
sitting_room_items = []
private_hall_items = []
kitchen_items = []
guest_hall_items = []
room1_items = []
room2_items = []
room3_items = []
room4_items = []
room5_items = []
host_bedroom_items = [gun]
hidden_room_items = []

# Character Inventory Lists

host_personal_items = []
elder_personal_items = []
general_personal_items = []
debutante_personal_items = []
fool_personal_items = []
noble_personal_items = [watch]
galatea_personal_items = []


