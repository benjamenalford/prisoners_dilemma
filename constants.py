# 0 - A and B remain silent - both 1 yr sentence
# 1 - A against B, B silent, A = 0 sentence  , B - 3 yr sentence
# 2 - A silent, B against A,  A = 3 sentence, B = 0 sentence
# 3 - A and B against each other, both  2 years
POSSIBLE_OUTCOMES = [0, 1, 2, 3]
OUTCOME_MAP = {
    0: "Silence",
    1: "A Rat B",
    2: "B Rat A",
    3: "Both Against",
}

# 0 - silence
# 1 - rat
POSSIBLE_CHOICES = [0, 1]
CHOICE_MAP = {
    0: "Silence",
    1: "Rat"
}
# morality
# -1 to 1 #-1 being immoral, 1 being morally
MORALITY_BASE = .5
MORALITY_MIN = 1
MORALITY_MAX = -1
