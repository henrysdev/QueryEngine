class Document:
    def __init__(self, title, url, terms):
        self.title = str(title)
        self.url = str(url)
        self.terms = terms
        self.num_terms = sum(self.terms.values())
        self.num_total_terms = len(self.terms.keys())

    def __str__(self):
        _str = str(self.title)
        _str += str(self.url)
        for elem in self.terms:
            _str += str(elem)
        return _str