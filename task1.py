class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def reverse(self):
        """Reverse the list in place by changing links between nodes."""
        prev = None
        cur = self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev

    def sort(self):
        """Sort the list in place with merge sort (O(n log n))."""
        self.head = _merge_sort(self.head)

    def to_list(self):
        values = []
        cur = self.head
        while cur:
            values.append(cur.data)
            cur = cur.next
        return values

    def __str__(self):
        return " -> ".join(map(str, self.to_list())) or "(empty)"


def _split(head):
    """Split a chain in two halves with the slow/fast pointer technique."""
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    return head, second


def _merge_nodes(a, b):
    """Merge two sorted node chains by relinking nodes."""
    dummy = tail = Node()
    while a and b:
        if a.data <= b.data:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


def _merge_sort(head):
    if head is None or head.next is None:
        return head
    first, second = _split(head)
    return _merge_nodes(_merge_sort(first), _merge_sort(second))


def merge_sorted_lists(list_a, list_b):
    """Return a new sorted list built from two sorted lists (inputs are kept)."""
    result = LinkedList()
    a, b = list_a.head, list_b.head
    while a or b:
        if b is None or (a is not None and a.data <= b.data):
            result.insert_at_end(a.data)
            a = a.next
        else:
            result.insert_at_end(b.data)
            b = b.next
    return result


def main():
    llist = LinkedList()
    for value in (5, 2, 9, 1, 7, 3):
        llist.insert_at_end(value)
    print("Вихідний список:      ", llist)

    llist.reverse()
    print("Після реверсування:   ", llist)

    llist.sort()
    print("Після сортування:     ", llist)

    other = LinkedList()
    for value in (8, 4, 6, 0):
        other.insert_at_end(value)
    other.sort()
    print("Другий (відсортований):", other)

    merged = merge_sorted_lists(llist, other)
    print("Об'єднаний:           ", merged)


if __name__ == "__main__":
    main()
