import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x_sorted = sorted(np.array(x))
    q= np.array(q)
    n = len(x_sorted)
    results = []
    
    for percentile in q:
        pos = (percentile / 100) * (n - 1)
        lower_idx = int(pos)
        upper_idx = min(lower_idx + 1, n - 1)
        
        if lower_idx == upper_idx:
            results.append(x_sorted[lower_idx])
        else:
            fraction = pos - lower_idx
            value = x_sorted[lower_idx] + fraction * (x_sorted[upper_idx] - x_sorted[lower_idx])
            results.append(value)
    
    return np.array(results)