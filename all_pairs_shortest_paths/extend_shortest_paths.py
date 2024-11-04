import sys


def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f"{A[i][j]:>5}", end=' ')

        print('')


def extend_shortest_paths(L, W):
    for i in range(len(L)):
        for j in range(len(L[i])):
            l = sys.maxsize
            for k in range(len(L[i])):
                l = min(l, L[i][k] + W[k][j])

            L[i][j] = l


def all_pairs_shortest_paths(W):
    L = [[W[i][j] for j in range(len(W))] for i in range(len(W))]

    print("--- l = 0 ---")
    print_matrix(L)

    for l in range(1, len(W) - 1):
        extend_shortest_paths(L, W)

        print(f"--- l = {l} ---")
        print_matrix(L)


if __name__ == '__main__':
    W = [
        [0, 3, 8, 1000, -4],
        [1000, 0, 1000, 1, 7],
        [1000, 4, 0, 1000, 1000],
        [2, 1000, - 5, 0, 1000],
        [1000, 1000, 1000, 6, 0]
    ]

    print("--- Adjacency Matrix ---")
    print_matrix(W)

    print("--- execute algotithm ---")
    all_pairs_shortest_paths(W)
