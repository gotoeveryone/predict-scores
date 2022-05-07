import os
from predict.model import Model
from predict.storage import StorageManager

if __name__ == '__main__':
    filepath = Model().generate()

    if not os.environ.get('DEBUG', False):
        StorageManager().upload('predict_scores.sav', filepath)
