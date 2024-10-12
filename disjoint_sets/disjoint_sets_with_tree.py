class Element:

    def __init__(self, character):
        self.character = character
        self.parent = self
        self.rank = 0

    def print_element(self):
        print(self.character, end='')
        if self.character != self.parent.character:
            print(f", parent = {self.parent.character}", end='')
        print('')


def union(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y

        if x.rank == y.rank:
            y.rank += 1


def find_set(elem):
    if elem != elem.parent:
        elem.parent = find_set(elem.parent)

    return elem.parent


if __name__ == '__main__':
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    elements = {ch: Element(ch) for ch in characters}

    while True:
        print("1:find 2:union 3:print > ", end='')
        op = int(input())

        if op == 1:
            print("input character > ", end='')
            ch = input()

            root = find_set(elements[ch])
            print(f"root = {root.character}")
        elif op == 2:
            print("input character > ", end='')
            x = input()
            print("input character > ", end='')
            y = input()

            union(elements[x], elements[y])
        elif op == 3:
            for elem in elements.values():
                elem.print_element()
        else:
            print("invalid operation")
