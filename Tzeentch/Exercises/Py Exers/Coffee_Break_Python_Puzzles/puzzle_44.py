#############################
## id 274
## Puzzle Elo 1729
## Correctly solved 44 %
#############################

def has_path(graph, v_start, v_end, path_len=0):
    '''Graph has path from v_start to v_end'''

    # Traverse each vertex only once
    if path_len >= len(graph):
        return False

    # Direct path from v_start to v_end?
    if graph[v_start][v_end]:
        return True

    # Indirect path via neighbor v_nbor?
    for v_nbor, edge in enumerate(graph[v_start]):
        if edge: # between v_start and v_nbor
            if has_path(graph, v_nbor, v_end, path_len + 1):
                return True

    return False

# The graph represented as adjancy matrix
G = [[1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 1, 1, 1, 0],
     [1, 0, 0, 1, 1]]
print(has_path(graph=G, v_start=3, v_end=0))
