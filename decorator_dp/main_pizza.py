
from plain_pizza import PlainPizza
from toppings import *

plain_pizza = PlainPizza()

pizza_with_tomato = TomatoTopping(plain_pizza)
print(plain_pizza)

print(pizza_with_tomato.get_cost())
print(pizza_with_tomato.get_details())

hawaiian_pizza = PineappleTopping(pizza_with_tomato)
print(hawaiian_pizza)

mozzarella_pineapple_pizza = MozzarellaTopping(PineappleTopping(PlainPizza()))

options = {'1': 'tomato', '2': 'pineapple', '3': 'mozzarella', '4': 'bye'}
current_pizza = plain_pizza
print('now pizza is:', current_pizza)
while True:
    choice = input('what topping? [1] Tomato [2] Pineapple [3] Mozzarella [4] bye')
    match options[choice]:
        case 'tomato': current_pizza = TomatoTopping(current_pizza)
        case 'pineapple': current_pizza = PineappleTopping(current_pizza)
        case 'mozzarella': current_pizza = MozzarellaTopping(current_pizza)
        case 'bye':
            break
        case _: print('unknown topping ...')
    print('now pizza is:', current_pizza)



















