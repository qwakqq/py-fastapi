from typing import Union
import requests as r
from fastapi import FastAPI
from pydantic import BaseModel

class CreateBookScheme(BaseModel):
    author: str
    namebook: Union[str, list[str]]



app = FastAPI()


date = {
        'Достоевский': 'идиот',
    }



@app.get('/my-path')
def my_path():

    return {'ответ my path': 'май патх'}

@app.get('/get_data')
def get_data():
    return date

@app.get('/add')
def add(
    a: int, 
    b: int
) -> dict:
    return{'result': a + b}

@app.post('create_book')
def create_book(
    book_date: CreateBookScheme
):
    book_date.author
    date[book_date.author] = book_date.namebook
    return date