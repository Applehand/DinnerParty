from gamechars import *

# TODO: Expand Descriptions and Create Shorter Descriptions If Location Has Already Been Visited

# Room Definitions
main_hall = Room("""
A long, crimson carpet extends the length of the main hall. 
""")
main_hall.name = 'The Main Hall'

foyer = Room("""
Soft benches line one side of the foyer, with tall cabinets on the other.
""")
foyer.name = 'The Foyer, or Entrance Room.'
foyer.short_descr = 'The benches and cabinets are still here.'

grand_showroom = Room("""
The Grand Showroom is full of artifacts with labels detailing their historical significance.
""")
grand_showroom.name = 'The Grand Showroom'

sitting_room = Room("""
Expertly made sofas and chairs decorate the room, with full bookshelves lining every available space.
""")
sitting_room.name = 'The Sitting Room'

dining_room = Room("""
A massive table spans nearly the whole length of the dining room, with glass chandeliers hanging above.
""")
dining_room.name = 'The Dining Room'

private_hall = Room("""
A small connective hall joins many rooms, with a few tables, decorations, and a mirror.
""")
private_hall.name = 'The Private Hall (Servant Hall)'
private_hall.locked_descr = 'There is a small sign in front of the double doors to the private hall \
                            that says, "Closed until 5:30 P.M."'

kitchen = Room("""
The kitchen is heavily used and worn, with blackened ovens and bits of fresh food scrap about the counters.
 """)
kitchen.name = 'The Kitchen'

host_bedroom = Room("""
A spacious bedroom with a massive bed, a few thick rugs, and an alcove with a window and seats.
""")
host_bedroom.name = "The Host's Bedroom"

hidden_room = Room("""
A dark stone room with wooden shelves filled with glassware and experimental instruments.
""")
hidden_room.name = 'The hidden room'

# TODO: Describe 'Characters' Room accordingly.

elder_room = Room("""
A quaint room for guests to lodge comfortably.
""")
elder_room.name = "The Elder's Room"

debutante_room = Room("""
A quaint room for guests to lodge comfortably.
""")
debutante_room.name = "The Debutante's Room"

fool_room = Room("""
A quaint room for guests to lodge comfortably.
""")
fool_room.name = "The Fool's Room"

noble_room = Room("""
A quaint room for guests to lodge comfortably.
""")
noble_room.name = "The Noble's Room"

general_room = Room("""
A quaint room for guests to lodge comfortably.
""")
general_room.name = "The General's Room"

guest_hall = Room("""
A short hallway with 3 doors on the left and two on the right.
""")
guest_hall.name = 'The Guest Hall'

front_yard = Room("""
Sharply cut hedges line the outer walls of the manor. A circular driveway sweeps across the face of the building.
""")
front_yard.name = 'The Front Yard'
front_yard.short_descr = 'Standing on the front yard near the circular drive, you feel the cold as sharp as the hedges.'
front_yard.visited = True

back_yard = Room("""
An expansive backyard dotted with tall trees stretches before you, all the way to the horizon.
""")
back_yard.name = 'The Back Yard'

# Room Connections / Room Layout

room_keys = ['main', 'foyer', 'showroom', 'sitting', 'dining', 'private', 'kitchen', 'bedroom', 'hidden',
             'guest', 'room1', 'room2', 'room3', 'room4', 'room5', 'front', 'back']

foyer.connections = {'main': main_hall, 'front': front_yard}
main_hall.connections = {'foyer': foyer, 'showroom': grand_showroom, 'private': private_hall, 'dining': dining_room,
                         'sitting': sitting_room}
grand_showroom.connections = {'main': main_hall}
sitting_room.connections = {'main': main_hall, 'dining': dining_room}
dining_room.connections = {'main': main_hall, 'sitting': sitting_room, 'kitchen': kitchen}
private_hall.connections = {'main': main_hall, 'guest': guest_hall, 'kitchen': kitchen, 'bedroom': host_bedroom}
kitchen.connections = {'private': private_hall, 'dining': dining_room}
host_bedroom.connections = {'private': private_hall, 'hidden': hidden_room, 'back': back_yard}
hidden_room.connections = {'bedroom': host_bedroom}
guest_hall.connections = {'private': private_hall, 'room1': elder_room, 'room2': debutante_room, 'room3': fool_room,
                          'room4': noble_room, 'room5': general_room, }
elder_room.connections = {'guest': guest_hall}
debutante_room.connections = {'guest': guest_hall}
fool_room.connections = {'guest': guest_hall}
noble_room.connections = {'guest': guest_hall}
general_room.connections = {'guest': guest_hall}
front_yard.connections = {'foyer': foyer, 'back': back_yard}
back_yard.connections = {'front': front_yard, 'bedroom': host_bedroom}

# TODO: Block Access To Rooms Until Constraints Lifted (Create Items or Dialogue Conditions to Satisfy Constraint)

# Room Constraints / Room Conditions

hidden_room.locked = True  # The Entrance Is Hidden Until Dialogue Accessed or Item Found
host_bedroom.locked = True
kitchen.locked = True  # Servants are preparing dinner, so the kitchen is blocked off.
private_hall.locked = True

# Create Room Inventories for Characters

front_yard.chars = Bag([the_host, the_elder, the_general, the_fool, the_debutante, the_noble, galatea])
foyer.chars = Bag()
main_hall.chars = Bag()
grand_showroom.chars = Bag()
sitting_room.chars = Bag()
dining_room.chars = Bag()
private_hall.chars = Bag()
kitchen.chars = Bag()
host_bedroom.chars = Bag()
hidden_room.chars = Bag()
guest_hall.chars = Bag()
elder_room.chars = Bag()
debutante_room.chars = Bag()
fool_room.chars = Bag()
noble_room.chars = Bag()
general_room.chars = Bag()


# Create Room Inventories for Items

front_yard.items = Bag(front_yard_items)
foyer.items = Bag(foyer_items)
main_hall.items = Bag(main_hall_items)
grand_showroom.items = Bag(grand_showroom_items)
sitting_room.items = Bag(sitting_room_items)
dining_room.items = Bag(dining_room_items)
private_hall.items = Bag(private_hall_items)
kitchen.items = Bag(kitchen_items)
host_bedroom.items = Bag(host_bedroom_items)
hidden_room.items = Bag(hidden_room_items)
guest_hall.items = Bag(guest_hall_items)
elder_room.items = Bag(room1_items)
debutante_room.items = Bag(room2_items)
fool_room.items = Bag(room3_items)
noble_room.items = Bag(room4_items)
general_room.items = Bag(room5_items)
