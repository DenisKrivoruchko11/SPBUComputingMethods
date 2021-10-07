from igraph import Graph


def sssp(m, start):
    matrix = Graph.Weighted_Adjacency(m)

    return matrix.shortest_paths(start, weights=matrix.es["weight"])[0]
