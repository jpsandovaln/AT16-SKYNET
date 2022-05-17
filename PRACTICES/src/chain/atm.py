from src.chain.dispense_100 import Dispense100
from src.chain.dispense_50 import Dispense50
from src.chain.dispense_20 import Dispense20
from src.chain.dispense_10 import Dispense10


class ATM:
    def __init__(self, value):
        self.value = value

    def get_money(self):
        """
        if self.value >= 100:
            data = Dispense100()
            self.value = data.dispense(self.value)
        if self.value >= 50:
            data = Dispense50()
            self.value = data.dispense(self.value)
        if self.value >= 20:
            data = Dispense20()
            self.value = data.dispense(self.value)
        if self.value >= 10:
            data = Dispense10()
            self.value = data.dispense(self.value)
        print("Reminder = " + str(self.value))
        """
        dispense100 = Dispense100()
        dispense50 = Dispense50()
        dispense20 = Dispense20()
        dispense10 = Dispense10()

        dispense100.next_chain(dispense50)
        dispense50.next_chain(dispense20)
        dispense20.next_chain(dispense10)

        dispense100.dispense(self.value)
