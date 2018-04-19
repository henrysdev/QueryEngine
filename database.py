import csv
from document import Document

class Database:
    def __init__(self, path):
        self.documents = self.read_in_data(path)

    def read_in_data(self, path):
        documents = []
        with open(path) as file_in:
            reader = csv.reader(file_in, skipinitialspace=True, quotechar="'")
            # grab all the term headers from the first row (exclude the first one at is a label)
            terms = next(reader)[1:]
            for row in reader:
                # create tuples of (term, term-frequency)
                tpairs = list(zip(terms[1:],row[1:]))
                newDoc = Document(title=row[0], terms=tpairs)
                documents.append(newDoc)
        return documents

    def get_dictionary(self):
        return [x[0] for x in self.documents[0].terms]

    def __str__(self):
        _str = "-- DATABASE --"
        for doc in self.documents:
            _str += str(doc)
        _str += "-------------"
        return _str