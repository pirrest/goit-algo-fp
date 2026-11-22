import runpy

if __name__ == "__main__":
    for number in range(1, 8):
        print(f"=== Завдання {number} ===")
        runpy.run_module(f"task{number}", run_name="__main__")
        print()
