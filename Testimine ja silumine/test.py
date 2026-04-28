"""Tests for solution."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is True


def test__students_study__night_without_coffee__no_studying():
    """During night without coffee students do not study."""
    assert students_study(2, False) is False


def test__students_study__morning_with_coffee__studying():
    """During morning with coffee students study."""
    assert students_study(7, True) is True


def test__students_study__morning_without_coffee__no_studying():
    """During morning without coffee students do not study."""
    assert students_study(10, False) is False


def test__students_study__evening_with_coffee__studying():
    """During evening with coffee students study."""
    assert students_study(20, True) is True


def test__students_study__evening_without_coffee__studying():
    """During evening without coffee students study."""
    assert students_study(22, False) is False


def test__students_study__boundary_5_with_coffee__studying():
    """At time 5 with coffee students study."""
    assert students_study(5, True) is True


def test__students_study__boundary_17_without_coffee__no_studying():
    """At time 17 without coffee students do not study."""
    assert students_study(17, False) is False


def test__students_study__boundary_18_without_coffee__studying():
    """At time 18 without coffee students study."""
    assert students_study(18, False) is False


def test__students_study__boundary_4_with_coffee__no_studying():
    """At time 4 with coffee students do not study."""
    assert students_study(4, True) is True


def test__students_study__time_5_with_coffee__study():
    """Time 5 with coffee."""
    assert students_study(5, True) is True


def test__students_study__time_17_without_coffee__no_study():
    """Time 17 without coffee."""
    assert students_study(17, False) is False


def test__students_study__time_18__study():
    """Time 18 always study."""
    assert students_study(18, False) is False


def test__students_study__night_edge_with_coffee():
    """Night edge with coffee."""
    assert students_study(4, True) is True


def test__students_study__night_edge_without_coffee():
    """Night edge without coffee."""
    assert students_study(4, False) is False


def test__students_study__day_edge_with_coffee():
    """Day edge with coffee."""
    assert students_study(5, True) is True


def test__students_study__day_edge_without_coffee():
    """Day edge without coffee."""
    assert students_study(5, False) is False


def test__students_study__evening_edge_with_coffee():
    """Evening edge with coffee."""
    assert students_study(18, True) is True


def test__students_study__evening_edge_without_coffee():
    """Evening edge without coffee."""
    assert students_study(18, False) is False


def test__students_study__night_edge_case_coffee_true():
    """Night edge case with coffee."""
    assert students_study(1, True) is True


def test__students_study__night_edge_case_coffee_false():
    """Night edge case without coffee."""
    assert students_study(4, False) is False


def test__students_study__day_edge_case_coffee_true():
    """Day edge case with coffee."""
    assert students_study(5, True) is True


def test__students_study__day_edge_case_coffee_false():
    """Day edge case without coffee."""
    assert students_study(17, False) is False


def test__students_study__evening_edge_case_coffee_true():
    """Evening edge case with coffee."""
    assert students_study(18, True) is True


def test__students_study__evening_edge_case_coffee_false():
    """Evening edge case without coffee."""
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


def test__fruit_order__small_only__use_small():
    """Only small baskets used."""
    assert fruit_order(5, 0, 3) == 3


def test__fruit_order__mix_big_and_small__valid():
    """Combination of big and small baskets."""
    assert fruit_order(3, 1, 8) == 3


def test__fruit_order__not_possible__return_minus_one():
    """Order cannot be fulfilled."""
    assert fruit_order(1, 1, 7) == -1


def test__fruit_order__zero_amount__zero_small():
    """Zero order amount."""
    assert fruit_order(5, 5, 0) == 0


def test__fruit_order__edge_case__one_small():
    """Edge case requiring one small basket."""
    assert fruit_order(2, 1, 6) == 1


def test__fruit_order__all_zero():
    """All zero."""
    assert fruit_order(0, 0, 0) == 0


def test__fruit_order__only_big_not_enough():
    """Only big not enough."""
    assert fruit_order(0, 1, 10) == -1


def test__fruit_order__only_big_more_than_needed():
    """Only big more than needed."""
    assert fruit_order(0, 5, 10) >= 0


def test__fruit_order__only_small_exact():
    """Only small exact."""
    assert fruit_order(5, 0, 5) == 5


def test__fruit_order__only_small_not_enough():
    """Only small not enough."""
    assert fruit_order(3, 0, 5) == -1


def test__fruit_order__zero_amount_zero_small():
    """Zero amount, zero small."""
    assert fruit_order(0, 5, 0) == 0


def test__fruit_order__zero_amount_zero_big():
    """Zero amount, zero big."""
    assert fruit_order(5, 0, 0) == 0


def test__fruit_order__only_big_more_than_required_match():
    """Only big more than required exact match."""
    assert fruit_order(0, 3, 10) == 0


def test__fruit_order__only_big_more_than_required_no_match():
    """Only big cannot match exactly."""
    assert fruit_order(0, 3, 12) == -1


def test__fruit_order__only_small_more_than_required():
    """Only small more than required."""
    assert fruit_order(10, 0, 5) == 5


def test__fruit_order__match_with_more_than_5_smalls():
    """Match using more than 5 small baskets."""
    assert fruit_order(6, 1, 11) == 6


def test__fruit_order__use_some_smalls_some_bigs():
    """Use both small and big baskets."""
    assert fruit_order(4, 2, 14) == 4


def test__fruit_order__enough_bigs_not_enough_smalls():
    """Enough big baskets but not enough small."""
    assert fruit_order(1, 3, 16) == 1


def test__fruit_order__only_small_not_enough_more_than_5_smalls():
    """Only small baskets >5 but not enough."""
    assert fruit_order(6, 0, 10) == -1


def test__fruit_order__use_all_smalls_some_bigs():
    """Use all smalls and some bigs."""
    assert fruit_order(4, 2, 14) == 4


def test__fruit_order__use_some_smalls_less_bigs():
    """Use some small and some big baskets."""
    assert fruit_order(4, 2, 14) == 4


def test__fruit_order__not_enough_with_more_than_5_smalls():
    """Not enough even with many small baskets."""
    assert fruit_order(6, 1, 20) == -1


def test__fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Large numbers but not enough small."""
    assert fruit_order(2, 15, 103) == -1


def test__fruit_order__match_large_numbers():
    """Large numbers exact match."""
    assert fruit_order(25, 25, 100) == 0
