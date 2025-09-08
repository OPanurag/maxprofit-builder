"""
test_optimizer.py

Unit tests for the dynamic programming optimizer in the Max Profit Builder project.

These tests validate that:
1. The optimizer returns the correct maximum profit for a given time horizon.
2. The optimizer selects the correct mix of Theatres (T), Pubs (P), and
   Commercial Parks (C) as specified in the original problem statement.

Test cases are based directly on the examples provided in the PDF.
"""

import pytest
from solver.optimizer import maximize_profit


def test_case_1():
    """
    Time units: 7
    Expected profit: 3000
    Expected mix: Either
        - 1 Theatre (T=1, P=0, C=0), or
        - 1 Pub (T=0, P=1, C=0)
    """
    profit, sol = maximize_profit(7)
    assert profit == 3000
    assert (sol == {"T": 1, "P": 0, "C": 0}) or (sol == {"T": 0, "P": 1, "C": 0})


def test_case_2():
    """
    Time units: 8
    Expected profit: 4500
    Expected mix: 1 Theatre (T=1, P=0, C=0)
    """
    profit, sol = maximize_profit(8)
    assert profit == 4500
    assert sol == {"T": 1, "P": 0, "C": 0}


def test_case_3():
    """
    Time units: 13
    Expected profit: 16500
    Expected mix: 2 Theatres (T=2, P=0, C=0)
    """
    profit, sol = maximize_profit(13)
    assert profit == 16500
    assert sol == {"T": 2, "P": 0, "C": 0}
