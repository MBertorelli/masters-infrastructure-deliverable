import requests
import sys
sys.path.append('..')
import config
from typing import List

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


    def _parse_games_response(self, response) -> List[Game]:
        response = response.json()['results']
        
        list_of_games = []
        
        for game in response:
            name = game['name']
            release_date = game['released']
            rating = game['rating']
            game_genres = []
            for genre in game['genres']:
                game_genres.append(genre['name'])

            list_of_games.append(Game(name, release_date, rating, game_genres))

        return list_of_games


    def _parse_genres_response(self, response):
        response = response.json()['results']

        available_genres = [item['name'] for item in response]

        return available_genres


    def get_list_of_games(self) -> List[Game]:
        games_api_endpoint = self._sign_url(self.base_url + '/games')
        print(f"Querying to {games_api_endpoint}")

        response = requests.request("GET", games_api_endpoint, headers=self.headers)
        parsed_data = self._parse_games_response(response)

        return parsed_data

    
    async def get_list_of_genres(self):
        games_api_endpoint = self._sign_url(self.base_url + '/genres')
        print(f"Querying to {games_api_endpoint}")

        response = requests.request("GET", games_api_endpoint, headers=self.headers)
        parsed_data = self._parse_genres_response(response)

        return parsed_data
