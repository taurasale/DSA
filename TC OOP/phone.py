from item import Item
import csv

class Phone(Item):          # Cia yra inheritance pvz. Jis paveldi viska is Item klases
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #Call to super function to have access to have access to all attributes/ methods
        super().__init__(
            name, price, quantity)
        # Run validations to the received argumets
        assert broken_phones >= 0, f'Q {broken_phones} is not greater than zero!'

        # Assign to self object
        self.broken_phones = broken_phones