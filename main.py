# %%
import sports
# %%
sport = sports.random_picker()
print(f'We chose to play {sport}')
# %%
from sports import random_picker as rp
# %%
sport = rp()
print(f'We chose to play {sport}')
# %%
from scripts import sports, fortune_cookie
print(f'We chose to play {sports.random_picker()}')
print(f'My advice is {fortune_cookie.cookie()}')
# %%
import sys
for directory in sys.path:
    print(directory)
# %%
# %%
from collections import Counter
diet = ['oatmeal', 'oatmeal', 'toast', 'oatmeal', 'oatmeal', 'oatmeal', 'toast']
diet_counter = Counter(diet)
print(diet_counter)
# %%
diet_counter.most_common(1)
# %%
supplemental_diet = ['milk', 'milk', 'banana', 'apple', 'berries', 'toast', 'toast']
supplemental_diet_counter = Counter(supplemental_diet)
diet_counter + supplemental_diet_counter
# %%
diet_counter - supplemental_diet_counter
# %%
diet_counter & supplemental_diet_counter
# %%
diet_counter | supplemental_diet_counter
# %%
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
# %%
import itertools
for i in itertools.chain((1, 'one'), (2, 'two'), (3, 'three')):
    print(i)
# %%
k = 0
for j in itertools.cycle(('one', 'two', 'three')):
    k += 1
    print(j)
    if k > 100:
        break
# %%
monthly_sales = (10, 15, 10, 12, 15, 18, 20, 15, 12, 15, 12, 10)
for s in itertools.accumulate(monthly_sales):
    print(s)
# %%
from pprint import pprint
tuple_ = ((1, 2, 'super loooooong striiiiiiing', 'another extra loooooong string'),
          ('dog', 'cat'),
          ((1, 1, 1), 2, 2, ('looooong string', 'another looooong string')))
print(tuple_)
pprint(tuple_)
# %%
from random import choice
choice(('blue', 'red', 'yellow'))
choice(['one', 'two', 'three'])
choice(range(20))
choice('letters')
# %%
from random import sample
pprint(sample(('blue', 'red', 'yellow'), 3))
pprint(sample(['one', 'two', 'three'], 2))
pprint(sample(range(20), 5))
pprint(sample('letters', 3))
# %%
from random import choices
pprint(choices(('blue', 'red', 'yellow'), k=7))
pprint(choices(['one', 'two', 'three'], k=5))
pprint(choices(range(20), k=5))
pprint(choices('letters', k=9))
# %%
from random import randint
randint(10, 20)
# %%
from random import randrange
randrange(10, 20, 5)
# %%
from random import random
random()
# %%
