import pickle
from io import BytesIO

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
)
from sklearn.model_selection import cross_val_score, train_test_split

from storage import StorageManager

if __name__ == "__main__":
    manager = StorageManager()

    f = manager.get("predict_scores/input.csv")
    df = pd.read_csv(BytesIO(f), names=["game_date", "player1", "player2", "winner"])

    x_train, x_test, y_train, y_test = train_test_split(
        df.drop("winner", axis=1),
        df["winner"],
        random_state=123,
        stratify=df["winner"],
    )

    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=16,
        random_state=123,
        n_jobs=-1,
    )
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    print(f"score: {accuracy_score(y_pred, y_test)}")
    print("class distribution:")
    print(df["winner"].value_counts(normalize=True))
    print(f"baseline: {df['winner'].value_counts(normalize=True).max()}")
    print("confusion matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("classification report:")
    print(classification_report(y_test, y_pred))
    y_proba = model.predict_proba(x_test)[:, 1]
    print(f"roc auc: {roc_auc_score(y_test, y_proba)}")
    cv_scores = cross_val_score(model, df.drop("winner", axis=1), df["winner"], cv=5)
    print(f"cv scores: {cv_scores}")
    print(f"cv mean: {cv_scores.mean()}")

    manager.put(
        "predict_scores/finalized_model.sav",
        pickle.dumps(model),
        "application/octet-stream",
    )
