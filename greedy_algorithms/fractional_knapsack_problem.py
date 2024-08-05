if __name__ == '__main__':
    weights = [20, 30, 10]
    prices = [100, 120, 60]

    print("  i |", end='')
    for i in range(len(weights)):
        print(f"{i:>3}|", end='')
    print('')
    print("w[i]|", end='')
    for _w in weights:
        print(f"{_w:>3}|", end='')
    print('')
    print("p[i]|", end='')
    for _p in prices:
        print(f"{_p:>3}|", end='')
    print('')
