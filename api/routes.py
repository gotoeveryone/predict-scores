from datetime import datetime
import os
import pickle
import re

from flask import Blueprint, jsonify, request
import pandas as pd

api = Blueprint(
    'api',
    __name__,
)

DATE_FORMAT = re.compile('\\d{1,4}-\\d{1,2}-\\d{1,2}')


@api.route('/predict', methods=['GET'])
def get_predict():
    date = request.args.get('date')
    pid1 = request.args.get('pid1')
    pid2 = request.args.get('pid2')
    if (
        # date is invalid
        date is None or not DATE_FORMAT.match(date)
        # pid1 is invalid
        or pid1 is None or not pid1.isnumeric()
        # pid2 is invalid
        or pid2 is None or not pid2.isnumeric()
        # same value of pid1 and pid2
        or pid1 == pid2
    ):
        return jsonify({
            'error': 'parameter is invalid.'
        }), 400

    player1 = int(pid1)
    player2 = int(pid2)

    model_dir = os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))) + '/models/'
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(model_dir + filename, 'rb'))

    df = pd.DataFrame()
    df['game_date'] = [datetime.strptime(date, '%Y-%m-%d').timestamp()]
    df['player1'] = [player1]
    df['player2'] = [player2]

    predicted = loaded_model.predict(df)
    winner = int(predicted[0])

    return jsonify({'winner': player1 if winner == 1 else player2})
