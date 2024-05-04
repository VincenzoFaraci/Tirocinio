from fastapi import APIRouter,Depends,status,HTTPException,Response
from .. import schemas,database,models
from typing import List
from sqlalchemy.orm import Session
from ..hashing import Hash
from .repository import user

router = APIRouter(
    prefix= "/user",
    tags=['user']
)
get_db = database.get_db

@router.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request,db)
    

@router.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return user.get(id,db)