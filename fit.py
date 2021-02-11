import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from db import DBClient

if __name__ == '__main__':
    client = DBClient()
    df = client.fetch_scores()

    df_x = df.drop('winner', axis=1)
    df_y = df['winner']

    dtc = DecisionTreeClassifier(random_state=42)
    dtc.fit(df_x, df_y)
    print(f'scope: {dtc.score(df_x, df_y)}')

    filename = 'finalized_model.sav'
    pickle.dump(dtc, open(filename, 'wb'))
