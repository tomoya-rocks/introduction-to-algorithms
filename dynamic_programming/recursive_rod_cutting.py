import sys


def cut_rod(prices, length):
    if length == 0:
        return 0

    result = -sys.maxsize
    for i in range(1, length + 1):
        result = max(result, prices[i] + cut_rod(prices, length - i))

    return result


if __name__ == '__main__':
    prices = [0, 1, 5, 8, 9, 17, 17, 20, 24, 30]

    for i in range(len(prices)):
        result = cut_rod(prices, i)

        print(f"length = {i} / result = {result}")
