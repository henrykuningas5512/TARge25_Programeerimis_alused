"""Tests for solution."""


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False
from Solution_and_Test import students_study, lottery, fruit_order


# -------------------
# STUDENTS STUDY
# -------------------

def test_students_study_night_sleep():
    assert students_study(2, True) is False
    assert students_study(4, False) is False


def test_students_study_day_with_coffee():
    assert students_study(10, True) is True


def test_students_study_day_without_coffee():
    assert students_study(10, False) is False


def test_students_study_evening():
    assert students_study(18, False) is True
    assert students_study(23, True) is True


def test_students_study_boundaries():
    assert students_study(5, True) is True
    assert students_study(17, True) is True
    assert students_study(1, True) is False
    assert students_study(24, False) is True


# -------------------
# LOTTERY
# -------------------

def test_lottery_all_fives():
    assert lottery(5, 5, 5) == 10


def test_lottery_all_equal_not_five():
    assert lottery(2, 2, 2) == 5


def test_lottery_all_different_from_a():
    assert lottery(3, 1, 2) == 1


def test_lottery_one_matches_a():
    assert lottery(3, 3, 1) == 0
    assert lottery(3, 1, 3) == 0


# -------------------
# FRUIT ORDER
# -------------------

def test_fruit_order_exact_match():
    assert fruit_order(3, 1, 8) == 3  # 5 + 3


def test_fruit_order_only_big():
    assert fruit_order(0, 2, 10) == 0


def test_fruit_order_only_small():
    assert fruit_order(5, 0, 4) == 4


def test_fruit_order_impossible():
    assert fruit_order(1, 1, 7) == -1


def test_fruit_order_use_less_big():
    assert fruit_order(6, 2, 7) == 2  # 5 + 2


def test_fruit_order_zero():
    assert fruit_order(0, 0, 0) == 0