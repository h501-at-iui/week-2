import numpy as np


# update/add code below ...

def ways(n):
    # number of ways = number of valid nickels (0 to n//5) + 1
    return n // 5 + 1

import numpy as np

def lowest_score(names, scores):
    scores = np.array(scores)
    idx = np.argmin(scores)  # index of lowest score
    return names[idx]

def sort_names(names, scores):
    scores = np.array(scores)
    idx = np.argsort(scores)[::-1]  # descending order
    return [names[i] for i in idx]
