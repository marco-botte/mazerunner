from itertools import product

import networkx as nx

from .maze import Maze


class MazeGraph:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.n_rows = self.maze.num_rows
        self.n_cols = self.maze.num_cols
        self.node_idxs = list(product(range(self.n_rows), range(self.n_cols)))
        self.graph = self._graph_from_maze()
        print(list(self.graph.nodes))
        print(list(self.graph.edges))

    def _graph_from_maze(self) -> nx.Graph:
        graph = nx.Graph()
        graph.add_nodes_from(self.node_idxs)
        edges = []
        for x_idx, y_idx in self.node_idxs:
            cell = self.maze.cell(x_idx, y_idx)
            if not cell.has_right_wall:
                edges.append(((x_idx, y_idx), (x_idx + 1, y_idx)))
            if not cell.has_bottom_wall:
                edges.append(((x_idx, y_idx), (x_idx, y_idx + 1)))
        graph.add_edges_from(edges)
        return graph
