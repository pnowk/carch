"""Place for value objects.

Value Objects are used to express subtleties of reality.
"""

# pylint: disable=all
import inspect
from typing import Type
from decimal import Decimal, DecimalException


# Type aliases.
# Eg. few places in the code need to be aware that these are in fact integers.
AuctionId = int
BidderId = int


class Currency:
    precision = 2
    symbol = None


class USD(Currency):
    symbol = "$"


class PLN(Currency):
    symbol = 'PLN'


# Should be immutable
# Disallows instance creation with incorrect state eg. Money('hello')
# Signifies value, not identity.
# Instances with the same amount are considered equal.
# Likwise Decimal, it should support arithmetics operations.
class Money(Currency):

    def __init__(self, currency: Type[Currency], amount: str) -> None:
        iscurrency = inspect.isclass(currency) and issubclass(currency, Currency)

        # Check currency type
        if not iscurrency:
            raise ValueError(f'{currency} is not of type Currency.')

        # Check amount type
        try:
            amount = Decimal(amount)
        except DecimalException:
            raise ValueError(f'{amount} is not valid.')


        self._currency = currency
        self._amount = Decimal(amount)

    @property
    def currency(self) -> Type[Currency]:
        return self._currency

    @property
    def amount(self) -> Decimal:
        return self._amount

    def __eq__(self, o: 'Money') -> bool:
        return self.amount == o.amount and self.symbol == o.symbol
