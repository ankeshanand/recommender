import heapq
import numpy as np
import pandas as pd

class Recommendations(object):
    INSTANCE = None
    valid_challenges = set([])
    target_contest_id = ''
    challenges_file = ''

    def __init__(self, target_contest_id, challenges_file):
        Recommendations.target_contest_id = target_contest_id
        Recommendations.challenges_file = challenges_file
        self.find_valid_challenges()

    @classmethod
    def find_valid_challenges(cls):
        df = pd.read_csv(cls.challenges_file)
        challenges = df['challenge_id'].tolist()

        for c in challenges:
            if ((df['challenge_id'] == c) & (df['contest_id'] == cls.target_contest_id)).any():
                cls.valid_challenges.add(c)

    @classmethod
    def get_instance(cls, target_contest_id, challenges_file):
        if not cls.INSTANCE:
            cls.INSTANCE = Recommendations(target_contest_id, challenges_file)
        return cls.INSTANCE


    def get_top_k_recommendations(self, rating_matrix, similarity_matrix, hacker_id, hacker_dict, challenge_dict, k=10):
        print 'Recommending for ' + str(hacker_id)

        inv_challenge_dict = {v: k for k, v in challenge_dict.iteritems()}
        col_idx = hacker_dict[hacker_id]
        user_col = rating_matrix.getcol(col_idx).toarray().flatten()

        rated_item_indexes = [idx for idx, val in enumerate(user_col) if val == 1]
        predicted_ratings = []

        for row_idx, val in enumerate(user_col):
            challenge_id = inv_challenge_dict[row_idx]

            # Ignore the challenge if it is not a part of Target Contest
            if challenge_id not in self.valid_challenges:
                continue 

            if val != 1:
                similarities = []
                for idx in rated_item_indexes:
                    similarities.append(similarity_matrix[row_idx, idx])

                most_similar_items = heapq.nlargest(3, similarities)
                predicted_ratings.append((np.mean(most_similar_items), row_idx))

        inv_challenge_dict = {v: k for k, v in challenge_dict.iteritems()}

        recommendations = [inv_challenge_dict[row_idx] for score, row_idx in heapq.nlargest(k, predicted_ratings)]
        return recommendations



    


    

