from src.builder.builder_pizza import BuilderPizza
from src.builder.pizza import Pizza


class Napolitana(BuilderPizza):
    def __init__(self):
        self.pizza = Pizza()
        self.pizza.set_dough("soft")
        self.pizza.set_sauce("spicy")
        self.pizza.set_cheese("cheddar")
        self.pizza.set_olive("green")
        self.pizza.set_basil(1)
        self.pizza.set_tomato(1)

    def with_basil(self, basil):
        self.pizza.set_basil(basil)
        return self

    def build(self):
        return self.pizza

