import numpy as np

class Document:
    def __init__(self, title, url, terms, vect, _id):
        self.title = str(title)
        self.url = str(url)
        self.terms = terms
        self.num_terms = sum(self.terms.values())
        self.num_total_terms = len(self.terms.keys())
        self.vect = vect
        self._id = _id

    def __str__(self):
        _str = str(self.title)
        _str += str(self.url)
        return _str