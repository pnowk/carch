# pylint: disable=all

import inject

from .app import AuctionsDataAccess, PlacingBidOutputBoundary, PlacingBidWebPresenter
from .infra import DbAuctionsDataAccess


def di_config(binder: inject.Binder):
    binder.bind(AuctionsDataAccess, DbAuctionsDataAccess())

    binder.bind_to_provider(PlacingBidOutputBoundary, PlacingBidWebPresenter)



def main():
    print('Configuring auctions.')
    inject.configure(di_config)

