import math
import numpy as np
import random

class Similarity:
    def __init__(self, documents):
        self.documents = documents

    def has_term(self, query_term):
        """ finds and returns documents containing given term """
        docs_with_term = []
        for doc in self.documents:
            if query_term in doc.terms:
                docs_with_term.append(doc)
        return docs_with_term

    def distance(self, a, b, ax=0):
        """ calculates euclidean distance between two vectors """
        return np.linalg.norm(a - b, axis=ax)

    def k_means_cluster(self, k):
        """ generates k-means cluster groups """
        leaders = random.sample(self.documents, k)
        cluster_map = {}
        print("\nLeaders (doc id | doc title)")
        for l in leaders:
            print(l._id, "|", l.title)
            cluster_map[l._id] = []

        print("\nFollowers (doc id | doc title)")
        followers = [x for x in self.documents if x not in leaders]
        for f in followers:
            print(f._id, "|", f.title)

        for f in followers:
            dists = []
            for l in leaders:
                dist = self.distance(f.vect, l.vect)
                dists.append( (l._id, dist) )
            _min = dists[0]
            for d in dists:
                #print("f:", f._id, "d:", d)
                if d[1] < _min[1]:
                    _min = d
            cluster_map[_min[0]].append((f._id, _min[1]))

        print("\nClusters (leader id -> [follower id | score])")
        for lead_id in cluster_map:
            print("Cluster w/ Leader id:", lead_id)
            followers = cluster_map[lead_id]
            if not followers:
                print("(none)")
            for f_pair in followers:
                print("[", f_pair[0], "|", f_pair[1], "]")
            print("-------------------------------")

    def cosine_scores(self, query_terms):
        """ calculates tf-idf scores using ntc.nnn weighting """
        scores = []
        doc_matrix = np.zeros((len(self.documents),len(query_terms)))
        # container for docs who have had the 0.25 title term bonus added
        query_in_title = []
        for q, qterm in enumerate(query_terms):
            idf = 1 + math.log(len(self.documents) / len(self.has_term(qterm)))
            for d, doc in enumerate(self.documents):
                tf = doc.terms[qterm]
                normalized_tf = tf / doc.num_terms
                weighted = normalized_tf * idf
                # add 0.25 to score if the title shares terms with the query
                if qterm in doc.title.lower():
                    if doc.title not in query_in_title:
                        weighted += 0.25
                        query_in_title.append(doc.title)
                doc_matrix[d,q] = weighted
                
        for i, row in enumerate(doc_matrix):
            row = np.square(row)
            sqrt_sum_row = math.sqrt(np.sum(row))
            scores.append((str(self.documents[i].title), sqrt_sum_row))

        return scores