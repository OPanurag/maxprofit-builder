import pytest
from solver.optimizer import maximize_profit


def test_case_1():
    profit, sol = maximize_profit(7)
    assert profit == 3000
    # Expected: either 1 Theatre (built at t=5, earns 3*1500=4500?) or 1 Pub? 
    # But according to PDF solution: T=1,P=0,C=0 or P=1,C=0
    # The canonical expected solution is Theatre (1) OR Pub (1)
    assert (sol == {"T": 1, "P": 0, "C": 0}) or (sol == {"T": 0, "P": 1, "C": 0})


def test_case_2():
    profit, sol = maximize_profit(8)
    assert profit == 4500
    # Expected from PDF: T=1, P=0, C=0
    assert sol == {"T": 1, "P": 0, "C": 0}


def test_case_3():
    profit, sol = maximize_profit(13)
    assert profit == 16500
    # Expected from PDF: T=2, P=0, C=0
    assert sol == {"T": 2, "P": 0, "C": 0}
