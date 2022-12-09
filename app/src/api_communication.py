import requests
import sys
sys.path.append('..')
import config
from typing import List
from src.db_communication import DBCommunication
from src.utils import Game


class APICommunication():

    def __init__(self) -> None:
        self.base_url = config.API_BASE_URL
        self.headers = {
            "X-RapidAPI-Key": config.API_CREDENTIAL,
            "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
        }


    def _sign_url(self, url) -> str:
        return url + f'?key={config.API_KEY}'


    def _parse_game(self, game) -> Game:
        game_id = game['id']
        name = game['name']
        release_date = game['released']
        rating = game['rating']
        game_genres = []
        for genre in game['genres']:
            game_genres.append(genre['name'])

        return Game(game_id, name, release_date, rating, game_genres)


    def _parse_games_response(self, response) -> List[Game]:
        response = response.json()['results']
        
        list_of_games = []
        
        for game in response:
            list_of_games.append(self._parse_game(game))

        return list_of_games


    def _parse_genres_response(self, response) -> List[str]:
        response = response.json()['results']

        available_genres = []

        for item in response:
            genre_string = f"ID:{item['id']}\t{item['name']}"
            available_genres.append(genre_string)

        return available_genres


    def _parse_games_from_genre(self, response, genre) -> List[str]:
        response = response.json()['results']

        games_from_genre = []

        for item in response:
            if str(item['id']) == genre:
                for game in item['games']:
                    games_from_genre.append(f"ID:{game['id']} NAME:{game['name']}")

        return games_from_genre


    def get_list_of_games(self) -> List[Game]:
        games_api_endpoint = self._sign_url(self.base_url + '/games')
        print(f"Querying to {games_api_endpoint}")

        response = requests.request("GET", games_api_endpoint, headers=self.headers)
        parsed_data = self._parse_games_response(response)

        dbc = DBCommunication()
        dbc.insert_games(parsed_data)

        return parsed_data

    
    async def get_list_of_genres(self) -> List[str]:
        games_api_endpoint = self._sign_url(self.base_url + '/genres')
        print(f"Querying to {games_api_endpoint}")

        response = requests.request("GET", games_api_endpoint, headers=self.headers)
        parsed_data = self._parse_genres_response(response)

        return parsed_data


    def get_list_of_games_by_genre(self, genre) -> List[Game]:
        games_api_endpoint = self._sign_url(self.base_url + '/genres')
        print(f"Querying to {games_api_endpoint}")

        response = requests.request("GET", games_api_endpoint, headers=self.headers)
        parsed_data = self._parse_games_from_genre(response, genre)

        dbc = DBCommunication()
        dbc.insert_games(parsed_data)

        return parsed_data


    def search_game(self, game_id) -> Game:
        games_api_endpoint = self._sign_url(self.base_url + f'/games/{game_id}')
        print(f"Querying to {games_api_endpoint}")

        response = requests.request("GET", games_api_endpoint, headers=self.headers)
        response = response.json()
        game = self._parse_game(response)

        dbc = DBCommunication()
        dbc.insert_games([game])

        return game
