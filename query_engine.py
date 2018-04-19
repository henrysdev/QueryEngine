import sys
from database import Database

class QueryEngine:
    def __init__(self, path_to_tfcsv):
        self.database = Database(path_to_tfcsv)
        self.dictionary = self.database.get_dictionary()

    def handle_query(self, query):
        query_terms = query.split()
        if query_terms[0] == "stop":
            exit(0)
        query_terms = [x for x in query_terms if x in self.dictionary]
        if not query_terms:
            print("No results for the given query")


def menu(query_engine):
    print("Welcome to Henry's Query Engine.\nEnter a query below. ")
    while True:
        query = input("> ")
        if query is not None:
            query_engine.handle_query(query)


if __name__ == "__main__":
    if (len(sys.argv)) == 2:
        path_to_tfcsv = sys.argv[1]
        query_engine = QueryEngine(path_to_tfcsv)
        menu(query_engine)