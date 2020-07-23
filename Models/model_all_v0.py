import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('precise.csv.csv')
features = tpot_data.drop('Flight_Status', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['Flight_Status'], random_state=None)

# Average CV score on the training set was: 0.538890917697978
exported_pipeline = make_pipeline(
    StackingEstimator(estimator=ExtraTreesClassifier(bootstrap=True, criterion="entropy", max_features=0.7500000000000001, min_samples_leaf=4, min_samples_split=5, n_estimators=100)),
    StackingEstimator(estimator=MultinomialNB(alpha=0.1, fit_prior=True)),
    GaussianNB()
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)