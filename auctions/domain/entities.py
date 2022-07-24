# pylint: disable=all

from dataclasses import dataclass
from typing import Optional
from .types import BidderId, Money, BidId, AuctionId

# Entities should be implemented in "pure" python. 
# Eg. should not be coupled with any other class like sqlalchemy ORM.

@dataclass
class Bid:
    """Entity representing an offer made."""
    
    id: Optional[BidId]
    bidder_id: BidderId
    amount: Money


class Auction:
    

    # Each method belongs to either: command (changing the instance state) 
    # or query (returning data without changing the state) to follow 
    # CQS (command query separation) principle.

    # Queries are safe. They can be executed in any order without posing
    # risk to the state and integrity of the instance.
    # Commands are more risky. The order could be relevant.
    # Eg. There is not point in withdrawing and offer without placing it first.
    def __init__(self, starting_price: Money):
        self._starting_price = starting_price

    def place_bid(self, bider_id: BidderId, amount: Money):
        pass

    @property
    def current_price(self) -> Money:
        return self._starting_price

    @property
    def winner(self) -> BidderId:
        pass
