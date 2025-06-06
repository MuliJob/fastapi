"""Main file"""
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    """Index route function"""
    return {'data': {'name': 'Munyoki'}}

@app.get('/about')
def about():
    """About page"""
    return {'data': 'About-page'}
