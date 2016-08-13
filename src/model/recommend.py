import heapq
import numpy as np

def get_top_k_recommendations(rating_matrix, similarity_matrix, hacker_id, hacker_dict, challenge_dict, k=10):
    print 'Recommending for ' + str(hacker_id)
    col_idx = hacker_dict[hacker_id]
    user_col = rating_matrix.getcol(col_idx).toarray().flatten()

    rated_item_indexes = [idx for idx, val in enumerate(user_col) if val == 1]
    predicted_ratings = []
    for row_idx, val in enumerate(user_col):
        if val != 1:
            similarities = []
            for idx in rated_item_indexes:
                similarities.append(similarity_matrix[row_idx, idx])

            most_similar_items = heapq.nlargest(3, similarities)
            predicted_ratings.append((np.mean(most_similar_items), row_idx))

    inv_challenge_dict = {v: k for k, v in challenge_dict.iteritems()}
    
    recommendations = [inv_challenge_dict[row_idx] for score, row_idx in heapq.nlargest(k, predicted_ratings)]
    return recommendations



    


    

