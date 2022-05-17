import math
from src.chain.dispense_interface import IDispenser


class Dispense20(IDispenser):
    def __init__(self):
        self._dispense = None

    def next_chain(self, chain):
        self._dispense = chain

    def dispense(self, value):
        if value >= 20:
            num = math.trunc(value / 20)
            remainder = value % 20
            print("Dispensing 20 = " + str(num))
            if remainder != 0:
                self._dispense.dispense(remainder)
        else:
            self._dispense.dispense(value)
