from random import choice

tips = ['do it', 'don\'t do it', 'maybe do it', 'don\'t panic']
def cookie():
    '''
    Provides random tips
    '''
    return choice(tips)