class Element:

    def __init__(self, is_leaf=True):
        self.n = 0
        self.keys = []
        self.is_leaf = is_leaf
        self.children = []


class Tree:

    def __init__(self, min_degree=2):
        self.root = Element()
        self.min_degree = min_degree

    def insert(self, key):
        r = self.root
        if r.n == 2 * self.min_degree - 1:
            s = Element(is_leaf=False)
            s.children.insert(0, r)
            self.root = s

            self.__split_child(s, 0)

            self.__insert_non_full(s, key)
        else:
            self.__insert_non_full(r, key)

    def __insert_non_full(self, x, key):
        i = x.n - 1
        if x.is_leaf:
            while i >= 0 and x.keys[i] > key:
                i -= 1

            x.keys.insert(i + 1, key)
            x.n += 1
        else:
            while i >= 0 and x.keys[i] > key:
                i -= 1

            i += 1

            if x.children[i].n == 2 * self.min_degree - 1:
                self.__split_child(x, i)

                if x.keys[i] < key:
                    i += 1

            self.__insert_non_full(x.children[i], key)

    def __split_child(self, x, i):
        y = x.children[i]
        z = Element()

        key_to_up = y.keys[self.min_degree - 1]
        z.keys = y.keys[self.min_degree:]
        z.n = len(z.keys)
        z.is_leaf = y.is_leaf
        y.keys = y.keys[:self.min_degree - 1]
        y.n = len(y.keys)

        if not y.is_leaf:
            z.children = y.children[self.min_degree:]
            y.children = y.children[:self.min_degree]

        x.keys.insert(i, key_to_up)
        x.n += 1
        x.children.insert(i + 1, z)

    def print_tree(self):

        def print_tree_internal(r, space_size=0):
            print('  ' * space_size, r.keys)

            if not r.is_leaf:
                for c in r.children:
                    print_tree_internal(c, space_size=space_size + 1)

        print_tree_internal(self.root)


if __name__ == '__main__':
    t = Tree()

    while True:
        print("1:insert 2:remove 3:print > ", end='')
        op = int(input())

        if op == 1:
            print("input key > ", end='')
            key = int(input())

            t.insert(key)
        elif op == 2:
            pass
        elif op == 3:
            t.print_tree()
        else:
            print("invalid operation")