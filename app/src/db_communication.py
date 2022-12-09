import time
import mysql.connector
import config
from typing import List
from src.utils import Game


class DBCommunication():

    def __init__(self):
        connection_successful = False

        while not connection_successful:
            try: 
                self.mydb = mysql.connector.connect(
                    host=config.dbhost,
                    user=config.dbuser,
                    password=config.dbpassword,
                    database=config.dbname,
                )

                self.cursor = self.mydb.cursor()
                print("Connection to DB successful")
                self.create_games_table()
                print("Game table created")
                connection_successful = True
            except:
                print("Connection to MySQL failed")
                time.sleep(3)


    def create_games_table(self) -> bool:
        sql = "CREATE TABLE IF NOT EXISTS games (game_id INT PRIMARY KEY, name VARCHAR(255), release_date VARCHAR(255), rating DOUBLE, genres VARCHAR(255))"
        self.cursor.execute(sql)

        return True


    def insert_games(self, list_of_games) -> bool:
        sql = "INSERT IGNORE INTO games (game_id, name, release_date, rating, genres) VALUES (%s, %s, %s, %s, %s)"

        for game in list_of_games:
            val = game.get_game_values()
            self.cursor.execute(sql, val)

        self.mydb.commit()

        return True


    def dump_games_table(self) -> List[Game]:
        sql = "SELECT * FROM games"

        self.cursor.execute(sql)

        games_list = []

        sql_result = self.cursor.fetchall()
        for res in sql_result:
            games_list.append(Game(res[0], res[1], res[2], res[3], res[4].replace('"', '').strip('][').split(', ')))

        return games_list
