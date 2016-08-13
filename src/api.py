import pandas as pd

from data.prepare_data import create_rating_matrix, get_item_similarity_matrix
from model.recommend import get_top_k_recommendations
from constants import CHALLENGES_FILE, SUBMISSIONS_FILE


if __name__ == '__main__':
    rating_matrix, hacker_dict, challenge_dict = create_rating_matrix(CHALLENGES_FILE, SUBMISSIONS_FILE)
    similarity_matrix = get_item_similarity_matrix(rating_matrix)
    challenges_df = pd.read_csv(CHALLENGES_FILE)

    print 'Getting Recommendations'
    for hacker_id in hacker_dict:
        print get_top_k_recommendations(rating_matrix, similarity_matrix, hacker_id, hacker_dict, challenge_dict, challenges_df)

