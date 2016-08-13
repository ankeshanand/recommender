import pandas as pd
import numpy as np

from scipy.sparse import csr_matrix, coo_matrix

def create_rating_matrix(challenges_file_loc, submissions_file_loc):
    #challenges_df = pd.read_csv(challenges_file_loc)
    print 'Reading submissions.csv'
    submissions_df = pd.read_csv(submissions_file_loc)

    data, rows, cols = [], [], []
    hacker_dict, challenge_dict = {}, {}
    rowcols = set([])

    print 'Creating Sparse Matrix'
    for idx, row in submissions_df.iterrows():
        hacker_id, challenge_id = row['hacker_id'], row['challenge_id']

        if hacker_id not in hacker_dict:
            hacker_dict[hacker_id] = len(hacker_dict)

        if challenge_id not in challenge_dict:
            challenge_dict[challenge_id] = len(challenge_dict)

        row_idx, col_idx = challenge_dict[challenge_id], hacker_dict[hacker_id]

        if (row_idx, col_idx) not in rowcols:
            rows.append(row_idx)
            cols.append(col_idx)
            data.append(1)
            rowcols.add((row_idx, col_idx))

    shape = (len(challenge_dict), len(hacker_dict))
    data = np.array(data)
    matrix = coo_matrix((data, (rows, cols)), shape=shape)
    print matrix
    print matrix.get_shape()
    print matrix.data
    matrix = matrix.tocsr()
    print matrix
    print matrix.data
    print matrix.toarray()
    return matrix, hacker_dict, challenge_dict


def get_item_similarity_matrix(rating_matrix):
    print 'Creating Item similarity matrix'
    n_items = rating_matrix.get_shape()[0]
    similarity_matrix = np.zeros((n_items, n_items))
    count = 0
    A = rating_matrix.astype(np.int64)
    print A.shape
    m = sparse_corrcoef(A)
    print m.shape
    return m

    for i in xrange(n_items):
        if count % 100 == 0:
            print count
        count += 1
        vector_i = rating_matrix.getrow(i).toarray().flatten()
        #print vector_i
        #print vector_i.shape
        for j in xrange(n_items):
            if similarity_matrix[j][i] != 0:
                similarity_matrix[i][j] = similarity_matrix[j][i]
                continue
            vector_j = rating_matrix.getrow(j).toarray().flatten()
            similarity_matrix[i][j] = np.corrcoef(vector_i, vector_j)[0,1]

    return similarity_matrix

def sparse_corrcoef(A, B=None):

    A = A.astype(np.float64)

    # compute the covariance matrix
    # (see http://stackoverflow.com/questions/16062804/)
    A = A - A.mean(1)
    norm = A.shape[1] - 1.
    C = A.dot(A.T.conjugate()) / norm

    # the correlation coefficients are given by
    # C_{i,j} / sqrt(C_{i} * C_{j})
    d = np.diag(C)
    coeffs = C / np.sqrt(np.outer(d, d))

    return coeffs




