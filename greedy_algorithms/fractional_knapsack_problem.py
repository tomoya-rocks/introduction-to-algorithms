def select_items(weights, prices, limit):
    unit_prices = {}
    for i, (price, weight) in enumerate(zip(prices,  weights)):
        unit_prices[i] = price / weight

    sorted_unit_prices = sorted(
        unit_prices.items(), key=lambda x: x[1], reverse=True)

    rest = limit
    results = {}
    for idx, _ in sorted_unit_prices:
        weight_to_load = weights[idx] if weights[idx] <= rest else rest
        results[idx] = weight_to_load

        rest -= weight_to_load
        if rest == 0:
            break

    return results


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

    item_to_select = select_items(weights, prices, 50)
    print("--- result ---")
    total = 0.0
    for idx, weight in item_to_select.items():
        print(f"item = {idx}, weight = {weight}")

        total += weight * (prices[idx] / weights[idx])
    print(f"total = {total}")
