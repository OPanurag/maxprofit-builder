"""
Helper utilities for the Max Profit Builder project.
Currently provides functions to format the output of the optimizer
into a human-readable string for console display.
"""


def format_solution(solution):
    """
    Format the building mix dictionary into a user-friendly string.

    Args:
        solution (dict): Dictionary mapping building codes ("T", "P", "C")
                         to the number of units built.

    Returns:
        str: A formatted string representation of the mix.

    Example:
        >>> format_solution({"T": 2, "P": 0, "C": 1})
        'Mix: T=2, P=0, C=1'
    """
    return "Mix: " + ", ".join([f"{b}={c}" for b, c in solution.items()])
