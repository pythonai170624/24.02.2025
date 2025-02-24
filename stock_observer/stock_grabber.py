# stock_observer/stock_grabber.py
from typing import override

from i_subject import ISubject
from i_observer import IObserver

class StockGrabber(ISubject):
    def __init__(self):
        self.observers = []
        self.ibm_price = 0.0
        self.apple_price = 0.0
        self.google_price = 0.0

    @override
    def register(self, observer: IObserver):
        self.observers.append(observer)
        print(f"{observer} is registered.")

    @override
    def unregister(self, observer: IObserver):
        self.observers.remove(observer)
        print(f"{observer} is no longer registered.")

    @override
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.ibm_price, self.apple_price, self.google_price)

    def set_ibm_price(self, price: float):
        self.ibm_price = price
        self.notify_observers()

    def set_apple_price(self, price: float):
        self.apple_price = price
        self.notify_observers()

    def set_google_price(self, price: float):
        self.google_price = price
        self.notify_observers()
