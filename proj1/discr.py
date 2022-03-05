import random

def prob_suff(*suffixes: str) -> float:
    if isinstance(suffixes[0], list):
        suffixes = (*(suffixes[0]), )
    average_iter = 0
    attemps = 10000
    suf_len = len(max(suffixes, key=len))

    for _ in range(attemps):
        iter: int = 1
        string = ''.join([chr(random.randint(0, 25) + 97) for _ in range(3)])

        while not(string.endswith(suffixes)):
            string = ''.join([chr(random.randint(0, 25) + 97) for _ in range(3)])    
            iter += 1

        average_iter += iter
    
    return 1.0  / (average_iter / attemps)