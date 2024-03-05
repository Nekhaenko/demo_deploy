from fastapi import FastAPI, Request
from transformers import pipeline
# from pydantic import BaseModel
from starlette.responses import RedirectResponse

app = FastAPI()
pipe = pipeline(model="nlptown/bert-base-multilingual-uncased-sentiment")

@app.get('/')
def home():
    # Home page redirects to docs
    return RedirectResponse(url='/docs')
    

@app.post("/sentiment")
async def read_root(request: Request):
    data = await request.json()

    if 'text' in data:
        user_input = data['text']
        # print(user_input)
        return pipe(user_input)
    else:
        response = {"Recieved Text": "No Text Found"}
    return response