from pygraphblas import Matrix, Vector, UINT8, BOOL, descriptor


def bfs(m, start):
    matrix = Matrix.from_lists(m[0], m[1], m[2])
    result = Vector.sparse(UINT8, matrix.nrows)
    q = Vector.sparse(BOOL, matrix.nrows)

    q[start] = True
    level = 1

    while q.reduce_bool() and level <= matrix.nrows:
        result.assign_scalar(level, mask=q)
        result.vxm(matrix, mask=result, out=q, desc=descriptor.RC)
        level += 1

    return result


"""A = Matrix.from_lists(
    [0, 0, 1, 3, 3, 4, 1, 5],
    [1, 3, 2, 4, 5, 2, 5, 4],
    [1, 1, 1, 1, 1, 1, 1, 1])"""