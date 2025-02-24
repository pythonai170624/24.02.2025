from typing import override

from ipizza import IPizza

class PlainPizza(IPizza):

    @override
    def get_details(self) -> str:
        return "Plain dough and spices"

    @override
    def get_cost(self) -> float:
        return 20.0

    def __str__(self) -> str:
        return f"PlainPizza [{self.get_details()} {self.get_cost()}]"
