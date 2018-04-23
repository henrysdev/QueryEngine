"""
Leader / Follower

n = group_count = sqrt(num_docs)

leaders can be picked at random (pick n leaders)

once you pick the leaders, 

compute the distance between the distance of the remaining docs and relate 
them to the closest leader

distance = cosine similarity
"""
import numpy as np
import math
import random

class Similarity:
    def __init__(self, documents):
        self.documents = documents

    def has_term(self, query_term):
        docs_with_term = []
        for doc in self.documents:
            if query_term in doc.terms:
                docs_with_term.append(doc)
        return docs_with_term

    def cosine_similarity(self, doc1, doc2):
        scores = []
        doc_matrix = np.zeros((doc2.num_total_terms))
        for q, qterm in enumerate(doc2.terms):
            idf = 1 + math.log(len(self.documents) / len(self.has_term(qterm)))
            tf = doc1.terms[qterm]
            normalized_tf = tf / doc1.num_terms
            weighted = normalized_tf * idf
            doc_matrix[q] = weighted
        score = np.square(doc_matrix)
        score = math.sqrt(np.sum(score))

        return score

    def determine_leaders(self):
        # int(math.sqrt(len(self.documents)))
        leaders = [random.choice(self.documents) for x in range(
            int(math.sqrt(len(self.documents))))]
        followers = [x for x in self.documents if x not in leaders]
        for f in followers:
            min_dist = 2
            for l in leaders:
                dist = self.cosine_similarity(f, l)
                if dist < min_dist:
                    print("new min dist: ", dist)
                    print("L: {}".format(l.title))
                    min_dist = dist
                else:
                    print("nope")
            print()

        print("leaders: ", leaders)
        print("followers: ", followers)
        return leaders

    def cosine_scores(self, query_terms):
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