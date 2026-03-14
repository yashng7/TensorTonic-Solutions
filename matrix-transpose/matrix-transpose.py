import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A, dtype=float)
    n, m = A.shape
    transposed = np.zeros((m, n))

    for i in range(n):
        for j in range(m):
            transposed[j][i] = A[i][j]
    return transposed
    

