from solver.config import BUILDINGS

def maximize_profit(n):
    """
    Dynamic Programming approach:
    At each time t, either:
    - Start building any property here (if enough time remains)
    - Or skip to t+1 (wait)
    Each property earns 'profit' per unit time after it is completed,
    only for the periods left in total time.
    """
    dp = [(0, {"T": 0, "P": 0, "C": 0}) for _ in range(n + 2)]

    for t in range(n, -1, -1):
        # Option 1: Do nothing - take dp[t+1]
        best_profit, best_solution = dp[t + 1]
        # Option 2: Start any building at time t
        for b, info in BUILDINGS.items():
            build_time = info["time"]
            per_unit_profit = info["profit"]
            finish_time = t + build_time
            if finish_time <= n:
                operational_time = n - finish_time  # Only time after completion (matches sample output)
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
