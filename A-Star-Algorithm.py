def aStar(startNode, stopNode):
    openSet = set(startNode)
    closedSet = set()
    g = {startNode: 0}
    parents = {startNode: startNode}

    while len(openSet) > 0:
        n = None
        for v in openSet:
            if n is None or g[v] + 