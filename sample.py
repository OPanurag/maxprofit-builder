"""
Max Profit Builder Solution.

Single-file solution for the Max Profit Builder problem.
Online Compiler Compatible.

Problem:
- Given a total number of time units (n), determine the optimal sequence of
  Theatres (T), Pubs (P), and Commercial Parks (C) to construct.
- Only one property can be under construction at a time.
- Each property earns profit *per unit time* after it is completed,
  for the remainder of the time horizon.

Usage (example in online compiler):
Input:
13

Output:
Max Profit = $16500
Mix: T=2, P=0, C=0
"""

# ---------------- CONFIG ----------------
BUILDINGS = {
    "T": {"time": 5, "profit": 1500},   # Theatre
    "P": {"time": 4, "profit": 1000},   # Pub
    "C": {"time": 10, "profit": 3000},  # Commercial Park
}


# ---------------- UTILS ----------------
def format_solution(solution):
    """
    Format the building mix dictionary into a readable string.
    """
    return "Mix: " + ", ".join([f"{b}={c}" for b, c in solution.items()])


# ---------------- OPTIMIZER ----------------
def maximize_profit(n):
    """
    Dynamic programming solution.

    Args:
        n (int): Total available time units.

    Returns:
        (int, dict): Maximum profit and optimal building mix.
    """
    dp = [(0, {"T": 0, "P": 0, "C": 0}) for _ in range(n + 2)]

    for t in range(n, -1, -1):
        best_profit, best_solution = dp[t + 1]  # Option: do nothing

        for b, info in BUILDINGS.items():
            build_time = info["time"]
            per_unit_profit = info["profit"]
            finish_time = t + build_time
            if finish_time <= n:
                operational_time = n - finish_time
                if operational_time > 0:
                    building_profit = per_unit_profit * operational_time
                    future_profit, future_solution = dp[finish_time]
                    total_profit = building_profit + future_profit
                    if total_profit > best_profit:
                        new_solution = future_solution.copy()
                        new_solution[b] += 1
                        best_profit = total_profit
                        best_solution = new_solution
        dp[t] = (best_profit, best_solution)

    return dp[0]


# ---------------- MAIN ----------------
def main():
    """
    Reads input n, computes max profit and building mix, and prints results.
    """
    try:
        time_units = int(input("Enter the total number of time units: ").strip())
    except Exception:
        print("Please enter a valid integer for time units.")
        return

    profit, solution = maximize_profit(time_units)
    print(f"Max Profit = ${profit}")
    print(format_solution(solution))


if __name__ == "__main__":
    main()
