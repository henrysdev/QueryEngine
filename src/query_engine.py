import sys

from database import Database
from similarity import Similarity

class QueryEngine:
    def __init__(self, path_to_tfcsv):
        self.database = Database(path_to_tfcsv)
        self.dictionary = self.database.get_dictionary()
        self.similarity = Similarity(self.database.documents)
        self.rank_limit = 6
        self.num_leaders = 5
        self.similarity.k_means_cluster(self.num_leaders)

    def handle_query(self, query):
        query = query.lower()
        query_terms = query.split()
        if query_terms[0] == "stop":
            exit(0)
        query_terms = [x for x in query_terms if x in self.dictionary]
        if not query_terms:
            print("No results for the given query")
        ranked_results = sorted(self.similarity.cosine_scores(query_terms), 
                                key=lambda x: x[1], reverse=True)
        print("\nQUERY RESULTS: ")
        print("--------------------------------------")
        for i, res in enumerate(filter(lambda x: x[1] > 0, ranked_results)):
            if i < self.rank_limit:
                doc_title = res[0]
                cos_score = res[1]
                doc_url = self.database.get_url(doc_title)
                print("[{}] {}\n{}\n(cosine_score={})".format(
                    i+1,
                    doc_title,
                    doc_url,cos_score))
                print("--------------------------------------")
        print()


def menu(query_engine):
    print("\n*******************************************************")
    print("          Welcome to Henry's Query Engine.")
    print("*******************************************************")
    print("\nEnter a query below. ")
    while True:
        query = input("> ")
        if query is not None:
            query_engine.handle_query(query)


if __name__ == "__main__":
    if (len(sys.argv)) == 2:
        path_to_tfcsv = sys.argv[1]
        query_engine = QueryEngine(path_to_tfcsv)
        menu(query_engine)