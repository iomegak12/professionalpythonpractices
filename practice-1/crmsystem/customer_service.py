from crmsystem.decorators import LogProvider


class CustomerService:
    def __init__(self):
        super().__init__()

    @LogProvider(pre=True, post=True)
    def getCustomers(self):
        customers = [
            {"id": 10, "name": "Northwind", "address": "Bangalore"},
            {"id": 11, "name": "Southwind", "address": "Bangalore"},
            {"id": 12, "name": "Westwind", "address": "Bangalore"},
            {"id": 13, "name": "Adventureworks", "address": "Bangalore"},
            {"id": 14, "name": "Footmart", "address": "Chennai"},
        ]

        return customers
