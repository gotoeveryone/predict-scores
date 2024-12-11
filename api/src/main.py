import pickle
import re
import sys
from datetime import datetime

import pandas as pd

from storage import StorageManager

DATE_FORMAT = re.compile("\\d{1,4}-\\d{1,2}-\\d{1,2}")

if __name__ == "__main__":
    _, date, pid1, pid2 = sys.argv

    if (
        # date is invalid
        date is None
        or not DATE_FORMAT.match(date)
        # pid1 is invalid
        or pid1 is None
        or not pid1.isnumeric()
        # pid2 is invalid
        or pid2 is None
        or not pid2.isnumeric()
        # same value of pid1 and pid2
        or pid1 == pid2
    ):
        print({"error": "parameter is invalid."})

    player1 = int(pid1)
    player2 = int(pid2)

    f = StorageManager().get("predict_scores/finalized_model.sav")
    loaded_model = pickle.loads(f)

    df = pd.DataFrame()
    df["game_date"] = [datetime.strptime(date, "%Y-%m-%d").timestamp()]
    df["player1"] = [player1]
    df["player2"] = [player2]

    predicted = loaded_model.predict(df)
    winner = int(predicted[0])

    print({"winner": player1 if winner == 1 else player2})
