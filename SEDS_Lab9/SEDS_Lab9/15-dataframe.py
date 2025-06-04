from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import json
app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/houseprices")
async def home(request: Request):
    df = pd.read_csv("data/house_pricing.csv", nrows=25)
    js = df.to_json(orient="records")
    data=json.loads(js)
    return templates.TemplateResponse("/houseprices.html",
                                    {"request":request,
                                    "house_prices":data})