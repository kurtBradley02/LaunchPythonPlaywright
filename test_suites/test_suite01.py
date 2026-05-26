from step_definitions.test_definition01 import *


def test_01(page):
    actual = step_01(page)
    expected = "\n      Registration Submitted!\n      Name: test\n      Email: test@mail.com\n      Gender: Male\n      Nationality: Filipino\n      Updates: Yes\n    "
    result = actual == expected
    assert result
