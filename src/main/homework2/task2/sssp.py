from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra


def sssp(m, start):
    matrix = csr_matrix(m)

    return dijkstra(csgraph=matrix, directed=True, indices=start, return_predecessors=False)
