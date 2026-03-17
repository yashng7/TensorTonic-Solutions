import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    
    if abs(np.sum(p) - 1.0) > 1e-9:
        raise ValueError("Probabilities must sum to 1")
    
    result = np.sum(x * p)
    return int(result) if result == int(result) else result
