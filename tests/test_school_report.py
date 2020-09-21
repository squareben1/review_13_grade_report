from src.school_report import *


def test_returns_single_green():
    assert check_grades("75") == "Green: 1"


def test_returns_two_greens():
    assert check_grades("75, 76") == "Green: 2"


def test_returns_single_amber():
    assert check_grades("50") == "Amber: 1"


def test_returns_two_ambers():
    assert check_grades("50, 51") == "Amber: 2"


def test_returns_single_red():
    assert check_grades("49") == "Red: 1"


def test_returns_two_red():
    assert check_grades("49, 49") == "Red: 2"


def test_returns_diff_grades():
    assert check_grades("10, 50, 70, 100") == "Green: 1\nAmber: 2\nRed: 1"
