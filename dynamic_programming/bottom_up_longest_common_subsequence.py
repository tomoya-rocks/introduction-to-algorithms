import enum
import sys


class Direction(enum.Enum):

    UP = 'up'
    LEFT = 'left'
    DIAGONAL = 'diagonal'


def common_lcs(x, y):
    results = [[sys.maxsize for _ in range(len(y) + 1)]
               for _ in range(len(x) + 1)]
    directions = [[None for _ in range(len(y) + 1)]
               for _ in range(len(x) + 1)]

    for i in range(len(x)):
        for j in range(len(y)):
            if i == 0 and j == 0:
                if x[i] == y[j]:
                    results[i][j] = 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    results[i][j] = 0
                    directions[i][j] = Direction.UP
            elif i == 0:
                if x[i] == y[j]:
                    results[i][j] = 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    results[i][j] = results[i][j - 1]
                    directions[i][j] = Direction.LEFT
            elif j == 0:
                if x[i] == y[j]:
                    results[i][j] = 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    results[i][j] = results[i - 1][j]
                    directions[i][j] = Direction.UP
            else:
                if x[i] == y[j]:
                    results[i][j] = results[i - 1][j - 1] + 1
                    directions[i][j] = Direction.DIAGONAL
                else:
                    if results[i - 1][j] >= results[i][j - 1]:
                        results[i][j] = results[i - 1][j]
                        directions[i][j] = Direction.UP
                    else:
                        results[i][j] = results[i][j - 1]
                        directions[i][j] = Direction.LEFT

    return results, directions


def print_optimal_strategy(x, directions, i, j):
    if i < 0 or j < 0:
        return
    if directions[i][j] == Direction.DIAGONAL:
        print_optimal_strategy(x, directions, i - 1, j - 1)
        print(x[i], end='')
    elif directions[i][j] == Direction.UP:
        print_optimal_strategy(x, directions, i - 1, j)
    else:
        print_optimal_strategy(x, directions, i, j - 1)


if __name__ == '__main__':
    x = 'ABCBDAB'
    y = 'BDCABA'

    results, directions = common_lcs(x, y)

    for i in range(len(x)):
        for j in range(len(y)):
            print(f"i = {i}, j = {j}, X = {x[:i + 1]}, Y = {y[:j + 1]}, result = {results[i][j]}", end='')

            if results[i][j] > 0:
                print('(', end='')
                print_optimal_strategy(x, directions, i, j)
                print(')', end='')

            print('')
