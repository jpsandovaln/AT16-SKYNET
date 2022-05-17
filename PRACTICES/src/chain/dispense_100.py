import math
from src.chain.dispense_interface import IDispenser


class Dispense100(IDispenser):
    def __init__(self):
        self._dispense = None

    def next_chain(self, chain: IDispenser):
        self._dispense = chain

    def dispense(self, value):
        if value >= 100:
            num = math.trunc(value / 100)
            remainder = value % 100
            print("Dispensing 100 = " + str(num))
            if remainder != 0:
                self._dispense.dispense(remainder)
        else:
            self._dispense.dispense(value)
