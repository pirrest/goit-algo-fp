from collections import deque

import matplotlib.pyplot as plt

from min_heap import MinHeap
from task4 import heap_to_tree
from tree_node import DEFAULT_COLOR, draw_tree

DARK = (18, 30, 90)
LIGHT = (190, 225, 255)


def gradient_colors(count):
    """Return `count` hex RGB colors going from dark to light shades."""
    colors = []
    for i in range(count):
        t = i / (count - 1) if count > 1 else 0
        rgb = (round(d + (l - d) * t) for d, l in zip(DARK, LIGHT))
        colors.append("#{:02X}{:02X}{:02X}".format(*rgb))
    return colors


def dfs_order(root):
    """Iterative depth-first traversal using a stack."""
    order, stack = [], [root]
    while stack:
        node = stack.pop()
        order.append(node)
        # Push right first so the left child is visited first.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def bfs_order(root):
    """Iterative breadth-first traversal using a queue."""
    order, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def visualize_traversal(root, order, name):
    """Show one subplot per step; visited nodes get colors dark -> light."""
    colors = gradient_colors(len(order))
    all_nodes = dfs_order(root)
    cols = 4
    rows = -(-len(order) // cols)
    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 3 * rows))
    axes = axes.flatten()

    for node in all_nodes:
        node.color = DEFAULT_COLOR
    for step, node in enumerate(order):
        node.color = colors[step]
        draw_tree(root, title=f"Крок {step + 1}: {node.val} ({colors[step]})",
                  ax=axes[step], node_size=600)
    for ax in axes[len(order):]:
        ax.axis("off")

    fig.suptitle(name)
    plt.tight_layout()
    plt.show()


def main():
    heap = MinHeap()
    for value in (15, 3, 8, 1, 12, 7, 20, 5, 9, 2):
        heap.push(value)
    root = heap_to_tree(heap.to_list())

    for name, traverse in (("Обхід у глибину (DFS, стек)", dfs_order),
                           ("Обхід у ширину (BFS, черга)", bfs_order)):
        order = traverse(root)
        print(f"{name}: {[node.val for node in order]}")
        visualize_traversal(root, order, name)


if __name__ == "__main__":
    main()
