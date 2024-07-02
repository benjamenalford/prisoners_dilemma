import random
# prisoners dilemma
# trying to keep simple, but leave some flexibility for in the future.
# general flow setup -> play_round() -> make choice() -> determine outcome() -> reset()

# create the prisoners , it's an array so if needed it can be looped through later.
prisoners = []
for i in range(0,2):
    prisoners.append({'prisoner_id': i, 'sentence': 0,'choice':0 })

# Note, I'm using numerics whenever I can ;force of habit and if I port to something else I won't have to deal with boxing/unboxing/casting

# 0 - A and B remain silent - both 1 yr sentence
# 1 - A against B, B silent, A = 0 sentence  , B - 3 yr sentence
# 2 - A silent, B against A,  A = 3 sentence, B = 0 sentence
# 3 - A and B against each other, both  2 years
possible_outcomes = [0,1,2,3]

# 0 - silence
# 1 - rat
possible_choices = [0,1]

# sentencing!  I keep going back and forth on sentencing and outcome logic being at the same level but i don't see any reason to split it up as the logic is the same.
def determine_outcome(prisoner_a, prisoner_b):
    outcome = 0
    if (prisoner_a['choice'] == prisoner_b['choice']) and (prisoner_a['choice'] != 1 ) :
        outcome=0
        prisoner_a['sentence'] = 1
        prisoner_b['sentence'] = 1
    elif (prisoner_a['choice'] == 1 and prisoner_b['choice'] == 0):
        outcome=1
        prisoner_a['sentence'] = 0
        prisoner_b['sentence'] = 3
    elif (prisoner_a['choice'] == 0 and prisoner_b['choice'] == 1):
        outcome =2
        prisoner_b['sentence'] = 0
        prisoner_a['sentence'] = 0
    elif (prisoner_a['choice'] == 1 and prisoner_b['choice'] == 1):
        outcome = 3
        prisoner_a['sentence'] = 2
        prisoner_b['sentence'] = 2
    return outcome

def play_round():
    for prisoner in prisoners:
        prisoner['choice'] = make_choice()
    return determine_outcome(prisoners[0],prisoners[1])

def make_choice():
    choice = random.choice(possible_choices)
    return choice

def reset():
    prisoners = []
    for i in range(0,2):
        prisoners.append({'prisoner_id': i, 'sentence': 0,'choice':0 })

trials = []

max_trials = 1000 # starts to choke on a ham sandwich after 100m or so
for i in range(0,max_trials):
    round = {}
    round['trial_outcome'] = play_round()
    for prisoner in prisoners:
        for key in prisoner: # total hack and testament of laziness. since I'm defining the data as I go, I didn't want to keep coming back here each time I added or removed something from the prisoner ( will be important later)
            round[f'prisoner_{prisoner['prisoner_id']}_{key}'] = prisoner[key] #this is just assuming I'll want the prisoner data later for something
            round[f'prisoner_{prisoner['prisoner_id']}_{key}'] = prisoner[key] #samsies
        round[f'prisoner_{prisoner['prisoner_id']}_{key}'] = prisoners[0]['sentence'] - prisoners[1]['sentence']

    trials.append(round)
    reset()

# didn't want to do this, but it's just temp for getting the data to another file to work on.
import pandas as pd
pd.DataFrame(trials).to_csv('trial_data.csv', index_label='trial_id')