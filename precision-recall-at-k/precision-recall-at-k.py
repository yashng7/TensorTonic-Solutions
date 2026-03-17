import numpy as np
def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    recommended = np.array(recommended)
    relevant = np.array(relevant)
    top_k = recommended[:k]
    relevant_set = set(relevant)
    hits = np.sum(np.isin(top_k, list(relevant_set)))
    precision_k = hits / k if k > 0 else 0
    recall_k = hits / len(relevant) if len(relevant) > 0 else 0
    return [precision_k, recall_k]