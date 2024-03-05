from fastapi import FastAPI
# from transformers import pipeline

app = FastAPI()
# pipe = pipeline(model="nlptown/bert-base-multilingual-uncased-sentiment")

@app.post("/sentiment")
async def sentiment_analysis(text: str):
    return 'test'
    # return pipe(text)
