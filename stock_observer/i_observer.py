# stock_observer/i_observer.py

from abc import ABC, abstractmethod

class IObserver(ABC):
    @abstractmethod
    def update(self, ibm_price: float, apple_price: float, google_price: float):
        pass
