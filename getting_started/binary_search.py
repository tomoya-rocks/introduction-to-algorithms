def search(data, key):
    idx_of_low = 0
    idx_of_high = len(data) - 1

    while idx_of_low <= idx_of_high:
        idx_of_min = (idx_of_low + idx_of_high) // 2

        if data[idx_of_min] == key:
            return idx_of_min
        elif data[idx_of_min] < key:
            idx_of_low = idx_of_min + 1
        else:
            idx_of_high = idx_of_min - 1

    return -1


if __name__ == '__main__':
    data = [i ** 2 for i in range(20)]

    print(data)

    print("input key > ", end='')
    key = int(input())

    result = search(data, key)
    if result == -1:
        print(f"{key} is not found.")
    else:
        print(f"result = {result}")
