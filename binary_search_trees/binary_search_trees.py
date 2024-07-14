class Element:

    __slots__ = ['key', 'left', 'right', 'parent']

    def __init__(self, key):
        self.key = key
        self.left = self.right = self.parent = None


class Tree:

    __slots__ = ['size', 'height', 'root']

    def __init__(self):
        self.size = self.height = 0
        self.root = None

    def put(self, z):
        self.size += 1

        x, y = self.root, None
        while x:
            y = x
            x = x.left if z.key < x.key else x.right

        z.parent = y
        if not y:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

        self.height = self.__get_height()

    def print_tree(self):

        def print_tree_internal(r, space_size=0):
            if r.left:
                print_tree_internal(r.left, space_size=space_size+1)

            print('    ' * space_size, f"{r.key:>3}")

            if r.right:
                print_tree_internal(r.right, space_size=space_size+1)

        print(f"size = {self.size} / height = {self.height}")

        if self.root:
            print_tree_internal(self.root)

    def __get_height(self):

        def get_height_internal(r):
            if not r:
                return -1

            height_of_left = get_height_internal(r.left)
            height_of_right = get_height_internal(r.right)

            if height_of_left > height_of_right:
                return height_of_left + 1
            else:
                return height_of_right + 1

        if not self.root:
            return 0

        return get_height_internal(self.root)


if __name__ == '__main__':
    t = Tree()

    while True:
        print("1:put 2:remove 3:print 4:successor > ", end='')
        op = int(input())

        if op == 1:
            print("input key > ", end='')
            key = int(input())

            t.put(Element(key))
        elif op == 2:
            pass
        elif op == 3:
            t.print_tree()
        elif op == 4:
            pass
        else:
            print("invalid operation")
