def select_activities(start, finish):
    results = [0]
    finished = finish[0]

    for i in range(1, len(start)):
        if finished <= start[i]:
            results.append(i)
            finished = finish[i]

    return results


if __name__ == '__main__':
    start = [1, 3, 0, 5, 3, 5, 6, 7, 8, 2, 12]
    finish = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    print("  i |", end='')
    for i in range(len(start)):
        print(f"{i:>3}|", end='')
    print('')
    print("s[i]|", end='')
    for _s in start:
        print(f"{_s:>3}|", end='')
    print('')
    print("f[i]|", end='')
    for _f in finish:
        print(f"{_f:>3}|", end='')
    print('')

    activities = select_activities(start, finish)
    print('result = [', end='')
    for i, activity in enumerate(activities):
        print(activity, end=', ' if i < len(activities) - 1 else ']')
    print('')
