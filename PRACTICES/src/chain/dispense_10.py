import math
from src.chain.dispense_interface import IDispenser


class Dispense10(IDispenser):
    def __init__(self):
        self._dispense = None

    def next_chain(self, chain):
        self._dispense = chain

    def dispense(self, value):
        if value >= 10:
            num = math.trunc(value / 10)
            remainder = value % 10
            print("Dispensing 10 = " + str(num))
            if remainder != 0:
                print("reminder = " + str(remainder))
