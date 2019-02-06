import pytest


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (5, -2, 3),
                                            (10, 20, 30)])
def test_calculator(a, b, expected):
    from fun import add_two
    answer = add_two(a, b)
    assert answer == expected
