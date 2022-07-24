import copy
from auctions.app import AuctionsRepository
from auctions.domain import Auction, AuctionId

class FakeAuctionsRepository(AuctionsRepository):

    def __init__(self):
        self._data =  {}

    def get(self, auction_id: AuctionId) -> Auction:
        return copy.deepcopy(self._data[auction_id])

    def save(self, auction) -> None:
        self._data[auction.id] = copy.deepcopy(auction)