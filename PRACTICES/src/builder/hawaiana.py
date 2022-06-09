from src.builder.builder_pizza import BuilderPizza
from src.builder.pizza import Pizza


class Hawaiana(BuilderPizza):
    def __init__(self):
        self.pizza = Pizza()
        self.pizza.set_dough("soft")
        self.pizza.set_sauce("sweet")
        self.pizza.set_cheese("mozarella")

    def with_ham(self, ham):
        self.pizza.set_ham(ham)
        return self

    def with_pineapple(self, pineapple):
        self.pizza.set_pineapple(pineapple)
        return self

    def build(self):
        return self.pizza
