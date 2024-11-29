def floyd_warshall(W, PI):
    n = len(W)

    D = [W.copy() for _ in range(n)]
    P = [PI.copy() for _ in range(n)]
    print("--- D = 0 ---")
    print_matrix(D[0])
    print_matrix(P[0])

    for k in range(n):
        print(f"--- D = {k} ---")

        D[k] = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if D[k - 1][i][j] <= D[k - 1][i][k] + D[k - 1][k][j]:
                    D[k][i][j] = D[k - 1][i][j]
                    P[k][i][j] = P[k - 1][i][j]
                else:
                    D[k][i][j] = D[k - 1][i][k] + D[k - 1][k][j]
                    P[k][i][j] = P[k - 1][k][j]

        print("--- D ---")
        print_matrix(D[k])
        print("--- P ---")
        print_matrix(P[k])

    return D[n - 1], P[n - 1]


def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] is not None:
                print(f"{A[i][j]:^5}", end='')
            else:
                print(f"None ", end='')
        print('')


if __name__ == '__main__':
    W = [
        [0, 3, 8, 1000, -4],
        [1000, 0, 1000, 1, 7],
        [1000, 4, 0, 1000, 1000],
        [2, 1000, -5, 0, 1000],
        [1000, 1000, 1000, 6, 0]
    ]
    PI = [
        [None, 1, 1, None, 1],
        [None, None, None, 2, 2],
        [None, 3, None, None, None],
        [4, None, 4, None, None],
        [None, None, None, 5, None]
    ]

    print("--- Graph ---")
    print_matrix(W)
    print("---")
    print_matrix(PI)

    print("--- Floyd-Warshall algorithm ---")
    D, P = floyd_warshall(W, PI)

    print("--- result ---")
    print("--- W ---")
    print_matrix(D)
    print("--- PI ---")
    print_matrix(P)
