class Element:

    __slots__ = ['data', 'next']

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    __slots__ = ['head', 'tail']

    def __init__(self):
        self.head = self.tail = None


class DisjointSet:

    def __init__(self, characters):
        self.sets = [None for _ in range(len(characters))]

        self.__initialize_set(characters)

    def union(self, ch1, ch2):

        def find_set(ch):
            result = None
            for s in self.sets:
                p = s.head
                while p:
                    if p.data == ch:
                        result = s

                        break

                    p = p.next

                if result:
                    return result

            return None

        s1 = find_set(ch1)
        s2 = find_set(ch2)

        if s1 == s2:
            return

        s1.tail.next = s2.head
        s1.tail = s2.tail
        self.sets.remove(s2)

    def find_set(self, ch):
        for s in self.sets:
            result = None
            p = s.head
            while p:
                if p.data == ch:
                    result = p

                    break

                p = p.next

            if result:
                return s.head.data

        return None

    def print_disjoint_set(self):

        def print_list(l):
            p = l.head
            while p:
                print(p.data, end=' -> ' if p.next else '')

                p = p.next

            print('')

        for s in self.sets:
            print_list(s)

    def __initialize_set(self, characters):
        for i, ch in enumerate(characters):
            self.sets[i] = LinkedList()
            self.sets[i].head = self.sets[i].tail = Element(ch)


if __name__ == '__main__':
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    disjoint_set = DisjointSet(characters)

    while True:
        print("1:union 2:find 3:print > ", end='')
        op = int(input())

        if op == 1:
            print("input character 1 > ", end='')
            ch1 = input()
            print("input character 2 > ", end='')
            ch2 = input()

            disjoint_set.union(ch1, ch2)
        elif op == 2:
            print("input data > ", end='')
            data = input()

            representative = disjoint_set.find_set(data)
            if representative:
                print(f"representative element = {representative}")
            else:
                print(f"{data} is not found.")
        elif op == 3:
            disjoint_set.print_disjoint_set()
        else:
            print("invalid operation")
