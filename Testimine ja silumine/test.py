"""Tests for solution."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False


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
    assert students_study(22, False) is True


def test__students_study__boundary_5_with_coffee__studying():
    """At time 5 with coffee students study."""
    assert students_study(5, True) is True


def test__students_study__boundary_17_without_coffee__no_studying():
    """At time 17 without coffee students do not study."""
    assert students_study(17, False) is False


def test__students_study__boundary_18_without_coffee__studying():
    """At time 18 without coffee students study."""
    assert students_study(19, False) is True


def test__students_study__boundary_4_with_coffee__no_studying():
    """At time 4 with coffee students do not study."""
    assert students_study(4, True) is False


#------------------------------------------------------------------


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
    """b equals a."""
    assert lottery(2, 2, 3) == 0


def test__lottery__c_equals_a__no_win():
    """c equals a."""
    assert lottery(4, 3, 4) == 0


#------------------------------------------------------------------


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
