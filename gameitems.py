from advlib import *

# TODO: Create At Least 3 Novelty Items, 3 Weapons, and 3 Gear For Each Room


# Item Creation


cane = Item('cane', 'wooden cane', 'walking cane')  # Starts In Foyer, Belongs to General
cane.description = 'A sturdy wooden cane with a rough, misshaped handle made from the antler of some unknown animal.'
cane.pickup = True
cane.wearable = True
cane.edible = False
cane.context = 'cane'

gun = Item('gun', 'pistol', 'handgun')  # Starts In Bedroom
gun.description = "A black 9mm pistol with it's identification markings scrubbed clean."
gun.pickup = True
gun.wearable = False
gun.edible = False
gun.context = 'gun'



