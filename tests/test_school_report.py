from src.school_report import *


def test_returns_single_green():
    assert grade_checker("75") == "Green: 1"


def test_returns_two_greens():
    assert grade_checker("75, 76") == "Green: 2"


def test_returns_single_amber():
    assert grade_checker("50") == "Amber: 1"
