from temp_conversion_module import convert_c_to_f
from temp_conversion_module import fever_detection


def test_convert_c_to_f():
    answer = convert_c_to_f(20.0)
    expected = 68.0

    assert answer == expected


def test_2():
    answer = convert_c_to_f(-40)
    expected = -40

    assert answer == expected


def test_3():
    answer = convert_c_to_f(50)
    expected = 122

    assert answer == expected


def test_fever_detection():
    temp_list = [93.0, 98.0, 100.0, 104.0, 101.0]
    max_temp, is_fever = fever_detection(temp_list)
    max_expected = 104.0
    expected_is_fever = True

    assert max_temp == max_expected
    assert is_fever == expected_is_fever


def test_fever_detection_bad():
    temp_list = [93.0, "98.0", 105.0, 101.0]
    max_temp, is_fever = fever_detection(temp_list)
    max_expected = 105.0
    expected_is_fever = True

    assert max_temp == max_expected
    assert is_fever == expected_is_fever
