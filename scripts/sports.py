from random import choice
sports = ['ski', 'scuba', 'football', 'baseball', 'soccer']

def random_picker():
    '''
    Returns a random element from the sports list
    '''
    return choice(sports)