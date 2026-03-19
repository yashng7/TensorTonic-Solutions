import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    a, b = list(rater1), list(rater2)
    if len(a) != len(b):
        raise ValueError("Equal length required")

    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    freq_a = {}
    freq_b = {}
    for x in a:
        freq_a[x] = freq_a.get(x, 0) + 1
    for x in b:
        freq_b[x] = freq_b.get(x, 0) + 1
    pe = sum((freq_a.get(l, 0) / n) * (freq_b.get(l, 0) / n) for l in set(a) | set(b))

    return 1.0 if pe == 1.0 else (po - pe) / (1 - pe)