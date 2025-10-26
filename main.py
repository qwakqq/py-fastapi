import requests as r
from fastapi import FastAPI
from pydantic import BaseModel

class CreateBookScheme(BaseModel):
    author: str
    namebook: str | list[str]

app = FastAPI()

date = {
    'Достоевский': 'идиот',
}

items_database = {
    100: {
        'who in family': 'mom',
        'name': 'Tatiana',
        'age': 46,
        'phone number': '+7(951)-627-44-13'
    },
    101: {
        'who in family': 'dad',
        'name': 'Sergey',
        'age': 52,
        'phone number': '+7(902)-160-51-24'
    },
    102: {
        'who in family': 'daughter, sister',
        'name': 'Darya',
        'age': 20,
        'phone number': '+7(950)-384-55-26'
    },
    103: {
        'who in family': 'son, brother',
        'name': 'Arsenii',
        'age': 13,
        'phone number': '+7(902)-169-43-45' 
    }
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
    return {'result': a + b}

@app.post('/create_book') 
def create_book(book_date: CreateBookScheme):
    date[book_date.author] = book_date.namebook
    return date

@app.get('/family')
def family():
    return items_database

@app.get('/familyID/{member_id}')
def family_member(member_id: int):  
    if member_id in items_database:
        return {
            'member_id': member_id,
            **items_database[member_id]
        }
    else:
        return {"error": "Member not found"}