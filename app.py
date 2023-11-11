from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, Request, status

from fastapi.responses import HTMLResponse

from controllers.conectionpostgres import select_appointments, insert_appointments, delete_appointments, update_appointments, select_person, insert_person, delete_person, update_person, select_medicalhistorial, insert_medicalhistorial, delete_medicalhistorial, update_medicalhistorial,get_pdf_json
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


@app.get("/", response_class=HTMLResponse, tags=["Home"] )
def message():
    with open("index.html", "r") as file:
        content = file.read()
    return content

@app.get("/appointment/{id_cita}",tags=["Citas Médicas"])
async def get_appointment(id_cita: int):
    return select_appointments(id_cita)

@app.post("/appointment/",tags=["Citas Médicas"])
async def agregar_appoitments( appointment: Appointment):
        insert_appointments(appointment.date, appointment.time, appointment.doctor, appointment.prescription)
        return {"message": "Appointment created successfully"}


@app.delete("/appointment/{id_cita}",tags=["Citas Médicas"])
async def delete_appointment(id_cita: int):
    delete_appointments(id_cita)
    return {"message": "Appointment deleted successfully"}

@app.put("/appointment/{id_cita}",tags=["Citas Médicas"])
async def update_appointment(id_cita: int, appointment: Appointment):
    update_appointments(appointment.date, appointment.time, appointment.doctor, appointment.prescription, id_cita)
    return {"message": "Appointment updated successfully"}


@app.get("/person/{id}",tags=["Personas"])
async def get_person(id_person: int):
    return select_person(id_person)

@app.post("/person/",tags=["Personas"])
async def post_person( person: Person):
        insert_person(person.typeperson, person.occupation)
        return {"message": "Person created successfully"}


@app.delete("/person/{id}",tags=["Personas"])
async def dele_person(id_person: int):
    delete_person(id_person)
    return {"message": "Person deleted successfully"}

@app.put("/person/{id}",tags=["Personas"])
async def upda_person(id_person: int , person: Person):
    update_person(person.typeperson, person.occupation,id_person)
    return {"message": "Person updated successfully"}


# Endpoint para obtener un registro de Medicalhistorial por su ID
@app.get("/medicalhistorial/{id}",tags=["Historiales Médicos"])
def get_medical(id: int):
    medicalhistorial = select_medicalhistorial(id)
    if medicalhistorial is None:
        raise HTTPException(status_code=404, detail="Medicalhistorial not found")
    return medicalhistorial

# Endpoint para crear un nuevo registro en Medicalhistorial
@app.post("/medicalhistorial/",tags=["Historiales Médicos"])
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
@app.delete("/medicalhistorial/{id}",tags=["Historiales Médicos"])
async def delete_medical(id: int):
    delete_medicalhistorial(id)
    return {"message": "Medicalhistorial deleted successfully"}

# Endpoint para actualizar un registro de Medicalhistorial por su ID
@app.put("/medicalhistorial/{id}",tags=["Historiales Médicos"])
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


@app.get("/pdf/{llave_images}", tags=["diagnosticimaging"])
def get_pdf(llave_images: int):
    
    return get_pdf_json(llave_images) 
