from abc import ABC, abstractmethod
from typing import override

from ipizza import IPizza

class ToppingDecorator(IPizza, ABC):

    def __init__(self, pizza: IPizza):
        self.pizza = pizza

    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

    def __str__(self) -> str:
        return f"PlainPizza [{self.get_details()} {self.get_cost()}]"


