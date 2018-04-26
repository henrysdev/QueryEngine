import csv
import numpy as np

from document import Document

class Database:
    def __init__(self, path):
        self.id_counter = 0
        self.documents = self.read_in_data(path)

    def read_in_data(self, path):
        documents = []
        with open(path) as file_in:
            reader = csv.reader(file_in, skipinitialspace=True, quotechar="'")
            # grab all the term headers from the first row (exclude the first one at is a label)
            terms = next(reader)[2:]
            for row in reader:
                termvect = np.asarray([int(x) for x in row[2:]])
                # create tuples of (term, term-frequency)
                tpairs = dict(zip(terms[2:],[int(x) for x in row[2:]]))
                newDoc = Document(title=row[0].replace('"',''), 
                                  url=row[1].replace('"',''), 
                                  terms=tpairs,
                                  vect=termvect,
                                  _id=self.id_counter)
                documents.append(newDoc)
                self.id_counter += 1

        return documents

    def get_url(self, doc_title):
        for i, elem in enumerate(self.documents):
            if elem.title == doc_title:
                return elem.url

    def get_dictionary(self):
        return [x for x in self.documents[0].terms]

    def __str__(self):
        _str = "-- DATABASE --"
        for doc in self.documents:
            _str += str(doc)
        _str += "-------------"
        return _str