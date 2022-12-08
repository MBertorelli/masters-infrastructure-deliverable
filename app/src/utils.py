from dataclasses import dataclass
from typing import List
import datetime


@dataclass
class Game:
    """Class storing info from a specific game retrieved from API."""
    name: str
    release_date: datetime.date
    rating: float
    genres: List[str]

    def __init__(self, name: str, release_date: datetime.date, rating: float, genres: List[str]):
        self.name = name
        self.release_date = release_date
        self.rating = rating
        self.genres = genres
