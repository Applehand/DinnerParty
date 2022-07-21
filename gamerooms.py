from advlib import *
import gameitems, gamechars

# Room Definitions
main_hall = Room("""
A long, crimson carpet extends the length of the main hall. 
""")

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
A small connective hall joining many rooms, with a few tables, decorations, and a mirror.
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

spying_room1 = Room("""
A small room for spying on the guest rooms.
""")

spying_room2 = Room("""
A small room for spying on the guest rooms.
""")

spying_room3 = Room("""
A small room for spying on the guest rooms.
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
A small room with a hallway with the guest room doors on either side.
""")

# Room Connections / Room Layout
room_keys = ['main', 'foyer', 'showroom', 'sitting', 'dining', 'private', 'kitchen', 'bedroom', 'hidden', 'guesthall',
             'room1', 'room2', 'room3', 'room4', 'room5']
foyer.connections = {'main': main_hall}
main_hall.connections = {'foyer': foyer, 'showroom': grand_showroom}
grand_showroom.connections = {'main': main_hall}
sitting_room.connections = {}
dining_room.connections = {}
private_hall.connections = {}
kitchen.connections = {}
host_bedroom.connections = {}
hidden_room.connections = {}
guest_hall.connections = {}
guest_room1.connections = {'guesthall': guest_hall}
guest_room2.connections = {'guesthall': guest_hall}
guest_room3.connections = {'guesthall': guest_hall}
guest_room4.connections = {'guesthall': guest_hall}
guest_room5.connections = {'guesthall': guest_hall}


# Room Constraints / Room Conditions

# Place Characters In Initial Room

foyer.chars_in_room.add(gamechars.party_host)

# Place Items In Initial Room
foyer.items_in_room.add(gameitems.cane)