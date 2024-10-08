def common_lcs(x, y, i, j):
    if i == 0 and j == 0:
        return 1 if x[0] == y[0] else 0
    elif i == 0:
        return 1 if x[i] == y[j] else common_lcs(x, y, i, j - 1)
    elif j == 0:
        return 1 if x[i] == y[j] else common_lcs(x, y, i - 1, j)
    else:
        if x[i] == y[j]:
            return common_lcs(x, y, i - 1, j - 1) + 1
        else:
            return max(common_lcs(x, y, i - 1, j), common_lcs(x, y, i, j - 1))


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    for i, _ in enumerate(x):
        print(f"--- i = {i} ---")

        for j, _ in enumerate(y):
            result = common_lcs(x, y, i, j)

            print(f"i = {i}, j = {j}, x = {
                  x[:i + 1]}, y = {y[:j + 1]}, result={result}")
