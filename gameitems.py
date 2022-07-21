from advlib import *

# TODO: Create At Least 3 Items For Each Room


# Item Creation
cane = Item('cane', 'wooden cane', 'walking cane')
cane.description = 'A sturdy wooden cane.'
cane.pickup = True
cane.wearable = True
cane.edible = False
cane.context = 'cane'

gun = Item('gun', 'pistol', 'handgun')
gun.description = 'A 9mm pistol.'
gun.pickup = True
gun.wearable = False
gun.edible = False
gun.context = 'gun'




