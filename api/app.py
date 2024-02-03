import os
from dotenv import load_dotenv
from fastapi import FastAPI, responses
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from embedchain import Pipeline
import uvicorn

load_dotenv(".env")

app = FastAPI(title="Embedchain FastAPI App")
embedchain_app = Pipeline()
origins = [
   
    "*",  # Allows all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Specify allowed methods
    allow_headers=["X-Requested-With", "Content-Type", "Authorization"],  # Specify allowed headers
)
embedchain_app.add("https://housing.asu.edu")
embedchain_app.add("https://live-housing-d9.pantheonsite.io/sitemap.xml", data_type='sitemap')
embedchain_app.add("https://housing.asu.edu/housing-resources/housing-rates-and-costs")
embedchain_app.add('https://tuition.asu.edu/sitemap.xml', data_type='sitemap')
embedchain_app.add('https://fullcircle.asu.edu/faculty-sitemap.xml', data_type='sitemap')
embedchain_app.add('https://fullcircle.asu.edu/external_news-sitemap.xml', data_type='sitemap')
embedchain_app.add('https://asu.campuslabs.com/engage/api/discovery/search/organizations?orderBy%5B0%5D=UpperName%20asc&top=100&filter=&query=&skip=70', data_type='sitemap')



class SourceModel(BaseModel):
    source: str


class QuestionModel(BaseModel):
    question: str


@app.post("/add")
async def add_source(source_model: SourceModel):
    """
    Adds a new source to the EmbedChain app.
    Expects a JSON with a "source" key.
    """
    source = source_model.source
    embedchain_app.add(source)
    return {"message": f"Source '{source}' added successfully."}


@app.post("/query")
async def handle_query(question_model: QuestionModel):
    """
    Handles a query to the EmbedChain app.
    Expects a JSON with a "question" key.
    """
    question = question_model.question
    answer = embedchain_app.query(question)
    return {"answer": answer}


@app.post("/chat")
async def handle_chat(question_model: QuestionModel):
    """
    Handles a chat request to the EmbedChain app.
    Expects a JSON with a "question" key.
    """
    question = question_model.question
    response = embedchain_app.query(question)
    return {"response": response}


@app.get("/")
async def root():
    return responses.RedirectResponse(url="/docs")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
