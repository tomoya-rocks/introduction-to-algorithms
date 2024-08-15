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

    def search(self, key):

        def search_internal(r, key):
            i = 0
            while i < r.n and r.keys[i] < key:
                i += 1

            if i < r.n and key == r.keys[i]:
                return r
            else:
                if r.is_leaf:
                    return None
                else:
                    return search_internal(r.children[i], key)

        return search_internal(self.root, key)

    def remove(self, key):

        def remove_internal(x, key):
            i = 0
            while i < x.n and x.keys[i] < key:
                i += 1

            if i < x.n and x.keys[i] == key:
                if x.is_leaf:
                    # case 1
                    x.keys.pop(i)
                    x.n -= 1
                else:
                    if x.children[i].n >= self.min_degree:
                        # case 2 - a
                        y = x.children[i]
                        key_to_up = y.keys[-1]

                        x.keys[i] = key_to_up

                        y.keys = y.keys[:-1]
                        y.n -= 1
                    elif x.children[i + 1].n >= self.min_degree:
                        # case 2 - b
                        z = x.children[i + 1]
                        key_to_up = z.keys[0]

                        x.keys[i] = key_to_up

                        z.keys = z.keys[1:]
                        z.n -= 1
                    else:
                        # case 2 - c
                        y = x.children[i]
                        z = x.children[i + 1]

                        y.keys += x.keys
                        y.n += 1
                        y.keys += z.keys
                        y.n += z.n

                        if not y.is_leaf:
                            y.children += z.children

                        x.keys.pop(i)
                        x.n -= 1
                        x.children.pop(i + 1)

                        if x.n == 0:
                            self.root = y

                        remove_internal(y, key)
            else:
                if x.children[i].n == self.min_degree - 1:
                    if i >= 1 and x.children[i - 1].n >= self.min_degree:
                        # case 3 - a - (1)
                        y = x.children[i]
                        z = x.children[i - 1]

                        key_to_up = z.keys[-1]
                        z.keys.pop(-1)
                        z.n -= 1

                        key_to_down = x.keys[i - 1]
                        x.keys[i - 1] = key_to_up

                        y.keys.insert(0, key_to_down)
                        y.n += 1

                        if not y.is_leaf:
                            y.children.append(z.children[:-1])
                            z.children.pop(-1)

                        remove_internal(x.children[i], key)
                    elif i < x.n and x.children[i + 1].n >= self.min_degree:
                        # case 3 - a - (2)
                        y = x.children[i]
                        z = x.children[i + 1]

                        key_to_up = z.keys[0]
                        z.keys.pop(0)
                        z.n -= 1

                        key_to_down = x.keys[i]
                        x.keys[i] = key_to_up

                        y.keys.append(key_to_down)
                        y.n += 1

                        if not y.is_leaf:
                            y.children.insert(-1, z.children[0])
                            z.children.pop(0)

                        remove_internal(x.children[i], key)
                    elif i >= 1 and x.children[i - 1].n == self.min_degree - 1:
                        # case 3 - b - (1)
                        y = x.children[i]
                        z = x.children[i - 1]

                        key_to_down = x.keys[i - 1]

                        z.keys.append(key_to_down)
                        z.n += 1
                        z.keys.extend(y.keys)
                        z.n += y.n

                        if not z.is_leaf:
                            z.children.extend(y.children)

                        x.keys.pop(i - 1)
                        x.n -= 1
                        if x.n == 0:
                            self.root = z
                        x.children.pop(i)

                        remove_internal(z, key)
                    elif i < x.n and x.children[i + 1].n == self.min_degree - 1:
                        y = x.children[i]
                        z = x.children[i + 1]

                        key_to_down = x.keys[i]

                        y.keys.append(key_to_down)
                        y.n += 1
                        y.keys.extend(z.keys)
                        y.n += z.n

                        if not y.is_leaf:
                            y.children.extend(z.children)

                        x.keys.pop(i)
                        x.n -= 1
                        if x.n == 0:
                            self.root = y
                        x.children.pop(i + 1)

                        remove_internal(x.children[i], key)
                else:
                    remove_internal(x.children[i], key)

        remove_internal(self.root, key)

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

    t.insert(5)
    t.insert(9)
    t.insert(3)
    t.insert(7)
    t.insert(1)
    t.insert(2)
    t.insert(8)
    t.insert(6)
    t.insert(0)
    t.insert(4)

    while True:
        print("1:insert 2:remove 3:print > ", end='')
        op = int(input())

        if op == 1:
            print("input key > ", end='')
            key = int(input())

            t.insert(key)
        elif op == 2:
            print("input key > ", end='')
            key = int(input())

            r = t.search(key)
            if not r:
                print(f"{key} is not found in the tree.")
            else:
                t.remove(key)
        elif op == 3:
            t.print_tree()
        else:
            print("invalid operation")
