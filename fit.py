import os
import pickle
import pandas as pd
from sklearn.neural_network import MLPClassifier

if __name__ == '__main__':
  df = pd.read_csv(os.environ.get('FILE_PATH'))

  df_x = df.drop('winner', axis=1)
  df_y = df['winner']

  clf = MLPClassifier()
  clf.fit(df_x, df_y)

  filename = 'finalized_model.sav'
  pickle.dump(clf, open(filename, 'wb'))
