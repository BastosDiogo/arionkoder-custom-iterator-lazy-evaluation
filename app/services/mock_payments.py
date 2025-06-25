import random
from uuid import uuid1
from datetime import datetime


class Mock:
    """Class that simulate a NoSQL database as MongoDB or Maria DB."""

    @property
    def random_date(self):
        """Generate random date 'YYYY-MM-DD'."""
        return datetime(2025, random.randrange(1,7), random.randrange(1,20)).strftime('%Y-%m-%d')


    def payments(self):
        """Simulate a bunch of payments"""
        num_max_payments = random.randrange(10, 16)
        index = 1
        payments = []

        while index < num_max_payments:
            payments.append(
                {
                    'id': str(uuid1()),
                    "status" : "aproved",
                    "payment" : round(random.uniform(2000.99, 5000.99),2),
                    "client": {
                        "cnpj": str(random.randrange(11111111111111,22222222222222)),
                        "name": f"COMPANY {index}"
                    },
                    "created_at" : self.random_date
                }
            )
            index += 1

        return payments