def dfs_util(g, vertice, visitado, result):
    result.append(vertice)
    visitado.add(vertice)

    for vizinho in g[vertice]:
        if vizinho not in visitado:
            dfs_util(g, vizinho, visitado, result)

    return result


def dfs(g, source):
    return dfs_util(g, source, set(), [])
