import sys
from database import Database
from similarity import Similarity

class QueryEngine:
    def __init__(self, path_to_tfcsv):
        self.database = Database(path_to_tfcsv)
        self.dictionary = self.database.get_dictionary()
        self.similarity = Similarity(self.database.documents)

    def handle_query(self, query):
        query = query.lower()
        query_terms = query.split()
        if query_terms[0] == "stop":
            exit(0)
        query_terms = [x for x in query_terms if x in self.dictionary]
        if not query_terms:
            print("No results for the given query")
        #self.similarity.determine_leaders()
        ranked_results = sorted(self.similarity.cosine_scores(query_terms), 
                                key=lambda x: x[1], reverse=True)
        print("\nQUERY RESULTS: ")
        print("--------------------------------------")
        for i, res in enumerate(filter(lambda x: x[1] > 0, ranked_results)):
            print("[{}] {}\n(cosine_score={})".format(i+1,res[0],res[1]))
            print("--------------------------------------")
        print()


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