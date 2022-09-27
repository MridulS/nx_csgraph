class CSGraph:
    __networkx_plugin__ = "nxcsgraph"
    def __init__(self, csgraph, directed, nodelist):
        self.csgraph = csgraph
        self.directed = directed
        self.nodelist = nodelist
    
    @classmethod
    def from_networkx(cls, graph, weight=None):
        import networkx as nx
        csr = nx.to_scipy_sparse_array(graph, weight=weight)
        directed = True if graph.is_directed() else False
        return cls(csr, directed, list(graph))