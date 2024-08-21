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

max_trials = 1000  # starts to choke on a ham sandwich after 100m or so
for i in range(1, max_trials):
    trial_round = {}
    prisoners = []
    # create the prisoners , it's an array so if needed it can be looped through later.
    for j in range(0, 2):
        prisoners.append({'prisoner_id': j, 'sentence': 0,
                         'choice': 0, 'morality': MORALITY_BASE})
    trial_round['trial_id'] = i
    trial_round['trial_outcome'] = play_round(prisoners)
    for prisoner in prisoners:
        prisoner['morality'] = adjust_morality(
            trial_round['trial_outcome'], prisoner)
        trial_round['prisoner_' + str(prisoner['prisoner_id'])] = prisoner
    trial_round['prisoners'] = prisoners
    # print(trial_round)
    trials.append(trial_round)

# didn't want to do this, but it's just temp for getting the data to another file to work on.
pd.DataFrame(trials).to_json('trial_data.json', orient='records')
