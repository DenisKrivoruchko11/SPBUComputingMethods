from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import breadth_first_order


def bfs(m, start):
    matrix = csr_matrix(m)

    return breadth_first_order(matrix, start, directed=True)[0]


"""X = csr_matrix([
    [0, 1, 0, 9, 0],
    [3, 0, 3, 0, 0],
    [0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]])"""
