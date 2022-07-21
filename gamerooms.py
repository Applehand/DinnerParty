from advlib import *
import gameitems, gamechars

# Room Definitions
main_hall = Room("""
A long, crimson carpet extends the length of the main hall. 
""")
main_hall.context = 'main hall'


foyer = Room("""
Soft benches line one side of the foyer, with tall cabinets on the other.
""")

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

# Room Connections / Room Layout
room_keys = ['main', 'foyer', 'showroom', 'sitting', 'dining', 'private', 'kitchen', 'bedroom', 'hidden',
             'guest', 'room1', 'room2', 'room3', 'room4', 'room5']

foyer.connections = {'main': main_hall}
main_hall.connections = {'foyer': foyer, 'showroom': grand_showroom, 'private': private_hall, 'dining': dining_room,
                         'sitting': sitting_room}
grand_showroom.connections = {'main': main_hall}
sitting_room.connections = {'main': main_hall, 'dining': dining_room}
dining_room.connections = {'main': main_hall, 'sitting': sitting_room, 'kitchen': kitchen}
private_hall.connections = {'main': main_hall, 'guest': guest_hall, 'kitchen': kitchen, 'bedroom': host_bedroom}
kitchen.connections = {'private': private_hall, 'dining': dining_room}
host_bedroom.connections = {'private': private_hall, 'hidden': hidden_room}
hidden_room.connections = {'bedroom': host_bedroom}
guest_hall.connections = {'private': private_hall, 'room1': guest_room1, 'room2': guest_room2, 'room3': guest_room3,
                          'room4': guest_room4, 'room5': guest_room5, }
guest_room1.connections = {'guest': guest_hall}
guest_room2.connections = {'guest': guest_hall}
guest_room3.connections = {'guest': guest_hall}
guest_room4.connections = {'guest': guest_hall}
guest_room5.connections = {'guest': guest_hall}


# Room Constraints / Room Conditions

hidden_room.hidden = True
host_bedroom.locked = True

# Place Characters In Initial Room

foyer.chars_in_room.add(gamechars.party_host)

# Place Items In Initial Room
foyer.items_in_room.add(gameitems.cane)
foyer.items_in_room.add(gameitems.gun)