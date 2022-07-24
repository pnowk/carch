from auctions.domain.types import Money, USD, PLN



def test_money_equality():
    m1 = Money(PLN, "10.5")
    m2 = Money(PLN, "10.5")
    m3 = Money(USD, '1.0')

    assert (m1 is m2) is False
    assert (m1 == m2) is True
    assert (m1 == m3) is False
