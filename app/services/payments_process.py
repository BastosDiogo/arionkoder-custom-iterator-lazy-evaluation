from services.mock_payments import Mock
from services.lazy_collection import LazyCollection

class Payments:
    """Class to process and manage payments."""

    def __init__(self):
        self._data = LazyCollection(Mock().payments())

    def paginate(self, collection: LazyCollection, page: int, page_size: int):
        """Paginate any lazy collection."""
        return collection.paginate(collection, page, page_size)

    def all_payments(self, page:int, page_size:int):
        """Return all payments as LazyCollection."""
        return self.paginate(self._data, page, page_size)

    def created_before_month(self, month: int, page: int, page_size: int):
        """Filter payments created before or in a given month."""
        payment = self._data.filter(lambda payment: int(payment['created_at'][5:7]) <= month)
        return self.paginate(payment, page, page_size)

    def payment_groups(self, group_size:int, page:int, page_size:int):
        """Divide return payments into groups."""
        payments = self._data.chunk(group_size)
        return self.paginate(payments, page, page_size)

    def trimestal_payments(self):
        """Return payments per trimestre."""
        trimestral = {
            'jan_to_mar': {'payments': []},
            'abr_to_jun': {'payments': []}
        }

        payments_jan_to_mar = self._data.filter(lambda payment: int(payment['created_at'][5:7]) <= 3).to_list()
        payments_abr_to_jun = self._data.filter(lambda payment: 4 <= int(payment['created_at'][5:7]) <= 6).to_list()
        trimestral['jan_to_mar']['payments'] = payments_jan_to_mar
        trimestral['abr_to_jun']['payments'] = payments_abr_to_jun

        return trimestral
