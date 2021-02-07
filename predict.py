import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    df = pd.DataFrame()
    df['player1'] = []
    df['player2'] = []

    predicted = loaded_model.predict(df)
    for i, r in enumerate(predicted):
        t = df.iloc[i, :]
        p1 = t['player1']
        p2 = t['player2']
        w = t['player1'] if predicted[i] == 1 else t['player2']
        print(f'{p1}-{p2}: {w} is win.')
