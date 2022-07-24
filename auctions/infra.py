"""Auctions infrastructure."""

# pylint: disable=all


from .app import AuctionsRepository, Auction

class SqliteAuctionsRepository(AuctionsRepository):

    def get(self, auction_id: int):
        pass


    def save(self, auction: Auction):
        pass