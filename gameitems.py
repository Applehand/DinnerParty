from advlib import *

# Item Creation
cane = Item('cane', 'wooden cane', 'walking cane')
cane.description = 'A sturdy wooden cane.'
cane.pickup = True
cane.wearable = True
cane.edible = False
cane.context = 'cane'

gun = Item('pistol', 'gun', 'handgun')
gun.description = 'A 9mm pistol.'
gun.pickup = True
gun.wearable = False
gun.edible = False
gun.context = 'gun'




