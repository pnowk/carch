# pylint: disable=all

import abc
from dataclasses import dataclass
from auctions.app.repositories import AuctionsRepository
from auctions.domain.types import AuctionId, BidderId, Money
from ..domain import Auction


@dataclass(frozen=True)
class PlacingBidInputDto:
    bidder_id: int
    auction_id: int
    amount: Money


@dataclass(frozen=True)
class PlacingBidOutputDto:
    is_winning: bool
    current_price: Money


class PlacingBidOutputBoundary(abc.ABC):
    @abc.abstractmethod
    def present(self, output_dto: PlacingBidOutputDto):
        pass


class PlacingBidInputBoundary(abc.ABC):
    @abc.abstractmethod
    def execute(self, input_dto: PlacingBidInputDto, presenter: PlacingBidOutputBoundary):
        pass


class PlacingBidWebPresenter(PlacingBidOutputBoundary):
    """Concrete class implementing output boundary interface.
    
    It's job is to convert the output dto to a presentable web format.
    """
    def present(self, output_dto: PlacingBidOutputDto):

        # We do not return anything to the controler (or view) effectively
        # ending the flow, however we could be returning a value.

        self.result = {
            "price": f'${output_dto.current_price.quantize(".01")}',
            "is_winning": "Congrats!" if output_dto.is_winning else "Sorry..."
        }

    def get_presented_data(self) -> dict:

        # Since the formatted data is not returned we need 
        # a way to further fetch the results.
        # Here returned dict is another dto. It's common in various
        # python web frameworks. We could be returning something
        # more sophisticated though.
        return self.result


class AuctionsDataAccess:
    @abc.abstractmethod
    def get(self, auction_id: int):
        pass

    def save(self, auction: Auction):
        pass


class PlacingBid(PlacingBidInputBoundary):
    """PlacingBid controller.
    
    Use case orchestrates the whole business process.
    """

    def __init__(
        self,
        auctions_repo: AuctionsRepository,
        output_boundary: PlacingBidOutputBoundary
        ):

        # Important is how repository and output_boundary are created.
        # Here we accept already initiatlized instances of concrete implementations for these two.
        # Key thing is that the use case does not know the concrete arguments types because these
        # come from the infra layer.
        self._auctions_repo = auctions_repo
        self._output_boundary = output_boundary

    def execute(self, input_dto: PlacingBidInputDto):

        # Here we get the auction entity and execute place_bid command.
        # The purpose of place_bid command is to change the state of the entity without returning 
        # a value.
        auction = self._auctions_repo.get(input_dto.auction_id)
        auction.place_bid(input_dto.bidder_id, input_dto.amount)
        self._auctions_repo.save(auction)

        # Construct the output dto by executing a query method on the auction entity to determine
        # if it is a winning bid.
        iswinning = input_dto.bidder_id == auction.winner
        output_dto = PlacingBidOutputDto(
            is_winning=iswinning, current_price=auction.current_price)
        self._output_boundary.present(output_dto)


@dataclass(frozen=True)
class PlacingBidInputDto:
    bidder_id: BidderId
    auction_id: AuctionId
    amount: Money


@dataclass(frozen=True)
class PlacingBidOutputDto:
    is_winning: bool
    current_price: Money


class PlacingBidOutputBoundary(abc.ABC):
    @abc.abstractmethod
    def present(self, output_dto: PlacingBidOutputDto):
        pass


class PlacingBidInputBoundary(abc.ABC):
    @abc.abstractmethod
    def execute(self, input_dto: PlacingBidInputDto, presenter: PlacingBidOutputBoundary):
        pass


class PlacingBidWebPresenter(PlacingBidOutputBoundary):
    """Concrete class implementing output boundary interface.
    
    It's job is to convert the output dto to a presentable web format.
    """
    def present(self, output_dto: PlacingBidOutputDto):

        # We do not return anything to the controler (or view) effectively
        # ending the flow, however we could be returning a value.

        self.result = {
            "price": f'${output_dto.current_price.quantize(".01")}',
            "is_winning": "Congrats!" if output_dto.is_winning else "Sorry..."
        }

    def get_presented_data(self) -> dict:

        # Since the formatted data is not returned we need 
        # a way to further fetch the results.
        # Here returned dict is another dto. It's common in various
        # python web frameworks. We could be returning something
        # more sophisticated though.
        return self.result






