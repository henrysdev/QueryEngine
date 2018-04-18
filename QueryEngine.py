class QueryEngine:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def handle_query(self, query):
        query_terms = query.split()
        if query_terms[0] == "stop":
            exit(0)
        query_terms = [x for x in query_terms if x in dictionary]


def menu(query_engine):
    print("Welcome to Henry's Query Engine.\nEnter a query below. ")
    while True:
        query = input("> ")
        if query is not None:
            query_engine.handle_query(query)

if __name__ == "__main__":
    dictionary = {"ok":"ko", "hello":"ab"}
    query_engine = QueryEngine(dictionary)
    menu(query_engine)