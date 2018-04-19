class Document:
    def __init__(self, title, terms):
        self.title = title,
        self.terms = terms # list of tuples (term, tf)

    def __str__(self):
        print(type(self.title))
        _str = str(self.title)
        for elem in self.terms:
            _str += str(elem)
        return _str