class Element:

    def __init__(self):
        self.is_leaf = True
        self.n = 0
        self.keys = []
        self.children = []


class Tree:

    def __init__(self, min_degree=2):
        self.root = Element()
        self.min_degree = min_degree

    def insert(self, key):
        r = self.root

        if r.n == 2 * self.min_degree - 1:
            s = Element()
            s.children.append(r)
            s.is_leaf = False

            self.root = s
            
            self.__split_child(s, 0)

            self.__insert_non_full(s, key)
        else:
            self.__insert_non_full(r, key)

    def search(self, key):
        
        def search_internal(r, key):
            i = 0
            while i <= r.n - 1 and r.keys[i] < key:
                i += 1

            if i <= r.n - 1 and r.keys[i] == key:
                return r
            else:
                if r.is_leaf:
                    return None
                else:
                    return search_internal(r.children[i], key)

        return search_internal(self.root, key)

    def remove(self, key):

        def remove_internal(r, key):
            i = 0
            while i <= r.n - 1 and r.keys[i] < key:
                i += 1

            if i <= r.n - 1 and r.keys[i] == key:
                if r.is_leaf:
                    # case 1
                    r.keys.pop(i)
                    r.n -= 1
                else:
                    # case 2
                    if r.children[i].n >= self.min_degree:
                        replacement = r.children[i].keys[-1]
                        r.keys[i] = replacement
                        r.children[i].keys = r.children[i].keys[:-1]
                        r.children[i].n -= 1
                    elif r.children[i + 1].n >= self.min_degree:
                        replacement = r.children[i + 1].keys[0]
                        r.keys[i] = replacement
                        r.children[i + 1].keys = r.children[i + 1].keys[1:]
                        r.children[i + 1].n -= 1
                    else:
                        y = r.children[i]
                        z = r.children[i + 1]
                        y.keys += x.keys
                        y.n += x.n
                        y.keys += z.keys
                        y.n += z.n
                        if not y.is_leaf:
                            y.children += z.children
                        if self.root == x:
                            self.root = y
                        remove_internal(y, key)
            else:
                # case 3
                if r.children[i].n == self.min_degree - 1:
                    if i - 1 >= 0 and r.children[i - 1].n >= self.min_degree:
                        y = r.children[i - 1]
                        z = r.children[i]

                        key_to_up = y.keys[-1]
                        key_to_down = r.keys[i - 1]
                        y.keys = y.keys[:-1]
                        y.n -= 1
                        r.keys[i - 1] = key_to_up
                        z.keys.insert(0, key_to_down)
                        z.n += 1

                        if not y.is_leaf:
                            z.children.insert(0, y.children[-1])
                            y.children = y.children[:-1]
                    elif i <= r.n - 1 and r.children[i + 1].n >= self.min_degree:
                        y = r.children[i]
                        z = r.children[i + 1]

                        key_to_up = z.keys[0]
                        key_to_down = r.keys[i]
                        z.keys = z.keys[1:]
                        z.n -= 1
                        r.keys[i] = key_to_up
                        y.keys.append(key_to_down)
                        y.n += 1

                        if not z.is_leaf:
                            y.children.append(z.children[0])
                            z.children = z.children[1:]
                    else:
                        if i - 1 >= 0 and r.children[i - 1].n == self.min_degree - 1:
                            y = r.children[i - 1]
                            z = r.children[i]
                            key_to_down = r.keys[i - 1]

                            y.keys.append(key_to_down)
                            y.n += 1
                            y.keys.extend(z.keys)
                            y.n += z.n

                            if not y.is_leaf:
                                y.children.extend(z.children)

                            r.keys.remove(key_to_down)
                            r.n -= 1
                            r.children.pop(i)

                            if len(r.keys) == 0:
                                self.root = y

                            i -= 1
                        elif i <= r.n - 1 and r.children[i + 1].n == self.min_degree - 1:
                            y = r.children[i]
                            z = r.children[i + 1]
                            key_to_down = r.keys[i]

                            y.keys.append(key_to_down)
                            y.n + 1
                            y.keys.extend(z.keys)
                            y.n += z.n

                            if not y.is_leaf:
                                y.children.extend(z.children)

                            r.keys.remove(key_to_down)
                            r.n -= 1
                            r.children.pop(i + 1)

                            if len(r.keys) == 0:
                                self.root = y

                remove_internal(r.children[i], key)

        remove_internal(self.root, key)

    def __insert_non_full(self, x, key):
        i = x.n - 1
        if x.is_leaf:
            while i >= 0 and key < x.keys[i]:
                i -= 1

            i += 1
            x.keys.insert(i, key)
            x.n += 1
        else:
            while i >= 0 and key < x.keys[i]:
                i -= 1

            i += 1
            if x.children[i].n == 2 * self.min_degree - 1:
                self.__split_child(x, i)
                if key > x.keys[i]:
                    i += 1

            self.__insert_non_full(x.children[i], key)

    def __split_child(self, x, i):
        y = x.children[i]
        z = Element()
        key_to_up = y.keys[self.min_degree - 1]
        z.keys = y.keys[self.min_degree:]
        z.n = self.min_degree - 1
        y.keys = y.keys[:self.min_degree - 1]
        y.n = self.min_degree - 1

        z.is_leaf = y.is_leaf
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
                    print_tree_internal(c, space_size=space_size+1)
        
        if self.root.keys:
            print_tree_internal(self.root)


if __name__ == '__main__':
    t = Tree()

    # https://www.cs.utexas.edu/~djimenez/utsa/cs3343/lecture17.html
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

            x = t.search(key)
            if not x:
                print(f"{key} is not found in the tree.")
            else:
                t.remove(key)
        elif op == 3:
            t.print_tree()
        else:
            print("invalid operation")
