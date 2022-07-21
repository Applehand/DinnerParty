from advlib import *

# TODO: Add Details, Dialogue Options, and Contexts for Characters

# Create Player/NPC Attributes
player_health = 10
host_health = 15


# Generic Character Properties
Item.greeting = ''
Item.context = ''
Item.dialogue_options = {'option1': ''}

# Character - The Host

party_host = Item('Host', 'Party Host')
party_host.description = 'The host of the party. The reason you are all gathered here tonight.'
party_host.greeting = 'Welcome to the party, friend. Glad you could make it.'
party_host.context = 'host'
party_host.dialogue_options = {'option1': 'This is your first dialogue option.',
                               'option2': 'This is your second dialogue option.'}

# Character - The Graceful Elder

the_elder = Item('Elder', 'Old Woman')


# Character - The Grizzled General

the_general = Item('General', 'Soldier')


# Character - The Young Debutante

the_debutante = Item('Debutante', 'Young Woman')


# Character - The Cheery Fool

the_fool = Item('Fool', 'Idiot')


# Character - The Intellectual Noble

the_noble = Item('Noble', 'Intellectual')



