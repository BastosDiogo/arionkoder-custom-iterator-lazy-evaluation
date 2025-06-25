import logging
from services.mock_payments import Mock
from services.lazy_collection import LazyCollection

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        payment = self._data.filter(lambda p: int(p['created_at'][5:7]) <= month)
        return self.paginate(payment, page, page_size)
