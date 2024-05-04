from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn



app = FastAPI() #stiamo chiamando una istanza di della classe FastAPI


#quella tra parentesi è il PATH -> (PATH), @app invece è in questo caso il path operation decorator
@app.get('/') #@decorator IMPORTANTE 
def index(): #questa è la path operation function
    return {'data' : 'blog list'}

@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None): #Optional ci permette di non definire una variabile e renderla opzionale
    #only get 10 published blogs
    if published is True:
        return {'data' : f'{limit} published blogs from the database'}
    else:
        return {'data' : f'{limit} blogs from the database'}



@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unpublished blog'}

@app.get('/about')
def about():#path operation function del pth /about
    return {'data' : {'name' : 'about page'}}



@app.get('/blog/{id}') #dynamic routing
def show(id: int): #scrivendo id_ int stiamo dicendo che il parametro id deve essere un intero, se cosi non fosse avremmo un errore
    #fetch blog with id = id
    return {'data' : id}
 
 #RICORDA FASTAPI LEGGE IL CODICE RIGA PER RIGA



@app.get('/blog/{id}/comments')
def comments(id: int, limit = 10):
    #fetch comments of blog with id = id
    return limit
    return {'data' : {'1','2'}}



class Blog(BaseModel): #model fatto con pydantic
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data' : f'blog is created with title as: {blog.title}'}

#come fare debug?


#ma cosa sta succedendo all'interno di fastAPI





#per cambiare porta si fa alla fine del file main.py
#if __name__ == "__main__":
#    uvicorn.run(app, host = "127.0.0.1", port=9000)
