from src.customer import Customer
from src.drink import Drink
class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = ["Blue Dragon"]

    def increase_till(self, amount):
        self.till += amount

    def sell_drink_to_customer(self, drink, customer):
        customer.reduce_wallet(drink.price)
        self.increase_till(drink.price)
        