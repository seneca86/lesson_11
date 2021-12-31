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
