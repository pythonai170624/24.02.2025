# stock_observer/i_subject.py

from abc import ABC, abstractmethod
from typing import List
from i_observer import IObserver

class ISubject(ABC):
    @abstractmethod
    def register(self, observer: IObserver):
        pass

    @abstractmethod
    def unregister(self, observer: IObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# 100 * 3 = 300
#  70 * 3 = 210
# 110 * 3 = 330
# 300



