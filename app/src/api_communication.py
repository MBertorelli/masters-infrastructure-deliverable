import requests
import sys
sys.path.append('..')
import config


class APICommunication():

    def __init__():
        self.base_url = config.API_BASE_URL
        self.headers = {
            "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
            "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
        }


    def get_list_of_games():
        games_api_endpoint = self.base_url + '/games'

        response = requests.request("GET", games_api_endpoint, headers=self.headers)
        print(response.text)
