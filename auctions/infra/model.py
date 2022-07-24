from gettext import bind_textdomain_codeset
from sqlalchemy import (
    Column, 
    ForeignKey, 
    Table, 
    Float,
    Integer, 
    String
)
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class AuctionModel(Base):
    __tablename__ = 'auctions'

    id = Column(Integer, primary_key=True)
    current_price = Column(Float(4, asdecimal=True))
    bids = relationship('BidModel')



class BidModel(Base):
    __tablename__ = 'bids'

    id = Column(Integer, primary_key=True)
    bidder_id = Column(Integer)
    auction_id = Column(Integer, ForeignKey('auctions.id'))
