import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    # y = np.array(y)
    unique, counts = np.unique(y, return_counts=True)
    proportions = counts / len(y)
    
    # Only sum where p_i > 0 (avoid log(0))
    entropy = 0.0
    for p in proportions:
        if p > 0:
            entropy -= p * np.log2(p)
    
    return entropy