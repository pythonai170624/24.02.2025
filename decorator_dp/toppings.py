from topping_decorator import ToppingDecorator

class TomatoTopping(ToppingDecorator):
    def get_details(self) -> str:
        return f"{self.pizza.get_details()} Tomato"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 4

# IPrint, Printable, Runnable, Callable
class MozzarellaTopping(ToppingDecorator):
    def get_details(self) -> str:
        return f"{self.pizza.get_details()} Mozzarella"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 5

class PineappleTopping(ToppingDecorator):
    def get_details(self) -> str:
        return f"{self.pizza.get_details()} Pineapple"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 7

class ToppingHalfPrice(ToppingDecorator):
    def get_details(self) -> str:
        return f"{self.pizza.get_details()} discount 50%"

    def get_cost(self) -> float:
        return self.pizza.get_cost() / 2