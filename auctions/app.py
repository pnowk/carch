# pylint: disable=all

from dataclasses import dataclass
from decimal import Decimal
import abc


@dataclass(frozen=True)
class PlacingBidInputDto:
    bidder_id: int
    auction_id: int
    amount: Decimal


@dataclass(frozen=True)
class PlacingBidOutputDto:
    is_winning: bool
    current_price: Decimal


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
    def get(self, auction_id):
        ...


class PlacingBidUseCase(PlacingBidInputBoundary):
    """Use case orchestrates the whole business process. """

    def __init__(self, data_access: AuctionsDataAccess, output_boundary: PlacingBidOutputBoundary):

        # Important is how data_access and output_boundary are created.
        # Here we accept already initiatlized instances of concrete implementations for these two.
        # Key thing is that the use case does not know the concrete arguments types because these
        # come from the infra layer.
        self.data_access = data_access
        self.output_boundary = output_boundary

    def execute(self, input_dto: PlacingBidInputDto):

        # Here we get the auction entity and execute place_bid command.
        # The purpose of place_bid command is to change the state of the entity without returning 
        # a value.
        auction = self.data_access.get(input_dto.auction_id)
        auction.place_bid(input_dto.bidder_id, input_dto.amount)
        self.data_access.save(auction)

        # Construct the output dto by executing a query method on the auction entity to determine
        # if it is a winning bid.
        output_dto = PlacingBidOutputDto(input_dto.bidder_id in auction.winners, auction.current_price)
        self.output_boundary.present(output_dto)









