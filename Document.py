class Document:
    def __init__(self, _id):
        self._id = _id
        self.terms = [] # list of tuples (term, tf)

    def add_term(self, term):
        if term in self.terms:
            self.terms[term][1] += 1