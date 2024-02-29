# Some simple tests
import playground.add as add


def test_add():
    assert add(1, 2) == 3


def test_fail():
    assert add(1, 2) == 4
