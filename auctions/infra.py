"""Auctions infrastructure."""

# pylint: disable=all


from .app import AuctionsDataAccess, Auction


class ConcreteAuction(Auction):

    # Placeholder for concrete auction impl.
    pass

class DbAuctionsDataAccess(AuctionsDataAccess):

    # Placeholder for concrete data access impl.

    def get(self, aution_id: int):
        pass


    def save(self, aution: ConcreteAuction):
        pass