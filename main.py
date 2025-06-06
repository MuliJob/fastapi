"""Main file"""
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    """Index route function"""
    return {'data': 'blog list'}


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
