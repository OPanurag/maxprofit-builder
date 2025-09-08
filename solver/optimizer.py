from solver.config import BUILDINGS


def maximize_profit(n):
    """
    Dynamic Programming approach to maximize profit within given time units.
    Returns (max_profit, {T: count, P: count, C: count})
    """
    # dp[i] = (profit, solution_dict)
    dp = [(0, {"T": 0, "P": 0, "C": 0}) for _ in range(n + 1)]

    for t in range(1, n + 1):
        best_profit, best_solution = dp[t]

        for b, info in BUILDINGS.items():
            build_time = info["time"]
            build_profit = info["profit"]

            if t >= build_time:
                prev_profit, prev_solution = dp[t - build_time]
                new_profit = prev_profit + build_profit

                if new_profit > best_profit:
                    new_solution = prev_solution.copy()
                    new_solution[b] += 1
                    best_profit, best_solution = new_profit, new_solution

        dp[t] = (best_profit, best_solution)

    return dp[n]
