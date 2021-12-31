# Modules

## Introuduction

So far we have covered built-in and customized data and code structures. We will now use those to write our own realistic programs in Python.

You may think of data types as words, expressions and statements as sentences, functions as paragraphs, and modules as chapters.

## The import statement

`import module` is the simplest use of the import statement. Let's write a program that chooses which sport we will play during a school break.

```python
from random import choice
sports = ['ski', 'scuba', 'football', 'baseball', 'soccer']

def random_picker():
    '''
    Returns a random element from the sports list
    '''
    return choice(sports)
```

We will store this into a `sports.py` _module_ and then call the module from `main.py`.

```python
import sports
sport = sports.random_picker()
print(f'We chose to play {sport}')
```

Note that the two files need to be in the same directory.