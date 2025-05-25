class Element:

    __slots__ = ['data', 'next']

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    __slots__ = ['head', 'tail']

    def __init__(self):
        self.head = self.tail = None

    def make_set(self, e):
        self.head = self.tail = e

    def union(self, x, y):
        x.tail.next = y.head
        x.tail = y.tail

    def print_set(self):
        p = self.head
        while p:
            print(p.data, end=' -> ' if p.next else '\n')

            p = p.next


if __name__ == '__main__':
    disjoint_set = {}
    disjoint_set['a'] = LinkedList()
    disjoint_set['b'] = LinkedList()
    disjoint_set['c'] = LinkedList()
    disjoint_set['d'] = LinkedList()
    disjoint_set['e'] = LinkedList()
    disjoint_set['f'] = LinkedList()
    disjoint_set['g'] = LinkedList()
    disjoint_set['h'] = LinkedList()
    disjoint_set['i'] = LinkedList()
    disjoint_set['j'] = LinkedList()

    for k, v in disjoint_set.items():
        v.make_set(Element(k))

    for v in disjoint_set.values():
        v.print_set()

    print("union b and d")
    disjoint_set['b'].union(disjoint_set['b'], disjoint_set['d'])
    disjoint_set['b'].print_set()
    del disjoint_set['d']
    print("union e and g")
    disjoint_set['e'].union(disjoint_set['e'], disjoint_set['g'])
    disjoint_set['e'].print_set()
    del disjoint_set['g']
    print("union a and c")
    disjoint_set['a'].union(disjoint_set['a'], disjoint_set['c'])
    disjoint_set['a'].print_set()
    del disjoint_set['c']
    print("union h and i")
    disjoint_set['h'].union(disjoint_set['h'], disjoint_set['i'])
    disjoint_set['h'].print_set()
    del disjoint_set['i']
    print("union a and b")
    disjoint_set['a'].union(disjoint_set['a'], disjoint_set['b'])
    disjoint_set['a'].print_set()
    del disjoint_set['b']
    print("union e and f")
    disjoint_set['e'].union(disjoint_set['e'], disjoint_set['f'])
    disjoint_set['e'].print_set()
    del disjoint_set['f']
