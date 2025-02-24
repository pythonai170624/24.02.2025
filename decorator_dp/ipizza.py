from abc import ABC, abstractmethod

class IPizza(ABC):

    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


# Interface
# draw round shadow

# shape
# rectangle: Shape
# Triangle: Shape
# Circle: Shape, IDrawRound
# Oval: Shape, IDrawRound
