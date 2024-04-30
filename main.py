from fastapi import FastAPI

app = FastAPI() #stiamo chiamando una istanza di della classe FastAPI

@app.get('/') #@decorator
def index(): #funzione
    return {'data' : {'name' : 'Mbare Turi'}}

@app.get('/about')
def about():
    return {'data' : {'name' : 'about page'}}

#ma cosa sta succedendo all'interno di fastAPI