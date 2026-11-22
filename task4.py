from min_heap import MinHeap
from tree_node import Node, draw_tree


def heap_to_tree(items):
    """Build a binary tree from a heap array (children of i: 2i+1 and 2i+2)."""
    if not items:
        raise ValueError("Heap is empty")
    nodes = [Node(value) for value in items]
    for index, node in enumerate(nodes):
        left, right = 2 * index + 1, 2 * index + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def draw_heap(heap, title="Бінарна купа"):
    """Visualize a MinHeap (or a plain heap array) as a binary tree."""
    items = heap.to_list() if isinstance(heap, MinHeap) else list(heap)
    draw_tree(heap_to_tree(items), title=title)


def main():
    heap = MinHeap()
    for value in (15, 3, 8, 1, 12, 7, 20, 5, 9, 2):
        heap.push(value)
    print("Масив купи:", heap.to_list())
    draw_heap(heap)


if __name__ == "__main__":
    main()
