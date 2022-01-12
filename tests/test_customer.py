import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Rory Smith", 1000.00)

    def test_customer_has_name(self):
        self.assertEqual("Rory Smith", self.customer.name)

    def test_pay_till(self):
        self.customer.pay_till(8.00)
        self.assertEqual(992.00, self.customer.wallet)
