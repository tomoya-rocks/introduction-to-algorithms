import heapq


class Element:

    __slots__ = ['ch', 'count', 'left', 'right']

    def __init__(self, ch='', count=0):
        self.ch = ch
        self.count = count
        self.left = self.right = None

    def __lt__(self, other):
        return self.count < other.count

    def __str__(self):
        return f"{self.ch} ({self.count})"


def huffman(characters):
    heapq.heapify(characters)

    while len(characters) > 1:
        z = Element()
        x = heapq.heappop(characters)
        y = heapq.heappop(characters)
        z.count = x.count + y.count
        z.left = x
        z.right = y

        heapq.heappush(characters, z)

    return heapq.heappop(characters)


def print_tree(root):

    def print_tree_internal(r, space_size=0):
        if r.left:
            print_tree_internal(r.left, space_size=space_size + 1)

        print('    ' * space_size, r)

        if r.right:
            print_tree_internal(r.right, space_size=space_size + 1)

    print_tree_internal(root)


if __name__ == '__main__':
    characters = [
        Element(ch='a', count=45),
        Element(ch='b', count=13),
        Element(ch='c', count=12),
        Element(ch='d', count=16),
        Element(ch='e', count=9),
        Element(ch='f', count=5)
    ]

    print(" ch |", end='')
    for e in characters:
        print(f"{e.ch:^3}|", end='')
    print('')
    print("  n |", end='')
    for e in characters:
        print(f"{e.count:^3}|", end='')
    print('')

    root = huffman(characters)

    print("--- result ---")
    print_tree(root)
