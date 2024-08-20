import pandas as pd
import random
from constants import *
from game_funcs import *
import numpy as np
# prisoners dilemma
# trying to keep simple, but leave some flexibility for in the future.
# general flow setup -> play_round() -> make choice() -> determine outcome() -> reset()

# Note, I'm using numerics whenever I can ;force of habit and if I port to something else I won't have to deal with boxing/unboxing/casting
# sentencing!  I keep going back and forth on sentencing and outcome logic being at the same level but i don't see any reason to split it up as the logic is the same.

trials = []

max_trials = 10  # starts to choke on a ham sandwich after 100m or so
for i in range(0, max_trials):
    trial_round = {}
    prisoners = []
    # create the prisoners , it's an array so if needed it can be looped through later.
    for i in range(0, 2):
        prisoners.append({'prisoner_id': i, 'sentence': 0,
                         'choice': 0, 'morality': MORALITY_BASE})
    trial_round['trail_id'] = i
    trial_round['trial_outcome'] = play_round(prisoners)
    trial_round['prisoners'] = prisoners
    print(trial_round)
    trials.append(trial_round)

# didn't want to do this, but it's just temp for getting the data to another file to work on.
pd.DataFrame(trials).to_csv('trial_data.csv', index_label='trial_id')
