from scipy.sparse import tril, csr_matrix


def triangles_count(m):
    matrix = tril(csr_matrix(m))

    return int(matrix.multiply(matrix * matrix).sum())
