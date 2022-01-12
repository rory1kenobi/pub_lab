import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(8.00)
        self.assertEqual(108.00, self.pub.till)

    def buy_drink_from_pub(self):
        customer = Customer("Rory Smith", 1000)
        drink = Drink("Blue Dragon", 8.00)
        self.pub.sell_drink_to_customer(drink, customer)
        self.assertEqual(992.0, customer.wallet)
        self.assertEqual(108.0, self.pub.till)

    