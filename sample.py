"""
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
def format_solution_list(solutions):
    result = []
    for solution in solutions:
        result.append("Mix: " + ", ".join([f"{b}={solution.get(b, 0)}" for b in ["T", "P", "C"]]))
    return result


def solution_key(sol):
    return (sol.get("T", 0), sol.get("P", 0), sol.get("C", 0))


# ---------------- OPTIMIZER ----------------
def maximize_profit(n):
    """
    Dynamic programming with path tracking for multiple optimal combinations.
    Returns: max_profit, list of optimal building mixes.
    """
    dp = [(0, [{"T": 0, "P": 0, "C": 0}]) for _ in range(n + 1)]

    for t in range(n - 1, -1, -1):
        current_best_profit = -1
        current_best_solutions = []
        seen = set()

        # Try building each property
        for b, info in BUILDINGS.items():
            build_time = info["time"]
            per_unit_profit = info["profit"]
            finish_time = t + build_time

            if finish_time > n:
                continue

            operational_time = n - finish_time
            if operational_time <= 0:
                continue

            building_profit = per_unit_profit * operational_time
            future_profit, future_solutions = dp[finish_time]
            total_profit = building_profit + future_profit

            for sol in future_solutions:
                new_sol = sol.copy()
                new_sol[b] += 1
                key = solution_key(new_sol)

                if total_profit > current_best_profit:
                    current_best_profit = total_profit
                    current_best_solutions = [new_sol]
                    seen = {key}
                elif total_profit == current_best_profit and key not in seen:
                    current_best_solutions.append(new_sol)
                    seen.add(key)

        # Consider doing nothing (carry forward dp[t+1])
        next_profit, next_solutions = dp[t + 1]
        if next_profit > current_best_profit:
            current_best_profit = next_profit
            current_best_solutions = []
            seen = set()
            for sol in next_solutions:
                key = solution_key(sol)
                if key not in seen:
                    current_best_solutions.append(sol)
                    seen.add(key)
        elif next_profit == current_best_profit:
            for sol in next_solutions:
                key = solution_key(sol)
                if key not in seen:
                    current_best_solutions.append(sol)
                    seen.add(key)

        dp[t] = (current_best_profit, current_best_solutions)

    return dp[0]


# ---------------- MAIN ----------------
def main():
    try:
        time_units = int(input("Enter the total number of time units: ").strip())
    except:
        print("Please enter a valid integer for time units.")
        return

    profit, solutions = maximize_profit(time_units)
    print(f"Max Profit = ${profit}")
    print(f"{len(solutions)} possible combinations:")
    for line in format_solution_list(solutions):
        print(line)


if __name__ == "__main__":
    main()
