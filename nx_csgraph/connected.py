from scipy.sparse import csgraph
from collections import defaultdict

def connected_components(graph):
    if graph.directed == True:
        raise ValueError
    n_components, labels = csgraph.connected_components(csgraph=graph.csgraph, 
                                                        directed=graph.csgraph, 
                                                        return_labels=True)
    dd = defaultdict(set)
    for i, j in zip(labels, graph.nodelist):
        dd[i].add(j)
    for i in dd:
        yield dd[i]
