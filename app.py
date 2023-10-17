from fastapi import FastAPI
import json
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, Request, status
from uuid import uuid4 as uid
from controllers.person_controller import Person_controller
from logic.src.person import Person
from controllers.appoitments_controller import Appoitments_controller
from logic.src.appoitments import Appoitments
from fastapi.responses import HTMLResponse

# Initializing the FastAPI app
st_object2 = Appoitments_controller()
st_object = Person_controller()
app = FastAPI()
app.title = "Healthcare Provider API"

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/", response_class=HTMLResponse)
def message():
    with open("index.html", "r") as file:
        content = file.read()
    return content

# A POST endpoint to create a new person object in the database

@app.get("/appoitments")
async def get_appointments():
    return st_object2.show()

@app.post("/appoitments")
async def agregar_appoitments( date: str, time:str, doctor:str, prescription:str, id_cita:int):
    createPerson = Appoitments(date=date, time=time, doctor=doctor, prescription=prescription, id_cita=id_cita)
    print(createPerson)
    return st_object2.create_appoitments(createPerson)

# Ruta para eliminar una persona por su ID
@app.delete('/appoitments/{appoitments_id}')
def delete_appoitments(appoitments_id: int):
    success = st_object2.delete_appoitments(appoitments_id)
    if success:
        return {"message": f"cita con ID {appoitments_id} eliminada exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=f"No se encontró una cita con ID {appoitments_id}")


@app.put('/appoitments/{appoitments_id}')
def update_appoitments(appoitments_id: int, updated_data: dict):
    success = st_object2.update_appoitments(appoitments_id, updated_data)
    if success:
        return {"message": f"cita con _id {appoitments_id} actualizada exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=f"No se encontró una cita con _id {appoitments_id}")

@app.get("/person")
async def root():
    return st_object.show()
@app.post("/person")
async def agregar_person(id: int, typePerson:str, ocupation:str):
    createPerson = Person(id=id, typePerson=typePerson, ocupation=ocupation)
    print(createPerson)
    return st_object.create_person(createPerson)

# Ruta para eliminar una persona por su ID
@app.delete('/person/{person_id}')
def delete_person(person_id: int):
    success = st_object.delete_person(person_id)
    if success:
        return {"message": f"Persona con ID {person_id} eliminada exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=f"No se encontró una persona con ID {person_id}")
    

@app.put('/persons/{person_id}')
def update_person(person_id: int, updated_data: dict):
    success = st_object.update_person(person_id, updated_data)
    if success:
        return {"message": f"Persona con _id {person_id} actualizada exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=f"No se encontró una persona con _id {person_id}")
