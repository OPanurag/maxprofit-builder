import sys
from solver.optimizer import maximize_profit
from solver.utils import format_solution

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <time_units>")
        sys.exit(1)

    time_units = int(sys.argv[1])
    profit, solution = maximize_profit(time_units)
    print(f"Max Profit = ${profit}")
    print(format_solution(solution))

if __name__ == "__main__":
    main()
