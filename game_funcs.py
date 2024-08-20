import pandas as pd
import random
from constants import *
import numpy as np


def determine_outcome(prisoner_a, prisoner_b):
    outcome = 0

    # 0 - A and B remain silent - both 1 yr sentence
    if (prisoner_a['choice'] == prisoner_b['choice']) and (prisoner_a['choice'] != 1):
        outcome = 0
        prisoner_a['sentence'] = 1
        prisoner_b['sentence'] = 1
        # 1 - A against B, B silent, A = 0 sentence  , B - 3 yr sentence
    elif (prisoner_a['choice'] == 1 and prisoner_b['choice'] == 0):
        outcome = 1
        prisoner_a['sentence'] = 0
        prisoner_b['sentence'] = 3
        # 2 - A silent, B against A,  A = 3 sentence, B = 0 sentence
    elif (prisoner_a['choice'] == 0 and prisoner_b['choice'] == 1):
        outcome = 2
        prisoner_b['sentence'] = 0
        prisoner_a['sentence'] = 0
        # 3 - A and B against each other, both  2 years
    elif (prisoner_a['choice'] == 1 and prisoner_b['choice'] == 1):
        outcome = 3
        prisoner_a['sentence'] = 2
        prisoner_b['sentence'] = 2
    return outcome


def play_round(prisoners):
    for prisoner in prisoners:
        prisoner['choice'] = make_choice(prisoner)
    return determine_outcome(prisoners[0], prisoners[1])


def make_choice(prisoner):
    if prisoner['morality'] == 0:
        choice = np.random.choice(POSSIBLE_CHOICES)
    return choice


def adjust_morality(outcome, prisoner):

    if outcome == 1 or outcome == 2:
        prisoner['morality'] -= 1
    if prisoner['morality'] < 0:
        prisoner['morality'] = 0
