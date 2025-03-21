import random


def sort(data):
    count_table = [0 for _ in range(max(data) + 1)]

    for d in data:
        count_table[d] += 1

    print("--- counting table before accumlating ---")
    print(count_table)

    for i in range(len(count_table) - 1):
        count_table[i + 1] += count_table[i]

    print("--- counting table after accumlating ---")
    print(count_table)

    auxiliary_table = [-1 for _ in range(len(data))]
    for i in reversed(range(len(data))):
        target_data = data[i]
        idx_of_target = count_table[target_data] - 1
        auxiliary_table[idx_of_target] = target_data
        count_table[target_data] -= 1

    data.clear()
    data.extend(auxiliary_table)


if __name__ == '__main__':
    data = [random.randint(1, 20) for _ in range(40)]
    
    print("--- before ---")
    print(data)

    print("--- sort ---")
    sort(data)

    print("--- after ---")
    print(data)
