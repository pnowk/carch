


from abc import ABC, abstractmethod
from ..domain import Auction, AuctionId

class AuctionsRepository(ABC):
    """Persistence oriented repository for auctions.

    .. note::

        Other kind of repository is collection oriented repository
        able to add or remove an item but not persist it.
    """
    
    @abstractmethod
    def get(self, auction_id: AuctionId) -> Auction:
        pass

    @abstractmethod
    def save(self, auction: Auction) -> None:
        pass