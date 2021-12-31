# Modules

## Introuduction

So far we have covered built-in and customized data and code structures. We will now use those to write our own realistic programs in Python.

You may think of data types as words, expressions and statements as sentences, functions as paragraphs, and modules as chapters.

## The import statement

### Syntax

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

Note that the two files need to be in the same directory. Also note that our module does itself import a function from another module, in the case the `choice` function from the `random` module.

We need to write the name of the module before the function, i.e. `sports.random_picker`; however in the case of `choice` we used it directly. The former approach is safer, but the latter is typical when we foresee no name conflict.

Lastly, the `import random` could have gone inside `random_picker`. This is somewhat subjective: if the imported code is used only within the function, then it is better to import within the function; however, some programmers prefer to put all their imports at the top of the file regardless of that.

### Aliases

We could have imported `sports` with a different name: `import sports as s`. This is helpful when we have conflicts or convoluted module names.

### Restricted import

We often do not need to import all the functions from a module, e.g. with `import choice from random` we are not importing most parts of `choice`, just the ones of our interest. Applying this reasoning, plus an alias, to `main` we get the following.

```python
from sports import random_picker as rp
sport = rp()
print(f'We chose to play {sport}')
```

# Packages

## Basic usage

When we write many modules, storing them all in the same directoy can become confusing. Modules can be organized into file and module hierarchies called _packages_. Think of a package as a subdirectory that contains .py files.

Let's add a module called `scripts` and place two modules in it: `sports` and `fortune_cookie`. You may do it either with the right click or with the linux commands `mkdir` and `cd` in the console. If you are using VSCode, `code` will open a new file in the editor.

```console
mkdir scripts
cd scripts
code fortune_cookie.py
```

```python
from scripts import sports, fortune_cookie
print(f'We chose to play {sports.random_picker()}')
print(f'My advice is {fortune_cookie.cookie()}')
```

Note that you may need to restart your Python kernel in order for the modules to update properly.

If you are using a version of Python earlier than 3.3, you may need to place a file names `__init__.py` in the subdirectory.

Finally, regardless of the IDE you are using, you can always run the `main.py` file from the console.

```console
python3 main.py
```

## Module search path

When we use the `import` command, Python looks in several directories (e.g. where did the `random` module come from?). To know which are those, we can use the `path` list from the `sys` module.

```python
import sys
for directory in sys.path:
    print(directory)
```

There will be white line that corresponds to the current directory, which may or may not be the first in terms of priority.

Also, if there are name conflicts between our own modules (either in the current directory or in a subdirectory) and the Python standard library, we can explicitly call the path of the module with `from subdirectory.module import ...`. If the subdirectory is indeed the current directory, we will do `from . import module` and, if it is the parent directory, `from .. import module`. `.` and `..` is notation borrowed from Unix / Linux.

## Useful packages of the standard library

### Purpose

Python features several packages that we need to import but that are part of the so-called _standard library_.

### `Counter()`

The _collections_ library features the `Counter()` class that counts occurences of items.

```python
from collections import Counter
diet = ['oatmeal', 'oatmeal', 'toast', 'oatmeal', 'oatmeal', 'oatmeal', 'toast']
diet_counter = Counter(diet)
print(diet_counter)
```

`most_common(n)` is a method of this class that provides the `n` most frequent occurences.

```python
diet_counter.most_common(1)
```

Counters can be combined with `+`.

```python
supplemental_diet = ['milk', 'milk', 'banana', 'apple', 'berries', 'toast', 'toast']
supplemental_diet_counter = Counter(supplemental_diet)
diet_counter + supplemental_diet_counter
```

We can subtract one from the other with `-`. Think of this as set operations.

```python
diet_counter - supplemental_diet_counter
```

Common items are obtained with the `&` operator.

```python
diet_counter & supplemental_diet_counter
```

Finally, the union operator `|` provides the items in either one counter or the other.

```python
diet_counter | supplemental_diet_counter
```

### Stack + Queue -> Deque

_Deque_ (pronunced like _deck_) is short for _double-ended queue_. It has features of both a stack and a queue, and useful when adding or deleting items from either end of a sequence. `popleft()` and `pop()` remove the leftmost and rightmost items or the deque, respectively, working from the ends towards the middle. `appendleft()` and `append()` are the corresponding methods to add elements at the endpoints.

Let's practice with the example of a restaurant.

```python
from collections import deque
dq = deque()
# Customers arrive (from the right)
dq.append('Ann')
dq.append('Bob')
dq.append('Charlie')
print(dq)
# Two customers get seated
dq.popleft()
dq.popleft()
print(dq)
# A VIP customer arrives and skips the queue
dq.appendleft('VIP guy')
print(dq)
# The customer that was jumped over gets upset and leaves
dq.pop()
print(dq)
```

### Itertools

`itertools` contains iterator functions that return items when called in a loop, remembering its state between calls.

`chain` runs through its arguments as if they were a single iterable.

```python
import itertools
for i in itertools.chain((1, 'one'), (2, 'two'), (3, 'three')):
    print(i)
```

`cycle` cycles through its arguments infinitely, so we need some control mechanism (for instance a `break` command).

```python
k = 0
for j in itertools.cycle(('one', 'two', 'three')):
    k += 1
    print(j)
    if k > 100:
        break
```

`accumulate()` calculates accumulated values, by default adding them, although it accepts a parameter to calculate e.g. accumulated products.

```python
monthly_sales = (10, 15, 10, 12, 15, 18, 20, 15, 12, 15, 12, 10)
for s in itertools.accumulate(monthly_sales):
    print(s)
```

### Pretty print

`pprint()` stands for _pretty print_ and formats the output a bit more nicely. The difference becomes apparent with long variables.

```python
from pprint import pprint
tuple_ = ((1, 2, 'super loooooong striiiiiiing', 'another extra loooooong string'),
          ('dog', 'cat'),
          ((1, 1, 1), 2, 2, ('looooong string', 'another looooong string')))
print(tuple_)
pprint(tuple_)
```

### Random functions

We have already used `random.choice()`. 

```python
from random import choice
choice(('blue', 'red', 'yellow'))
choice(['one', 'two', 'three'])
choice(range(20))
choice('letters')
```
If we want a sample of more than one element, we need `choices`. Note that these are samples __with__ replacement.

```python
from random import choices
pprint(choices(('blue', 'red', 'yellow'), k=7))
pprint(choices(['one', 'two', 'three'], k=5))
pprint(choices(range(20), k=5))
pprint(choices('letters', k=9))
```

When we want to have samples __without__ replacement we need `sample`.

```python
from random import sample
pprint(sample(('blue', 'red', 'yellow'), 3))
pprint(sample(['one', 'two', 'three'], 2))
pprint(sample(range(20), 5))
pprint(sample('letters', 3))
```

When the sample consists of integers, we can use `randint()` (which includes both endpoints of the interval) or `randrange()` (which does not include the endpoint and which specifies the step).

```python
from random import randint
randint(10, 20)
```

```python
from random import randrange
randrange(10, 20, 5)
```

Finally, for random real numbers between 0 and 1 we use `random()`.

```python
from random import random
random()
```

### Other places to get Python code

Third-party Python code is plentiful, fortunately. Good resources are [PyPy](https://doc.pypy.org/en/latest/) or package-specific official sites such as [the Pandas official site](https://pandas.pydata.org/docs/)
 