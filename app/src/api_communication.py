import requests
import sys
sys.path.append('..')
import config

from src.utils import Game


class APICommunication():

    def __init__(self):
        self.base_url = config.API_BASE_URL
        self.headers = {
            "X-RapidAPI-Key": config.API_CREDENTIAL,
            "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
        }


    def _sign_url(self, url):
        return url + f'?key={config.API_KEY}'


    def _parse_response(self, response):
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


    def get_list_of_games(self):
        games_api_endpoint = self._sign_url(self.base_url + '/games')

        response = requests.request("GET", games_api_endpoint, headers=self.headers)
        parsed_data = self._parse_response(response)
        return parsed_data