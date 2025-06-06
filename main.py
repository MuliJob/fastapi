"""Main file"""
from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    """Index route function"""
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    """Unpublished blogs"""
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    """Blog detail page"""
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    """Comment function"""
    return {'data': {'3', '5'}}
