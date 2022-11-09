from task2_3 import sum_digit
import pytest

list_examle = [(5, 11.55), (6, 14.07)]

@pytest.mark.parametrize('a. expectrd_result', list_examle)
def test_task2_3(a, expectrd_result):
    assert sum_digit(a) == expectrd_result0000-