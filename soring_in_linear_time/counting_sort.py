import random


def sort(data):
    counting_table = [0 for _ in range(max(data) + 1)]

    for d in data:
        counting_table[d] += 1

    for i in range(1, len(counting_table)):
        counting_table[i] += counting_table[i - 1]

    print("--- counting table ---")
    print(counting_table)

    temp = [-1 for _ in range(len(data))]
    for i in reversed(range(len(data))):
        target_data = data[i]
        idx_to_be_replaced = counting_table[target_data] - 1
        temp[idx_to_be_replaced] = target_data
        counting_table[target_data] -= 1

    print("--- temporary data ---")
    print(temp)

    data.clear()
    data.extend(temp)


if __name__ == '__main__':
    data = [random.randint(1, 20) for _ in range(40)]

    print("--- before ---")
    print(data)

    print("--- sort ---")
    sort(data)

    print("--- after ---")
    print(data)
