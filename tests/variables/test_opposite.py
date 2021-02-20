import pytest


from tasks.variables.opposite import opposite


@pytest.mark.parametrize(
    "n, expected", [
        (1, -1),
        (3, -3),
        (5.123, -5.123),
     ]
)
def test_cockroach_speed(n, expected):
    assert opposite(n) == expected
