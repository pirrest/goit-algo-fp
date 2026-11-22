items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def _validate(budget):
    if isinstance(budget, bool) or not isinstance(budget, int) or budget < 0:
        raise ValueError("Budget must be a non-negative integer")


def greedy_algorithm(items, budget):
    """Pick dishes by the best calories/cost ratio while the budget allows.

    Returns (chosen_names, total_calories, total_cost).
    """
    _validate(budget)
    by_ratio = sorted(items.items(),
                      key=lambda pair: pair[1]["calories"] / pair[1]["cost"],
                      reverse=True)
    chosen, total_cost, total_calories = [], 0, 0
    for name, info in by_ratio:
        if total_cost + info["cost"] <= budget:
            chosen.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]
    return chosen, total_calories, total_cost


def dynamic_programming(items, budget):
    """0/1 knapsack: the set of dishes with maximal calories within the budget.

    Returns (chosen_names, total_calories, total_cost).
    """
    _validate(budget)
    names = list(items)
    n = len(names)
    # table[i][b] = max calories using the first i dishes with budget b
    table = [[0] * (budget + 1) for _ in range(n + 1)]
    for i, name in enumerate(names, start=1):
        cost, calories = items[name]["cost"], items[name]["calories"]
        for b in range(budget + 1):
            table[i][b] = table[i - 1][b]
            if cost <= b:
                table[i][b] = max(table[i][b], table[i - 1][b - cost] + calories)

    # Walk back through the table to restore the chosen dishes.
    chosen, b = [], budget
    for i in range(n, 0, -1):
        if table[i][b] != table[i - 1][b]:
            name = names[i - 1]
            chosen.append(name)
            b -= items[name]["cost"]
    chosen.reverse()
    total_cost = sum(items[name]["cost"] for name in chosen)
    return chosen, table[n][budget], total_cost


def main():
    for budget in (30, 60, 100, 150):
        print(f"Бюджет: {budget}")
        for label, func in (("Жадібний", greedy_algorithm),
                            ("Динамічне програмування", dynamic_programming)):
            chosen, calories, cost = func(items, budget)
            print(f"  {label}: {chosen}, калорії: {calories}, вартість: {cost}")


if __name__ == "__main__":
    main()
