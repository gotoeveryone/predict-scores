from datetime import datetime
import os
import pandas as pd
import pymysql


class DBClient:
    def __init__(self):
        self.user = os.environ.get('DB_USER')

    def connect(self):
        host = os.environ.get('DB_HOST')
        port = os.environ.get('DB_PORT', 3306)
        name = os.environ.get('DB_NAME')
        username = os.environ.get('DB_USERNAME')
        password = os.environ.get('DB_PASSWORD')

        return pymysql.connect(
            host=host,
            port=int(port),
            db=name,
            user=username,
            passwd=password,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def fetch_scores(self) -> pd.DataFrame:
        conn = self.connect()
        sql = """
            select
                unix_timestamp(ts.started) as game_date
                , tsd1.player_id as player1
                , tsd2.player_id as player2
                , case when tsd1.division = %s then 1 else 2 end as winner
            from title_scores ts
            inner join (
                select
                    tsd.title_score_id
                    , tsd.division
                    , min(tsd.player_id) as player_id
                from title_score_details tsd
                where division in (%s, %s) group by tsd.title_score_id
            ) tsd1 on ts.id = tsd1.title_score_id
            inner join (
                select
                    tsd.title_score_id
                    , tsd.division, max(tsd.player_id) as player_id
                from title_score_details tsd
                where division in (%s, %s) group by tsd.title_score_id
            ) tsd2 on ts.id = tsd2.title_score_id
        """
        df = pd.read_sql(
            sql,
            conn,
            params=('勝', '勝', '敗', '勝', '敗',),
        )

        df['player1'] = df['player1'].astype('int')
        df['player2'] = df['player2'].astype('int')
        df['winner'] = df['winner'].astype('int')

        return df
