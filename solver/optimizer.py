from solver.config import BUILDINGS

"""
The optimizer computes the maximum achievable profit and the optimal mix of
Theatres (T), Pubs (P), and Commercial Parks (C) that can be constructed
within a given number of time units. Only one property can be under construction
at any time, and each property generates profit per unit time after it is
completed, for the remainder of the available time horizon.

Approach:
- Use bottom-up dynamic programming, filling a dp table backwards from the end.
- dp[t] = maximum profit achievable starting from time t until the end n,
  along with the optimal building mix to achieve it.
- At each time t, decisions are:
    1. Skip building (carry forward dp[t+1]).
    2. Start constructing one of the available properties if time allows.
- Transition includes:
    profit = (per-unit profit × operational_time_remaining) + dp[finish_time].

This ensures sequential builds are respected and profits match the
example outputs from the problem statement.
"""

def maximize_profit(n):
    """
    Solve the Max Profit problem for a given time horizon.

    Args:
        n (int): Total number of time units available.

    Returns:
        tuple:
            - max_profit (int): Maximum achievable profit.
            - solution (dict): Dictionary with counts of buildings:
                {
                    "T": number_of_theatres,
                    "P": number_of_pubs,
                    "C": number_of_commercial_parks
                }
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
