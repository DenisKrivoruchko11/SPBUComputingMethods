from pygraphblas import Matrix, Vector, INT64


def sssp(m, start):
    matrix = Matrix.from_lists(m[0], m[1], m[2])

    result = Vector.sparse(matrix.type, matrix.nrows)
    result[start] = 0

    i = 0
    while i < matrix.nrows:
        result.min_plus(matrix, out=result, accum=INT64.min)
        i += 1

    return result
