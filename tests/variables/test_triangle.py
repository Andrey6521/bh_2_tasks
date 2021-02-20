import pytest


from tasks.variables.triangle import triangle


@pytest.mark.parametrize(
    "side_1, side_2, expected", [
        (3, 4, (5, 14, 6)),
        (5, 12, (13, 34, 30)),
        (33, 56, (65, 178, 924)),
     ]
)
def test_tip(side_1, side_2, expected):
    assert triangle(side_1, side_2) == expected
