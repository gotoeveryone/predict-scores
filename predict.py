from datetime import datetime, timezone
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    df = pd.DataFrame()
    df['game_date'] = [
        datetime(2019, 1, i + 1, tzinfo=timezone.utc).timestamp()
        for i in range(9)
    ]
    df['player1'] = [752, 8, 1055, 752, 1055, 1, 337, 1, 1]
    df['player2'] = [1055, 1, 752, 1, 337, 1055, 1, 337, 8]

    predicted = loaded_model.predict(df)
    print(predicted)
    for i, r in enumerate(predicted):
        t = df.iloc[i, :]
        d = datetime.fromtimestamp(t['game_date']).strftime('%Y-%m-%d')
        p1 = t['player1']
        p2 = t['player2']
        w = t['player1'] if predicted[i] == 1 else t['player2']
        print(f'{d} {p1}-{p2}: {w} is win.')
