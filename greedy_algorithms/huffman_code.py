import heapq


class Element:

    __slots__ = ['ch', 'frequency', 'left', 'right', 'parent']

    def __init__(self, ch, freq):
        self.ch = ch
        self.frequency =  freq
        self.left = self.right = self.parent = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def print_tree(root):

    def print_internal(r, space_size=0):
        if r.left:
            print_internal(r.left, space_size=space_size+1)

        print('    ' * space_size, f"{r.ch if r.ch != '' else ''}({r.frequency})")

        if r.right:
            print_internal(r.right, space_size=space_size+1)

    print_internal(root)


def huffman_code(elements):
    heapq.heapify(elements)

    while len(elements) > 1:
        z = Element('', 0)
        x = heapq.heappop(elements)
        print(f"popped: {x.ch if x.ch != '' else 'empty'} / {x.frequency}")
        y = heapq.heappop(elements)
        print(f"popped: {y.ch if y.ch != '' else 'empty'} / {y.frequency}")
        z.left = x
        z.right = y
        z.frequency = x.frequency + y.frequency
        print(f"pushed: {z.frequency}")

        heapq.heappush(elements, z)

    return heapq.heappop(elements)


if __name__ == '__main__':
    characters = ['a', 'b', 'c', 'd', 'e', 'f']
    frequencies = [45, 13, 12, 16, 9, 5]

    print("  i |", end='')
    for i in range(len(characters)):
        print(f"{i:>3}|", end='')
    print('')
    print("char|", end='')
    for ch in characters:
        print(f"{ch:>3}|", end='')
    print('')
    print("freq|", end='')
    for freq in frequencies:
        print(f"{freq:>3}|", end='')
    print('')

    elements = [Element(ch, freq) for ch, freq in zip(characters, frequencies)]

    root = huffman_code(elements)

    print("--- result ---")
    print_tree(root)
