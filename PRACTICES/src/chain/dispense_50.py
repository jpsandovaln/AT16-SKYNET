import math
from src.chain.dispense_interface import IDispenser


class Dispense50(IDispenser):
    def __init__(self):
        self._dispense = None

    def next_chain(self, chain):
        self._dispense = chain

    def dispense(self, value):
        if value >= 50:
            num = math.trunc(value / 50)
            remainder = value % 50
            print("Dispensing 50 = " + str(num))
            if remainder != 0:
                self._dispense.dispense(remainder)
        else:
            self._dispense.dispense(value)
