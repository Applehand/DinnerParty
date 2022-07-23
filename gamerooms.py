from gamechars import *

# TODO: Expand Descriptions and Create Shorter Descriptions If Location Has Already Been Visited

# Room Definitions
main_hall = Room("""
A long, crimson carpet extends the length of the main hall. 
""")

foyer = Room("""
Soft benches line one side of the foyer, with tall cabinets on the other.
""")
foyer.short_descr = 'The benches and cabinets are still here.'

grand_showroom = Room("""
The Grand Showroom is full of artifacts with labels detailing their historical significance.
""")

sitting_room = Room("""
Expertly made sofas and chairs decorate the room, with full bookshelves lining every available space.
""")

dining_room = Room("""
A massive table spans nearly the whole length of the dining room, with glass chandeliers hanging above.
""")

private_hall = Room("""
A small connective hall joins many rooms, with a few tables, decorations, and a mirror.
""")

kitchen = Room("""
The kitchen is heavily used and worn, with blackened ovens and bits of fresh food scrap about the counters. The smells are heavenly.
 """)

host_bedroom = Room("""
A spacious bedroom with a massive bed, a few thick rugs, and an alcove with a window and seats.
""")

hidden_room = Room("""
A dark stone room with wooden shelves filled with glassware and experimental instruments.
""")

# TODO: Rename Guest Rooms to 'Characters' Room and describe accordingly.

guest_room1 = Room("""
A quaint room for guests to lodge comfortably.
""")

guest_room2 = Room("""
A quaint room for guests to lodge comfortably.
""")

guest_room3 = Room("""
A quaint room for guests to lodge comfortably.
""")

guest_room4 = Room("""
A quaint room for guests to lodge comfortably.
""")

guest_room5 = Room("""
A quaint room for guests to lodge comfortably.
""")

guest_hall = Room("""
A short hallway with 3 doors on the left and two on the right.
""")

front_yard = Room("""
Sharply cut hedges line the outer walls of the manor. A circular driveway sweeps across the face of the building.
""")
front_yard.short_descr = 'It is cold out here.'

back_yard = Room("""
An expansive backyard dotted with tall trees stretches before you, all the way to the horizon.
""")

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
guest_hall.connections = {'private': private_hall, 'room1': guest_room1, 'room2': guest_room2, 'room3': guest_room3,
                          'room4': guest_room4, 'room5': guest_room5, }
guest_room1.connections = {'guest': guest_hall}
guest_room2.connections = {'guest': guest_hall}
guest_room3.connections = {'guest': guest_hall}
guest_room4.connections = {'guest': guest_hall}
guest_room5.connections = {'guest': guest_hall}
front_yard.connections = {'foyer': foyer, 'back': back_yard}
back_yard.connections = {'front': front_yard, 'bedroom': host_bedroom}

# TODO: Block Access To Rooms Until Constraints Lifted (Create Items or Dialogue Conditions to Satisfy Constraint)

# Room Constraints / Room Conditions

hidden_room.hidden = True  # The Entrance Is Hidden Until Dialogue Accessed or Item Found
host_bedroom.locked = True
kitchen.preparation = True  # Servants are preparing dinner, so the kitchen is blocked off.
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
guest_room1.chars = Bag()
guest_room2.chars = Bag()
guest_room3.chars = Bag()
guest_room4.chars = Bag()
guest_room5.chars = Bag()


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
guest_room1.items = Bag(room1_items)
guest_room2.items = Bag(room2_items)
guest_room3.items = Bag(room3_items)
guest_room4.items = Bag(room4_items)
guest_room5.items = Bag(room5_items)
