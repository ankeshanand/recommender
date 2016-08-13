import heapq
import numpy as np

from src.constants import TARGET_CONTEST_ID

def get_top_k_recommendations(rating_matrix, similarity_matrix, hacker_id, hacker_dict, challenge_dict, challenges_df, k=10):
    print 'Recommending for ' + str(hacker_id)

    inv_challenge_dict = {v: k for k, v in challenge_dict.iteritems()}
    col_idx = hacker_dict[hacker_id]
    user_col = rating_matrix.getcol(col_idx).toarray().flatten()
    df = challenges_df

    rated_item_indexes = [idx for idx, val in enumerate(user_col) if val == 1]
    predicted_ratings = []

    for row_idx, val in enumerate(user_col):
        challenge_id = inv_challenge_dict[row_idx]

        # Ignore the challenge if it is not a part of Target Contest
        if not ((df['challenge_id'] == challenge_id) & (df['contest_id'] == TARGET_CONTEST_ID)):
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



    


    

