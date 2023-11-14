import pizza

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

from pizza import make_pizza

make_pizza(18, "mozzarella")

from pizza import make_pizza as mp

mp(19, "red peppers", "feta cheese")

import pizza as p

p.make_pizza(20, "tomato sauce", "pepperoni", "cheese")

from pizza import *

make_pizza(21, "white sauce")
