from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
        User(
            id=UUID("fe07c74b-33d7-4116-96e4-92bb045aae32"),
            first_name="Maia",
            last_name="Oliveira", 
            email="email@gmail.com",
            role=[Role.role_1]
        ),
        User(
            id=UUID("0ac21900-c861-4845-bd0f-f314854dba6b",),
            first_name="Maria",
            last_name="Maia", 
            email="email@gmail.com",
            role=[Role.role_2]
        ),
        User(
            id=UUID("ff63cc1f-0852-4df4-b387-6bdb54112b7c",),
            first_name="Ruth",
            last_name="Silva", 
            email="email@gmail.com",
            role=[Role.role_3]
        ),
]


@app.get("/")
async def root():
    return{"Olá womakers!"}


@app.get("/api/users")
async def get_users():
    return db


@app.get("/api/users/{id}")
async def get_users(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuária não encontrada!"}

@app.post("/api/users/")
async def add_user(user: User): #novo usuario do tipo User que respeita a modelagem
    """   
    Adiciona um usuário na Base 
    - **id**: UUID
    - **first_name**: string 
    - **last_name**: string
    - **email**: string
    - **role**: Role 
    """
    
    db.append(user)
    return {"id": user.id} #lembrando que o id é feito de forma ramdomica

@app.delete("/api/users/{id}")
async def remove_user(id: UUID): #remover usuario do tipo User que respeita a modelagem
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com id{id} não encontrado!"
    )
