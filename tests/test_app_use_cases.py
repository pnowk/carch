
from auctions.app import PlacingBidOutputBoundary, PlacingBid
from auctions.domain import Auction
from auctions.app.use_cases import PlacingBidInputDto, PlacingBidOutputDto
from auctions.domain import Money, USD
from tests.fakes import FakeAuctionsRepository
from mock import Mock


def test_presents_winning_10_usd_price_when_higher_bid_placed():
    output_boundary_mock = Mock(spec_set=PlacingBidOutputBoundary)
    repo = FakeAuctionsRepository()
    repo.save(Auction(auction_id=1, starting_price=Money(USD, "9.99"), bids=[]))

    usecase = PlacingBid(
        output_boundary=output_boundary_mock,
        auctions_repo=repo
    )
    price = Money(USD, "10.00")
    input_dto = PlacingBidInputDto(
        bidder_id=1, auction_id=1, amount=price
    )

    usecase.execute(input_dto)

    output = PlacingBidOutputDto(is_winning=True, current_price=price)
    output_boundary_mock.present.assert_called_once_with(output)

