"""Tests for solution."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(1, True) is False
    assert students_study(2, True) is False
    assert students_study(3, True) is False
    assert students_study(4, True) is False


def test__students_study__night_without_coffee__no_studying():
    """During night without coffee students do not study."""
    assert students_study(1, False) is False
    assert students_study(2, False) is False
    assert students_study(3, False) is False
    assert students_study(4, False) is False


def test__students_study__morning_with_coffee__studying():
    """During morning with coffee students study."""
    assert students_study(5, True) is True
    assert students_study(6, True) is True
    assert students_study(7, True) is True
    assert students_study(8, True) is True
    assert students_study(9, True) is True
    assert students_study(10, True) is True
    assert students_study(11, True) is True
    assert students_study(12, True) is True
    assert students_study(13, True) is True
    assert students_study(14, True) is True
    assert students_study(15, True) is True
    assert students_study(16, True) is True
    assert students_study(17, True) is True


def test__students_study__morning_without_coffee__no_studying():
    """During morning without coffee students do not study."""
    assert students_study(5, False) is False
    assert students_study(6, False) is False
    assert students_study(7, False) is False
    assert students_study(8, False) is False
    assert students_study(9, False) is False
    assert students_study(10, False) is False
    assert students_study(11, False) is False
    assert students_study(12, False) is False
    assert students_study(13, False) is False
    assert students_study(14, False) is False
    assert students_study(15, False) is False
    assert students_study(16, False) is False
    assert students_study(17, False) is False


def test__students_study__evening_with_coffee__studying():
    """During evening with coffee students study."""
    assert students_study(18, True) is True
    assert students_study(19, True) is True
    assert students_study(20, True) is True
    assert students_study(21, True) is True
    assert students_study(22, True) is True
    assert students_study(23, True) is True
    assert students_study(24, True) is True


def test__students_study__evening_without_coffee__studying():
    """During evening without coffee students study."""
    assert students_study(18, False) is True
    assert students_study(19, False) is True
    assert students_study(20, False) is True
    assert students_study(21, False) is True
    assert students_study(22, False) is True
    assert students_study(23, False) is True
    assert students_study(24, False) is True


# ------------------------------------------------------------------


def test__lottery__all_fives__max_win():
    """All numbers are 5."""
    assert lottery(5, 5, 5) == 10


def test__lottery__all_same_not_five__medium_win():
    """All numbers same but not 5."""
    assert lottery(3, 3, 3) == 5


def test__lottery__all_different__small_win():
    """All numbers different."""
    assert lottery(1, 2, 3) == 1


def test__lottery__b_equals_a__no_win():
    """B equals a."""
    assert lottery(2, 2, 3) == 0


def test__lottery__c_equals_a__no_win():
    """C equals a."""
    assert lottery(4, 3, 4) == 0


def test__lottery__all_same_zero():
    """All zeros."""
    assert lottery(0, 0, 0) == 5


def test__lottery__all_same_negative():
    """All negative same."""
    assert lottery(-1, -1, -1) == 5


def test__lottery__b_c_same_a_diff():
    """B and c same, a different."""
    assert lottery(1, 2, 2) == 1


# ------------------------------------------------------------------


def test__fruit_order__exact_big_only__zero_small():
    """Only big baskets used exactly."""
    assert fruit_order(0, 2, 10) == 0
    assert fruit_order(0, 20, 100) == 0
    assert fruit_order(0, 200, 1000) == 0
    assert fruit_order(0, 10, 50) == 0
    assert fruit_order(0, 50, 250) == 0


def test__fruit_order__small_only__use_small():
    """Only small baskets used."""
    assert fruit_order(5, 0, 3) == 3
    assert fruit_order(10, 0, 9) == 9
    assert fruit_order(12, 0, 12) == 12
    assert fruit_order(50, 0, 50) == 50
    assert fruit_order(500, 0, 306) == 306
    assert fruit_order(5000, 0, 3000) == 3000
    assert fruit_order(75, 0, 75) == 75


def test__fruit_order__not_possible__return_minus_one():
    """Order cannot be fulfilled."""
    assert fruit_order(1, 1, 7) == -1


def test__fruit_order__zero():
    """Order zero."""
    assert fruit_order(0, 0, 0) == 0
    assert fruit_order(1, 0, 0) == 0
    assert fruit_order(0, 1, 0) == 0
    assert fruit_order(1, 1, 0) == 0
    assert fruit_order(0, 0, 0) == 0


def test__fruit_order__only_big_not_enough():
    """Only big not enough."""
    assert fruit_order(0, 1, 10) == -1


def test__fruit_order__only_small_not_enough():
    """Only small not enough."""
    assert fruit_order(3, 0, 5) == -1
    assert fruit_order(25, 0, 42) == -1
    assert fruit_order(40, 0, 70) == -1
    assert fruit_order(1, 0, 2) == -1


def test__fruit_order__only_big_more_than_required_match():
    """Only big cannot match exactly."""
    assert fruit_order(0, 3, 10) == 0
    assert fruit_order(0, 30, 100) == 0
    assert fruit_order(0, 56, 50) == 0
    assert fruit_order(0, 500, 1000) == 0


def test__fruit_order__only_big_more_than_required_no_match():
    """Only big cannot match exactly."""
    assert fruit_order(0, 3, 12) == -1
    assert fruit_order(0, 80, 122) == -1
    assert fruit_order(0, 4, 9) == -1
    assert fruit_order(0, 75, 156) == -1
    assert fruit_order(0, 30, 27) == -1


def test__fruit_order__use_smalls_some_bigs():
    """Use both small and big baskets."""
    assert fruit_order(4, 2, 14) == 4
    assert fruit_order(7, 2, 16) == 6
    assert fruit_order(7, 2, 19) == -1
    assert fruit_order(50, 2, 54) == 44
    assert fruit_order(4, 2, 14) == 4


def test__fruit_order__use_all_smalls_some_bigs():
    """Use all small and some big baskets."""
    assert fruit_order(4, 3, 14) == 4
    assert fruit_order(3, 7, 13) == 3
    assert fruit_order(1, 52, 101) == 1
    assert fruit_order(2, 12, 22) == 2
    assert fruit_order(2, 4, 7) == 2


def test__fruit_order__use_some_smalls_some_bigs():
    """Use some small and big baskets."""
    assert fruit_order(6, 3, 14) == 4
    assert fruit_order(600, 30, 4000) == -1
    assert fruit_order(4, 7, 27) == 2
    assert fruit_order(8, 32, 59) == 4
    assert fruit_order(11, 3, 11) == 1


def test__fruit_order__enough_bigs_not_enough_smalls():
    """Use enough small and big baskets."""
    assert fruit_order(3, 2, 14) == -1
    assert fruit_order(1, 20, 94) == -1
    assert fruit_order(1, 100, 402) == -1
    assert fruit_order(1, 100, 502) == -1


def test__fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Use not enough small and enough big baskets."""
    assert fruit_order(300, 200, 1400) == -1


def test__fruit_order__match_large_numbers():
    """Order match."""
    assert fruit_order(400, 200, 1400) == 400
    assert fruit_order(0, 200, 1000) == 0
    assert fruit_order(0, 400, 2000) == 0
    assert fruit_order(0, 2000, 10000) == 0
