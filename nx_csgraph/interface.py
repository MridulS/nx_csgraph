from .connected import connected_components
from .csgraph import CSGraph

class Dispatcher:
    connected_components = connected_components

    @staticmethod
    def convert(graph, weight=None):
        import networkx as nx
        return CSGraph.from_networkx(graph, weight=weight)