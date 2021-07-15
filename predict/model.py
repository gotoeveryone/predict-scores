import os
import pickle

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from predict.db import DBClient


class Model:
    __client = None

    def __init__(self):
        self.__client = DBClient()

    def generate(self):
        df = self.__client.fetch_scores()

        x_train, x_test, y_train, y_test = train_test_split(
            df.drop('winner', axis=1), df['winner'])

        dtc = DecisionTreeClassifier(random_state=123)
        dtc.fit(x_train, y_train)

        y_pred = dtc.predict(x_test)
        print(f'score: {accuracy_score(y_pred, y_test)}')

        model_dir = os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))) + '/models/'
        filename = 'finalized_model.sav'
        pickle.dump(dtc, open(model_dir + filename, 'wb'))
