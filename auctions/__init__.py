"""
Auction system implemented with clean architecture principles in mind.

===========
Definitions
===========


Layers
======

Layer is a grouping of code. Defines classes, functions and data sctructures
used to perform certain actions needed for that layer. A layer should not care about
implementation details of another layer.

Each layer can only depend (use code) on the layer below.
A layer should not be aware of the layer above.
Eg. domain layer cannot import functions, classes from the infra layer or 
use variables not known to the domain layer.

Control flow: external world -> infrastructure -> application -> domain

* infra uses application
* application uses domain
* infra can use the domain
* domain cannot use infra or application
* application cannot use infra


External world 
--------------

Spans OS, web and all the services used by the project that are not a part of the project.


Infrastructure 
--------------

Contains all the code needed to interact with the external world


Application
-----------

Houses application business rules.
Defines what the project really does by use cases (aka interactors).

Single use case represents an operation leading to a change in the system.
Use case is an operation performed by an actor (person or other system) which is important from 
the business perspective.

This layer also contains interfaces (aka ports) which are abstracting operations / services 
found in the upper layer.


::

    # application/ports/payments.py
    import abc

    class Payments(abc.ABC):
        @abc.abstractmethod
        def make_payment(self, amount: Decimal):
            pass

    # infra/adapters/payments.py
    from application.ports.payments import Payment

    class ConcretePayment(Payment):
        def make_payment(self, amount: Decimal):
            # Here goes implementation
            # for making the payment involving usage
            # of some other library or API calls.


Domain
------

Place for the code enforcing all the business rules.
The code has to be context free, it cannot depend on the upper layers.
Here are all the invariants, entities etc.
Make sure the entities follow `TellDontAsk` principle 
(delegate work to the object and do not care how it is being carried out).


:: 

    # domain/entities/auction.py
    class Auction:
        def place_bid(self, userid: int, amount: Decimal):
            ...

        def withdraw_bid(self, bid_id: int):
            ...

        

Boundaries
==========

They define the way how we communicate with given layer.

Technically it could be a group of functions or classes that are public, an api or a set of interfaces / base
classes defined within a given layer.

In order to pass data between boundaries DTOs are used.

Dto stands for data transfer object
Input and output dtos are used to pass data between layers
and are essential to guarantee correct control flow within the system.
What is important is that dtos should be immutable

::

    @dataclass(frozen=True)
    class EmailDto:
        src: EmailAdress
        replyto: EmailAdress
        body: str

The most important boundary is the application input boundary.
In order to guarantee loose coupling addtional abstraction layer is used
called `input boundary`.
Technically the application layer will consume and input dto and produce output dto.

Other terms used to solve the same problem are request and response concepts.

::

    @dataclass(frozen=True)
    class PlacingBidInputDto:
        bidder_id: int
        auction_id: int
        amount: Decimal

    @dataclass(frozen=True)
    class PlacingBidOutputDto:
        is_winning: bool
        current_price: Decimal

    class PlacingBidInputBoundary:
        @abc.abstractmethod
        def execute(self, request: PlacingBidInputDto):
            ...


"""
