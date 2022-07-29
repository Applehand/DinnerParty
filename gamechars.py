from gameitems import *


# TODO: Add Details, Dialogue Options, for Characters

# Create Player/NPC Attributes


# Generic Character Properties

Item.greeting = ''
Item.context = ''
Item.dialogue_options = {'option1': ''}

# Character - The Host

the_host = Item('The Host', 'Party Host')
the_host.description = 'The host of the party. The reason you are all gathered here tonight.'
the_host.greeting = 'Welcome to the party. Looks like you are the last to arrive - glad you could make it.'
the_host.context = 'host'
the_host.dialogue_options = {'option1': 'What a wonderful home you have, sir. Thank you for the invite.',
                             'option2': "Glad to be here, but why did you invite me?",
                             'option3': "I'm just here to see the sculptures.",
                             'option4': "I've come to kill! (You laugh maniacally)"}
the_host.dialogue_responses = {'response1': 'Oh thank you, my family built this house.',
                               'response2': "I always invite the people to come see the wonders of our world!",
                               'response3': 'Well.. the sculptures are magnificent!',
                               'response4': "Kill..?"}
the_host.animate = True

# Character - The Graceful Elder

the_elder = Item('The Elder', 'Old Woman')
the_elder.description = 'A small, quiet old lady. She is quick for her age.'
the_elder.greeting = ''
the_elder.context = 'elder'
the_elder.dialogue_options = {'option1': 'This is your first dialogue option.',
                              'option2': 'This is your second dialogue option.',
                              'option3': 'This is your third option.',
                              'option4': 'This is your fourth option.'}
the_elder.dialogue_responses = {'response1': "1",
                                'response2': "2",
                                'response3': "3",
                                'response4': "4"}
the_elder.animate = True

# Character - The Grizzled General

the_general = Item('The General', 'Soldier')
the_general.description = 'A loud, old veteran who prefers staying in his comfy seat.'
the_general.greeting = ''
the_general.context = 'general'
the_general.dialogue_options = {'option1': 'This is your first dialogue option.',
                                'option2': 'This is your second dialogue option.',
                                'option3': 'This is your third option.',
                                'option4': 'This is your fourth option.'}
the_general.dialogue_responses = {'response1': "1",
                                  'response2': "2",
                                  'response3': "3",
                                  'response4': "4"}
the_general.animate = True

# Character - The Young Debutante

the_debutante = Item('The Debutante', 'Young Woman')
the_debutante.description = 'A charming young woman with an eye for self-doubt.'
the_debutante.greeting = ''
the_debutante.context = 'debutante'
the_debutante.dialogue_options = {'option1': 'This is your first dialogue option.',
                                  'option2': 'This is your second dialogue option.',
                                  'option3': 'This is your third option.',
                                  'option4': 'This is your fourth option.'}
the_debutante.dialogue_responses = {'response1': "1",
                                    'response2': "2",
                                    'response3': "3",
                                    'response4': "4"}
the_debutante.animate = True

# Character - The Cheery Fool

the_fool = Item('The Fool', 'Idiot')
the_fool.description = 'A happy idiot who never realizes the gravity of a situation. Incapable of reading the room.'
the_fool.greeting = ''
the_fool.context = 'fool'
the_fool.dialogue_options = {'option1': 'This is your first dialogue option.',
                             'option2': 'This is your second dialogue option.',
                             'option3': 'This is your third option.',
                             'option4': 'This is your fourth option.'}
the_fool.dialogue_responses = {'response1': "1",
                               'response2': "2",
                               'response3': "3",
                               'response4': "4"}
the_fool.animate = True

# Character - The Intellectual Noble

the_noble = Item('The Noble', 'Intellectual')
the_noble.description = 'A confident middle-aged man who wears expensive clothes and uses a lot of words to say little.'
the_noble.greeting = ''
the_noble.context = 'noble'
the_noble.dialogue_options = {'option1': 'This is your first dialogue option.',
                              'option2': 'This is your second dialogue option.',
                              'option3': 'This is your third option.',
                              'option4': 'This is your fourth option.'}
the_noble.dialogue_responses = {'response1': "1",
                                'response2': "2",
                                'response3': "3",
                                'response4': "4"}
the_noble.animate = True

# Character - Galatea

galatea = Item('Galatea', 'Sculpture', 'Bust', 'Head')
galatea.description = 'A rough stone sculpture of a face.'
galatea.greeting = ''
galatea.context = 'noble'
galatea.dialogue_options = {'option1': 'This is your first dialogue option.',
                            'option2': 'This is your second dialogue option.',
                            'option3': 'This is your third option.',
                            'option4': 'This is your fourth option.'}
galatea.dialogue_responses = {'response1': "1",
                              'response2': "2",
                              'response3': "3",
                              'response4': "4"}
galatea.animate = True

# Create Personal Inventories (Pockets) For Characters

player_inventory = Bag()
the_host.pockets = Bag(host_personal_items)
the_elder.pockets = Bag(elder_personal_items)
the_general.pockets = Bag(general_personal_items)
the_debutante.pockets = Bag(debutante_personal_items)
the_fool.pockets = Bag(fool_personal_items)
the_noble.pockets = Bag(noble_personal_items)
galatea.pockets = Bag(galatea_personal_items)
