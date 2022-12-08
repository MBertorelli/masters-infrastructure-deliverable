from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.api_communication import APICommunication


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

api_communication = APICommunication()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/get_random")
async def get_random():
    list_of_games = api_communication.get_list_of_games() 
    return list_of_games

@app.get("/get_genre/")
async def get_random(genre: str):
    return genre
