import random
from collections import Counter

import matplotlib.pyplot as plt

ROLLS = 1_000_000
SEED = 42


def simulate(rolls=ROLLS, seed=SEED):
    """Roll two dice `rolls` times and return {sum: probability}."""
    if rolls <= 0:
        raise ValueError("Number of rolls must be positive")
    rng = random.Random(seed)
    counts = Counter(rng.randint(1, 6) + rng.randint(1, 6) for _ in range(rolls))
    return {total: counts[total] / rolls for total in range(2, 13)}


def analytical():
    """Exact probabilities: (6 - |s - 7|) / 36."""
    return {total: (6 - abs(total - 7)) / 36 for total in range(2, 13)}


def main():
    monte_carlo = simulate()
    exact = analytical()

    print(f"Кидків: {ROLLS}")
    print("Сума | Монте-Карло | Аналітично | Різниця (в.п.)")
    for total in range(2, 13):
        diff = (monte_carlo[total] - exact[total]) * 100
        print(f"{total:>4} | {monte_carlo[total] * 100:>10.2f}% | "
              f"{exact[total] * 100:>9.2f}% | {diff:>+8.3f}")

    sums = list(range(2, 13))
    width = 0.4
    plt.figure(figsize=(9, 5))
    plt.bar([s - width / 2 for s in sums], [monte_carlo[s] * 100 for s in sums],
            width, label="Монте-Карло")
    plt.bar([s + width / 2 for s in sums], [exact[s] * 100 for s in sums],
            width, label="Аналітично")
    plt.xticks(sums)
    plt.xlabel("Сума")
    plt.ylabel("Імовірність, %")
    plt.title("Імовірності сум при киданні двох кубиків")
    plt.legend()
    plt.savefig("task7_plot.png", dpi=120)
    plt.show()


if __name__ == "__main__":
    main()
