import uuid

import matplotlib.pyplot as plt
import networkx as nx

DEFAULT_COLOR = "skyblue"


class Node:
    def __init__(self, key, color=DEFAULT_COLOR):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Node fill color, used when drawing
        self.id = str(uuid.uuid4())  # Unique identifier for every node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Fill the networkx graph and the positions dict from a binary tree."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title=None, ax=None, node_size=2500):
    """Draw a binary tree. Draws on `ax` if given, otherwise opens a window."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [data["color"] for _, data in tree.nodes(data=True)]
    labels = {node_id: data["label"] for node_id, data in tree.nodes(data=True)}

    standalone = ax is None
    if standalone:
        plt.figure(figsize=(8, 5))
        ax = plt.gca()
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=node_size, node_color=colors, ax=ax)
    if title:
        ax.set_title(title)
    if standalone:
        plt.show()
