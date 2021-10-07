from igraph import Graph


def triangles_count(m):
    matrix = Graph.Adjacency(m)

    return len(matrix.cliques(3, 3))
