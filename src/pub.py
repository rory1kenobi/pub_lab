from src.customer import Customer
from src.drink import Drink
class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def sell_drink_to_customer(self, drink, customer):
        customer.reduce_wallet(drink.price)
        self.increase_till(drink.price)

    def check_customer_age(self, customer):
        if customer.age >= 21:
            return True
        else:
            return False

    def too_drunk(self, customer):
        if customer.drunkenness_level >= 15:
            return "NAW"
        else:
            self.sell_drink_to_customer
        
        