"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 1 <= time <= 4:
        return False

    if 5 <= time <= 17:
        return coffee_needed

    if 18 <= time <= 24:
        return True

    return False
    pass


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10

    if a == b == c:
        return 5

    if b != a and c != a:
        return 1

    return 0
    pass


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    max_big_used = min(big_baskets, ordered_amount // 5)

    for big_used in range(max_big_used, -1, -1):
        remaining = ordered_amount - big_used * 5

        if remaining <= small_baskets:
            return remaining

    return -1
    pass
