from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, Request, status

from fastapi.responses import HTMLResponse
from controllers.conectionpostgres import select_appointments, insert_appointments, delete_appointments, update_appointments, select_person, insert_person, delete_person, update_person, select_medicalhistorial, insert_medicalhistorial, delete_medicalhistorial, update_medicalhistorial
from controllers.models import Appointment, Person, Medicalhistorial

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
'''
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
'''


'''
@app.get("/person")
async def root():
    return st_object.show()
@app.post("/person")
async def agregar_person(id: int, typePerson:str, occupation:str):
    createPerson = Person(id=id, typePerson=typePerson, occupation=occupation)
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
    

@app.get("/medicalhistorial")
async def root():
    return st_object3.show()

@app.post("/medicalhistorial")
async def agregar_medicalhistorial(fullname :str, id: int, age:int,dayBirthday: str, genre:str, placeBirth:str, emergencyPerson:str, diseases:str, allergies:str):
    createPerson = MedicalHistorial(fullname = fullname, id = id, age=age,dayBirthday=dayBirthday, genre=genre, placeBirth=placeBirth, emergencyPerson=emergencyPerson, diseases=diseases, allergies=allergies)
    print(createPerson)
    return st_object3.create_medicalhistorial(createPerson)

# Ruta para eliminar una persona por su ID
@app.delete('/medicalhistorial/{medicalhistorial_id}')
def delete_medicalhistorial(medicalhistorial_id: int):
    success = st_object3.delete_medicalhistorial(medicalhistorial_id)
    if success:
        return {"message": f"Historial medico {medicalhistorial_id} eliminada exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=f"No se encontró historial medico con id{medicalhistorial_id}")
    

@app.put('/medicalhistorial/{medicalhistorial_id}')
def update_medicalhistorial(medicalhistorial_id: int, updated_data: dict):
    success = st_object3.update_medicalhistorial(medicalhistorial_id, updated_data)
    if success:
        return {"message": f"Historial con {medicalhistorial_id} actualizada exitosamente"}
    else:
        raise HTTPException(status_code=404, detail=f"No se encontró un historial con{medicalhistorial_id}")
    
'''




@app.get("/appointment/{id_cita}")
async def get_appointment(id_cita: int):
    return select_appointments(id_cita)

@app.post("/appointment/")
async def agregar_appoitments( appointment: Appointment):
        insert_appointments(appointment.date, appointment.time, appointment.doctor, appointment.prescription)
        return {"message": "Appointment created successfully"}


@app.delete("/appointment/{id_cita}")
async def delete_appointment(id_cita: int):
    delete_appointments(id_cita)
    return {"message": "Appointment deleted successfully"}

@app.put("/appointment/{id_cita}")
async def update_appointment(id_cita: int, appointment: Appointment):
    update_appointments(appointment.date, appointment.time, appointment.doctor, appointment.prescription, id_cita)
    return {"message": "Appointment updated successfully"}


@app.get("/person/{id}")
async def get_person(id_person: int):
    return select_person(id_person)

@app.post("/person/")
async def post_person( person: Person):
        insert_person(person.typeperson, person.occupation)
        return {"message": "Person created successfully"}


@app.delete("/person/{id}")
async def dele_person(id_person: int):
    delete_person(id_person)
    return {"message": "Person deleted successfully"}

@app.put("/person/{id}")
async def upda_person(id_person: int , person: Person):
    update_person(person.typeperson, person.occupation,id_person)
    return {"message": "Person updated successfully"}


# Endpoint para obtener un registro de Medicalhistorial por su ID
@app.get("/medicalhistorial/{id}")
def get_medical(id: int):
    medicalhistorial = select_medicalhistorial(id)
    if medicalhistorial is None:
        raise HTTPException(status_code=404, detail="Medicalhistorial not found")
    return medicalhistorial

# Endpoint para crear un nuevo registro en Medicalhistorial
@app.post("/medicalhistorial/")
async def create_medical(medicalhistorial: Medicalhistorial):
    insert_medicalhistorial(
        medicalhistorial.fullname,
        medicalhistorial.age,
        medicalhistorial.daybirthday,
        medicalhistorial.genre,
        medicalhistorial.placebirth,
        medicalhistorial.emergency_person,
        medicalhistorial.diseases,
        medicalhistorial.allergies
    )
    return {"message": "Medicalhistorial created successfully"}

# Endpoint para eliminar un registro de Medicalhistorial por su ID
@app.delete("/medicalhistorial/{id}")
async def delete_medical(id: int):
    delete_medicalhistorial(id)
    return {"message": "Medicalhistorial deleted successfully"}

# Endpoint para actualizar un registro de Medicalhistorial por su ID
@app.put("/medicalhistorial/{id}")
async def update_medical(id_medicalhistorial: int, medicalhistorial: Medicalhistorial):
    update_medicalhistorial(
        medicalhistorial.fullname,
        medicalhistorial.age,
        medicalhistorial.daybirthday,
        medicalhistorial.genre,
        medicalhistorial.placebirth,
        medicalhistorial.emergency_person,
        medicalhistorial.diseases,
        medicalhistorial.allergies, id_medicalhistorial
    )
    return {"message": "Medicalhistorial updated successfully"}