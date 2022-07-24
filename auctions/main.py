"""Module connecting application with infrastructure as well as configuration setup."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .infra.repositories import SqliteAuctionsRepository


HERE = os.path.dirname(os.path.abspath(__file__))


def get_db():
    return create_engine('sqlite:///' + get_db_file())


def get_db_file():
    return os.path.join(HERE, 'auctions.sqlite')


def get_session():
    return Session(get_db())


repo = SqliteAuctionsRepository(get_session())