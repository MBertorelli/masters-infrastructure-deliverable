from dataclasses import dataclass
from typing import List
import datetime
import json


@dataclass
class Game:
    """Class storing info from a specific game retrieved from API."""
    game_id: int
    name: str
    release_date: datetime.date
    rating: float
    genres: List[str]

    def __init__(self, game_id: int, name: str, release_date: datetime.date, rating: float, genres: List[str]):
        self.game_id = game_id
        self.name = name
        self.release_date = release_date
        self.rating = rating
        self.genres = genres


    def get_game_values(self):
        return (self.game_id, self.name, self.release_date, self.rating, json.dumps(self.genres))
