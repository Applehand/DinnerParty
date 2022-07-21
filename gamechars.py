from advlib import *

# Generic Character Properties
Item.greeting = ''
Item.context = ''

party_host = Item('Host', 'Party Host')
party_host.description = 'The host of the party. The reason you are all gathered here.'
party_host.greeting = 'Welcome to the party, friend. Glad you could make it.'
party_host.context = 'host'
