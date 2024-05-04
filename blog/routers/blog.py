from fastapi import APIRouter,Depends,status,HTTPException,Response
from .. import schemas,database,models,oauth2
from typing import List
from sqlalchemy.orm import Session
from .repository import blog

router = APIRouter(
    prefix = "/blog",
    tags = ['blogs']
)
get_db = database.get_db

@router.get('/', response_model=list[schemas.ShowBlog])
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED) #using Docs tags
def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id,db: Session = Depends(get_db), status_code = 200,current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id,db)


#update a blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)