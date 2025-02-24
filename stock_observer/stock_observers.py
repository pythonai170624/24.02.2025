# stock_observer/stock_observers.py
from typing import override

from i_observer import IObserver
from i_subject import ISubject

class StockObserver(IObserver):
    def __init__(self, name: str, subject: ISubject):
        self.name = name
        self.ibm_price = 0.0
        self.apple_price = 0.0
        self.google_price = 0.0
        self.subject = subject
        subject.register(self)

    @override
    def update(self, ibm_price: float, apple_price: float, google_price: float):
        self.ibm_price = ibm_price
        self.apple_price = apple_price
        self.google_price = google_price

        # only if there was a change ....
        self.print_prices()

    def print_prices(self):
        print(f"Observer {self.name} updated: IBM: {self.ibm_price}, Apple: {self.apple_price}, Google: {self.google_price}")

    def __str__(self):
        return f"StockObserver({self.name})"
