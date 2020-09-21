from src.school_report import *


def test_returns_single_green():
    assert grade_checker("75") == "Green: 1"
