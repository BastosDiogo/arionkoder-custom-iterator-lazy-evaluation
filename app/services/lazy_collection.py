from functools import reduce
from itertools import islice

class LazyCollection:
    def __init__(self, iterable):
        self._iterable = iterable

    def map(self, func):
        return LazyCollection(map(func, self._iterable))

    def filter(self, func):
        return LazyCollection(filter(func, self._iterable))

    def reduce(self, func, initial=None):
        if initial is not None:
            return reduce(func, self._iterable, initial)
        return reduce(func, self._iterable)

    def chunk(self, size):
        def generator():
            it = iter(self._iterable)
            while chunk := list(islice(it, size)):
                yield chunk
        return LazyCollection(generator())

    def paginate(self, data:list, page: int, page_size: int):
        data = self.to_list()
        total_items = len(data)
        total_pages = (total_items + page_size - 1) // page_size

        slice_page = lambda data, p, ps: data[(p - 1) * ps : p * ps]

        if page < 1 or page > total_pages:
            return {
                "items": [],
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages,
                "total_items": total_items,
                "message": "Ther are no more objects."
            }

        return {
            "items": slice_page(data, page, page_size),
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
            "total_items": total_items
        }

    def to_list(self):
        return list(self._iterable)
