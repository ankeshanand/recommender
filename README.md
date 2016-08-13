# recommender
A Python based recommendation engine for HackerRank challenges.

##Algorithm
We assume that if a hacker has taken out time to attempt and submit a solution to a challenge, he/she is interested in that challenge. 

We use **item-item collaborative filtering** to recommend new challenges to a hacker. The rationale behind using item-item collaborative filtering is as follows:

* Item-Item collaborative filtering works well in systems that have more users than items. Item-item models use rating distributions per item, not per user.
* The model is more stable since average item ratings change less often average user ratings.
* Computing similarities between all pairs of users is expensive. 
* Challenges dont't have enough metadata associated with them for us to create a powerful content based recommendation model.

## Evaluation Ideas:
There are several ways in which we can evaluate the model:
* **User Signals**: A/B tests between different models based on user feedback.
* **RMSE**: We can divde the dataset into a train-test split and try to predict the ratings on the test dataset. The RMSE can then be calculated using the ground truth. 
* **Precision and Recall**: Modelling the prediction process as a binary operation--either items are predicted (good) or not (bad). We can again perform this evaluation on a test-train split.

## Dependencies:
* pandas
* numpy
* scipy

## Usage:
* Make sure you have the dependencies installed.
* Run `python src\api.py`

## Project Structure

    |-- data                              <-- Raw dataset files
    |   |-- challenges.csv
    |   |-- submissions.csv
    |-- README.md
    |-- src                               <-- All the source code resides here
    |   |-- api.py                        <-- Driver Program
    |   |-- constants.py                  <-- Constants being used in the project
    |   |-- data                          
    |   |   |-- __init__.py
    |   |   |-- prepare_data.py           <-- Utilites to create rating matrix and item similarity matrix
    |   |-- __init__.py
    |   `-- model
    |       |-- __init__.py
    |       |-- recommend.py              <- Classes and Methods to get recommendations

