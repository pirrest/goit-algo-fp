import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

MAX_LEVEL = 12
DEFAULT_LEVEL = 8


def draw_square(ax, p1, p2, level, max_level):
    """Draw the square on base p1->p2 and recurse into two child squares."""
    (x1, y1), (x2, y2) = p1, p2
    # The square grows to the left of the direction p1 -> p2.
    ux, uy = -(y2 - y1), x2 - x1
    a = (x1 + ux, y1 + uy)
    b = (x2 + ux, y2 + uy)

    # Color goes from brown (trunk) to green (leaves).
    t = level / max_level if max_level else 1
    color = (0.45 * (1 - t) + 0.1 * t, 0.25 * (1 - t) + 0.7 * t, 0.1 * (1 - t) + 0.1 * t)
    ax.add_patch(Polygon([p1, p2, b, a], closed=True, facecolor=color,
                         edgecolor="black", linewidth=0.3))

    if level == max_level:
        return

    # Apex of the right isosceles triangle built on the top side a-b.
    apex = ((a[0] + b[0]) / 2 + ux / 2, (a[1] + b[1]) / 2 + uy / 2)
    draw_square(ax, a, apex, level + 1, max_level)
    draw_square(ax, apex, b, level + 1, max_level)


def draw_pythagoras_tree(level):
    fig, ax = plt.subplots(figsize=(10, 7))
    draw_square(ax, (-0.5, 0), (0.5, 0), 0, level)
    ax.set_aspect("equal")
    ax.autoscale_view()
    ax.axis("off")
    ax.set_title(f"Дерево Піфагора, рівень рекурсії: {level}")
    plt.show()


def ask_level():
    raw = input(f"Рівень рекурсії (0-{MAX_LEVEL}, Enter = {DEFAULT_LEVEL}): ").strip()
    if not raw:
        return DEFAULT_LEVEL
    level = int(raw)
    if not 0 <= level <= MAX_LEVEL:
        raise ValueError(f"Level must be between 0 and {MAX_LEVEL}")
    return level


def main():
    try:
        level = ask_level()
    except EOFError:
        level = DEFAULT_LEVEL
    draw_pythagoras_tree(level)


if __name__ == "__main__":
    main()
