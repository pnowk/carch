from auctions.domain import Auction
from auctions.domain.types import Money, USD


def test_new_auction_has_current_price_equal_to_starting():
    price = Money(USD, "10")
    auction = Auction(Money(USD, "10"))

    assert price == auction.current_price