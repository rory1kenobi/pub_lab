import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = ("Blue Dragon", 8.00)
        self.drink_2 = ("green Dragon", 6.50)
        self.customer_1 = Customer("Rory Smith", 100.00, 25, 25)
        self.customer_2 = Customer("Daniel Green", 60.00, 17, 20)
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(8.00)
        self.assertEqual(108.00, self.pub.till)

    def test_buy_drink_from_pub(self):
        customer = Customer("Rory Smith", 1000, 25, 25)
        drink = Drink("Blue Dragon", 8.00)
        self.pub.sell_drink_to_customer(drink, customer)
        self.assertEqual(992.0, customer.wallet)
        self.assertEqual(108.0, self.pub.till)

    def test_check_customer_age(self):
        test1 = self.pub.check_customer_age(self.customer_1)
        self.assertTrue(test1)
        test2 = self.pub.check_customer_age(self.customer_2)
        self.assertFalse(test2)

    def test_too_drunk(self):
        customer_3 = Customer("fred", 200, 46, 30)
        self.pub.too_drunk(customer_3)
        self.assertTrue(customer_3)

   




    