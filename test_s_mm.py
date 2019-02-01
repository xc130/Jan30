import pytest

@pytest.mark.parametrize("v1, v2, out1, list, out2, out3",[(7, 5, 2, [3,9,7,1,5],1,9), (8,-2,10,[13,4,8,19,-4,6] ,-4,19), (-3, -8, -11, [-30,-2,-4], -30,-2)])

def test_s_mm(v1, v2, out1, list, out2, out3):
    from subtract_two import subtract_two
    from min_max import find_min_max

    subans = subtract_two(v1, v2)
    mn, mx = find_min_max(list)

    assert subans == out1
    assert mn == out2
    assert mx == out
