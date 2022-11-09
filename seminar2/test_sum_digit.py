from task2_2 import sum_digit
import pytest

def test_sum_digit():
    assert sum_digit(4) == [1, 2, 6, 24]
