from auctions.domain import Bid, Money
from auctions.domain.entities import Auction
from auctions.domain.types import USD
from tests.fakes import FakeAuctionsRepository



def test_should_get_back_saved_auction():
    # Testing repository as a unit is ok because 
    # repository is an object storage abstraction.
    # Testing each method separately would violate
    # hermetization and make refactoring harder.
    bids = [
        Bid(id=1, bidder_id=1, amount=Money(USD, "10.0"))
    ]

    auction = Auction(auction_id=1, starting_price=Money(USD, "9"), bids=bids)

    repo = FakeAuctionsRepository()
    repo.save(auction)

    assert repo.get(auction.id) == auction