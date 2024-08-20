import json
import pandas as pd
import random
from constants import *
from game_funcs import *
import numpy as np

trials = []
df = pd.read_csv('trial_data.csv')
max_trials = 10  # len(df)-1
print(df.columns)
# for index, key in df.iterrows():
#     print(pd.DataFrame([key['prisoner_0']])[0])
# trial_round = {}
# print(df.loc[i]['prisoner_0'])
# prisoners = [df.loc[i], df.loc[i]]
# trial_round['trail_id'] = i + max_trials

# trial_round['trial_outcome'] = play_round(prisoners)
# for prisoner in prisoners:
#     prisoner['morality'] = adjust_morality(
#         trial_round['trial_outcome'], prisoner)
#     trial_round['prisoner_' + str(prisoner['prisoner_id'])] = prisoner
# trial_round['prisoners'] = prisoners
# print(trial_round)
# trials.append(trial_round)

# didn't want to do this, but it's just temp for getting the data to another file to work on.
# pd.DataFrame(trials).to_csv('trial_data.csv', index_label='trial_id')
