import pytest
from solver.optimizer import maximize_profit


def test_case_1():
    profit, sol = maximize_profit(7)
    assert profit == 3000


def test_case_2():
    profit, sol = maximize_profit(8)
    assert profit == 4500


def test_case_3():
    profit, sol = maximize_profit(13)
    assert profit == 16500
