from io import BytesIO
import pickle

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from storage import StorageManager


if __name__ == "__main__":
    manager = StorageManager()

    f = manager.get("predict_scores/input.csv")
    df = pd.read_csv(BytesIO(f), names=["game_date", "player1", "player2", "winner"])

    x_train, x_test, y_train, y_test = train_test_split(
        df.drop("winner", axis=1), df["winner"]
    )

    dtc = DecisionTreeClassifier(random_state=123)
    dtc.fit(x_train, y_train)

    y_pred = dtc.predict(x_test)
    print(f"score: {accuracy_score(y_pred, y_test)}")

    manager.put("predict_scores/finalized_model.sav", pickle.dumps(dtc), "text/csv")
