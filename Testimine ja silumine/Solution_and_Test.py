"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    # 1–4 → magavad
    if 1 <= time <= 4:
        return False

    # 5–17 → kohv peab olema
    if 5 <= time <= 17:
        return coffee_needed

    # 18–24 → alati õpivad
    if 18 <= time <= 24:
        return True

    return False


def lottery(a: int, b: int, c: int) -> int:
    # kõik 5 → 10
    if a == 5 and b == 5 and c == 5:
        return 10

    # kõik võrdsed → 5
    if a == b == c:
        return 5

    # b ja c mõlemad erinevad a-st → 1
    if b != a and c != a:
        return 1

    # muul juhul → 0
    return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    # kasutame võimalikult palju suuri korve
    max_big_used = min(big_baskets, ordered_amount // 5)

    remaining = ordered_amount - max_big_used * 5

    # kas väikestest piisab?
    if remaining <= small_baskets:
        return remaining

    return -1
"https://pydoc.pages.taltech.ee/code_quality/unittests.html"
