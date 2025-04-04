def common_lcs(x, y, idx_of_start, idx_of_end):
    if idx_of_start == 0 and idx_of_end == 0:
        result = 1 if x[idx_of_start] == y[idx_of_end] else 0
    elif idx_of_start == 0:
        result = 1 if x[idx_of_start] == y[idx_of_end] \
            else common_lcs(x, y, idx_of_start, idx_of_end - 1)
    elif idx_of_end == 0:
        result = 1 if x[idx_of_start] == y[idx_of_end] \
            else common_lcs(x, y, idx_of_start - 1, idx_of_end)
    else:
        if x[idx_of_start] == y[idx_of_end]:
            result = common_lcs(x, y, idx_of_start - 1, idx_of_end) + 1
        else:
            result = max(common_lcs(x, y, idx_of_start - 1, idx_of_end), \
                common_lcs(x, y, idx_of_start, idx_of_end - 1))

    return result


if __name__ == '__main__':
    x = 'ABCBDAB'
    y = 'BDCABA'

    for i in range(len(x)):
        for j in range(len(y)):
            result = common_lcs(x, y, i, j)

            print(f"i = {i}, j = {j}, X = {x[:i + 1]}, Y = {y[:j + 1]}, result = {result}")
