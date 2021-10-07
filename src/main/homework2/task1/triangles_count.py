from pygraphblas import Matrix


def triangles_count(m):
    matrix = Matrix.from_lists(m[0], m[1], m[2]).tril()
    return matrix.mxm(matrix, mask=matrix).reduce_int()
