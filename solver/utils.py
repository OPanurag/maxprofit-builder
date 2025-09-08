def format_solution(solution):
    return "Mix: " + ", ".join([f"{b}={c}" for b, c in solution.items()])
