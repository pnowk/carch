# pylint: disable=all

from dataclasses import dataclass
from typing import Optional, List
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
    # Important: all code inside should protect the invariants.
    def __init__(
        self,
        auction_id: AuctionId,
        starting_price: Money,
        bids: List[Bid]
        ):
        self._id = auction_id
        self._bids = sorted(bids, key=lambda bid: bid.amount)
        self._starting_price = starting_price

    @property
    def id(self):
        return self._id

    def place_bid(self, bidder_id: BidderId, amount: Money):
        """Submit a bid to the auction."""

        if amount > self.current_price:
            bid = Bid(id=None, bidder_id=bidder_id, amount=amount)
            self._bids.append(bid)

    @property
    def current_price(self) -> Money:
        """Get the highest bid amount or starting
        auction price if no bids were made."""

        if not self._bids:
            return self._starting_price
        return self._highest_bid.amount

    @property
    def winner(self) -> Optional[BidderId]:
        """Get the bidder id of the hightes bid or `None`
        if no bids were made."""

        if self._bids:
            return self._hightest_bid.bidder_id
        return None
            
    @property
    def _hightest_bid(self) -> Optional[BidderId]:
        
        # Hightest bid is the last on the list.
        return self._bids[-1]

    def __eq__(self, o: 'Auction') -> bool:
        return vars(self) == vars(o)
        
