from advlib import *

# TODO: Add Details, Dialogue Options, and Contexts for Characters

# Create Player/NPC Attributes
player_health = 10
host_health = 15
elder_health = 4
general_health = 12
debutante_health = 8
fool_health = 10
noble_health = 10


# Generic Character Properties
Item.greeting = ''
Item.context = ''
Item.dialogue_options = {'option1': ''}


# Character - The Host

party_host = Item('Host', 'Party Host')
party_host.description = 'The host of the party. The reason you are all gathered here tonight.'
party_host.greeting = 'Welcome to the party. Looks like you are the last to arrive - glad you could make it.'
party_host.context = 'host'
party_host.dialogue_options = {'option1': 'This is your first dialogue option.',
                               'option2': 'This is your second dialogue option.'}

# Character - The Graceful Elder

the_elder = Item('Elder', 'Old Woman')
the_elder.description = 'A small, quiet old lady. She is quick for her age.'
the_elder.greeting = ''
the_elder.context = 'elder'
the_elder.dialogue_options = {}


# Character - The Grizzled General

the_general = Item('General', 'Soldier')
the_general.description = 'A loud, old veteran who prefers staying in his comfy seat.'
the_general.greeting = ''
the_general.context = 'general'
the_general.dialogue_options = {}

# Character - The Young Debutante

the_debutante = Item('Debutante', 'Young Woman')
the_debutante.description = 'A charming young woman with an eye for self-doubt.'
the_debutante.greeting = ''
the_debutante.context = 'debutante'
the_debutante.dialogue_options = {}

# Character - The Cheery Fool

the_fool = Item('Fool', 'Idiot')
the_fool.description = 'A happy idiot who never realizes the gravity of a situation. Incapable of reading the room.'
the_fool.greeting = ''
the_fool.context = 'fool'
the_fool.dialogue_options = {}

# Character - The Intellectual Noble

the_noble = Item('Noble', 'Intellectual')
the_noble.description = 'A confident middle-aged man who wears expensive clothes and uses a lot of words to say little.'
the_noble.greeting = ''
the_noble.context = 'noble'
the_noble.dialogue_options = {}


