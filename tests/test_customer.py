import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Rory Smith", 1000.00, 25, 25)

    def test_customer_has_name(self):
        self.assertEqual("Rory Smith", self.customer.name)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(8.00)
        self.assertEqual(992.00, self.customer.wallet)

    def test_mad_with_it_level(self):
        self.customer.increase_mad_with_it(25)
        self.assertEqual(50, self.customer.drunkenness_level)

