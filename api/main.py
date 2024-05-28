import json
import sys

from api.src.app import get_winner

dummy_event = {
    "account": "admin",
    "detail": {},
    "detail-type": "Scheduled Event",
    "id": "dummy",
    "region": "ap-northeast-1",
    "resources": [],
    "source": "aws.events",
    "time": "2019-06-24T01:23:45Z",
    "version": "1.0",
    "queryStringParameters": {"date": "2024-05-01", "player1": "1", "player2": "2"},
}

# ローカル実行用
if __name__ == "__main__":
    _, date, player1, player2 = sys.argv

    print(json.dumps(get_winner(date, player1, player2), ensure_ascii=False, indent=2))
