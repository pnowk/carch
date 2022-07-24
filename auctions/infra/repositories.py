"""Auctions infrastructure."""

# pylint: disable=all


from typing import Optional, Dict
from attrs import define
from ..domain import AuctionId, Auction
from ..app import AuctionsRepository
from sqlalchemy.orm import Session
from .model import BidModel, AuctionModel


@define
class SqliteAuctionsRepository(AuctionsRepository):
    _session: Session

    def get(self, auction_id: AuctionId) -> Optional[Dict]:
  
        auction = self._session.query(AuctionModel).filter(
            AuctionModel.id == auction_id
        ).first()

        if auction:

            return {
                'id': auction.id,
                'current_price': auction.current_price,
                'bids': [{'id':b.id, 'bidder_id': b.bidder_id} for b in auction.bids]
            }


    def save(self, auction: Auction):
        auction_model = AuctionModel(
            id=auction.id,
            current_price=auction.current_price.amount,
            
        )
        self._session.merge(auction_model)
      
        for bid in auction._bids:
            self._session.merge(
                BidModel(
                    id=bid.id, 
                    bidder_id = bid.bidder_id,
                    auction_id=auction.id
                )
            )

        self._session.commit()
        
