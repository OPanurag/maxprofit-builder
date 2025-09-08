import sys
from solver.optimizer import maximize_profit
from solver.utils import format_solution

def main():

    """
    Command-line entry point for the Max Profit Builder project.

    It expects a single integer argument representing the total number of time
    units available for construction. The script calls the dynamic programming
    optimizer to compute the maximum profit achievable and the optimal mix of
    Theatres (T), Pubs (P), and Commercial Parks (C). The result is printed
    to the console.

    Usage:
        python main.py <time_units>

    Example:
        python main.py 13
        Output:
            Max Profit = $16500
            Mix: T=2, P=0, C=0
    """

    if len(sys.argv) != 2:
        print("Usage: python main.py <time_units>")
        sys.exit(1)

    time_units = int(sys.argv[1])
    profit, solution = maximize_profit(time_units)
    print(f"Max Profit = ${profit}")
    print(format_solution(solution))

if __name__ == "__main__":
    main()
