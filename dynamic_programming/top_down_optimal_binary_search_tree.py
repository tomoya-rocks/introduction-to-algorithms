import sys


def optimal_bst(p, q, idx_of_start, idx_of_end):
    results = [[sys.maxsize for _ in range(len(p) + 1)]
               for _ in range(len(p) + 1)]

    return optimal_bst_internal(p, q, idx_of_start, idx_of_end, results)


def optimal_bst_internal(p, q, idx_of_start, idx_of_end, results):
    if results[idx_of_start][idx_of_end] < sys.maxsize:
        return results[idx_of_start][idx_of_end]

    if idx_of_end == idx_of_start - 1:
        result = q[idx_of_start - 1]
    else:
        w = q[idx_of_start - 1]
        for l in range(idx_of_start, idx_of_end + 1):
            w += p[l]
            w += q[l]
        w = round(w, 2)

        result = sys.maxsize
        for r in range(idx_of_start, idx_of_end + 1):
            result = min(result, optimal_bst_internal(p, q, idx_of_start, r - 1, results) \
                + optimal_bst_internal(p, q, r + 1, idx_of_end, results) + w)

        result = round(result, 2)

    results[idx_of_start][idx_of_end] = result

    return result


if __name__ == '__main__':
    p = [0.0, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

    print("  i |", end='')
    for i in range(len(p)):
        print(f"{i:^5}|", end='')
    print('')
    print("p[i]|", end='')
    for _p in p:
        print(f"{_p:>5.2f}|", end='')
    print('')
    print("q[i]|", end='')
    for _q in q:
        print(f"{_q:>5.2f}|", end='')
    print('')

    diff = -1
    while diff < len(p):
        print(f"--- diff = {diff} ---")

        i = 1
        j = i + diff
        while j < len(p):
            result = optimal_bst(p, q, i, j)

            print(f"i = {i}, j = {j} / result = {result:.2f}")

            i += 1
            j += 1

        diff += 1
