import random

def pick_winner(people_dict):
    
    weights = list(people_dict.values())
    names = list(people_dict.keys())
    return random.choices(names,weights)[0]

def pick_n_winners(people_dict, n):
    weights = list(people_dict.values())
    names = list(people_dict.keys())
    return random.choices(names,weights)[0:n]

