# pylint: disable=all

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, List



@dataclass
class Bid:
    id: Optional[int]
    bidder_id: int
    amount: Decimal


class Auction:
    

    # Each method belongs to either: command (changing the instance state) 
    # or query (returning data without changing the state) to follow 
    # CQS (command query separation) principle.

    # Queries are safe. They can be executed in any order without posing
    # risk to the state and integrity of the instance.
    # Commands are more risky. The order could be relevant.
    # Eg. There is not point in withdrawing and offer without placing it first.
    def __init__(self, id: int, starting_price: Decimal, bids: List[Bid]):
        self.id = id
        self.starting_price = starting_price
        self.bids = bids

    def place_bid(self, user_id: int, amount: Decimal):
        pass

    @property
    def current_price(self) -> Decimal:
        pass

    @property
    def winners(self) -> List[int]:
        pass
