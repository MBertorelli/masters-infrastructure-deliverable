from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.api_communication import APICommunication
from src.db_communication import DBCommunication

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

api_communication = APICommunication()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    list_of_genres = await api_communication.get_list_of_genres()
    return templates.TemplateResponse("home.html", {
                                                    "request": request,
                                                    "genres": list_of_genres,
                                                    })


@app.get("/get_random")
async def get_random():
    list_of_games = api_communication.get_list_of_games()
    return list_of_games


@app.get("/get_genre/")
async def get_genre(genre: str):
    list_of_games_by_genre = api_communication.get_list_of_games_by_genre(genre)
    return list_of_games_by_genre


@app.get("/get_info/")
async def get_random(game_id: str):
    game = api_communication.search_game(game_id)
    return game


@app.get("/dump_db/")
async def get_random():
    dbc = DBCommunication()
    game = dbc.dump_games_table()
    return game
