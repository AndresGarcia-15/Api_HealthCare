from fastapi import FastAPI
from fastapi import HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, Request, status
from psycopg2 import DatabaseError
from fastapi.responses import HTMLResponse
from controllers.conectionpostgres import select_appointments, insert_appointments, delete_appointments, update_appointments, select_person, insert_person, delete_person, update_person, select_medicalhistorial, insert_medicalhistorial, delete_medicalhistorial, update_medicalhistorial,get_pdf_json,insert_diagnosticimaging,delete_diagnosticimaging_by_id,insert_person,allusers,id_user, select_diagnosticimaging, insert_laboratory, select_laboratory,update_person_role
from controllers.models import Appointment, Medicalhistorial, Diagnosticimaging,User,Laboratory,PersonUpdateRole
from controllers.utils import VerifyToken
from fastapi.security import HTTPBearer
app = FastAPI()
app.title = "Healthcare Provider API"
token_auth_scheme = HTTPBearer()
# Configuración de CORS
origins = ["http://localhost:5173"]  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Actualiza esto con los orígenes permitidos en producción
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
async def agregar_appoitments( appointment: Appointment,token: str = Depends(token_auth_scheme)):
        result = VerifyToken(token.credentials).verify()
        if not result.get("status"):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result.get("detail"))
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

# Endpoint para obtener un registro de Medicalhistorial por su ID
@app.get("/medicalhistorial/{id}",tags=["Historiales Médicos"])
def get_medical(id: int):
    medicalhistorial = select_medicalhistorial(id)
    if medicalhistorial is None:
        raise HTTPException(status_code=404, detail="Medicalhistorial not found")
    return medicalhistorial

# Endpoint para crear un nuevo registro en Medicalhistorial
@app.post("/medicalhistorial/",tags=["Historiales Médicos"])
async def create_medical(medicalhistorial: Medicalhistorial,token: str = Depends(token_auth_scheme)):
    result = VerifyToken(token.credentials).verify()
    if not result.get("status"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result.get("detail"))
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

@app.get("/diagnosticimaging/{id_llaves}",tags=["diagnosticimaging"])
def get_diagnosticimaging(id_llaves: int):
    return select_diagnosticimaging(id_llaves)
'''
@app.get("/pdf/{llave_images}", tags=["diagnosticimaging"])
def get_pdf(llave_images: int):
    
    return get_pdf_json(llave_images) 
'''

@app.post("/diagnosticimaging/", tags=["diagnosticimaging"])
async def create_pdf(diagnosticimaging: Diagnosticimaging,token: str = Depends(token_auth_scheme)):
    result = VerifyToken(token.credentials).verify()
    if not result.get("status"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result.get("detail"))
    insert_diagnosticimaging(
        diagnosticimaging.diagnostico_principal,
        diagnosticimaging.diagnosticos_secundarios,
        diagnosticimaging.plan_de_tratamiento,
        diagnosticimaging.medicamentos_recetados,
        diagnosticimaging.procedimientos_realizados
    )
    return {"message": "diagnosticimaging created successfully"}

@app.delete("/diagnosticimaging/{id}/", tags=["diagnosticimaging"])
async def delete_diagnosticimaging(id: int):
    delete_diagnosticimaging_by_id(id)
    return {"message": f"Diagnostic imaging record with ID {id} deleted successfully"}

@app.post("/api/register", tags=["Usuarios"])
async def register_user(user: User, token: str = Depends(token_auth_scheme)):
    # Verificar el token
    result = VerifyToken(token.credentials).verify()
    if not result.get("status"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result.get("detail"))

    # Verificar si el usuario ya existe
    existing_user = id_user(user.idClient)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya existe en la base de datos")

    # Si el usuario no existe, realizar la inserción
    insert_person(user.idClient, user.email, user.username)
    return {"message": "Usuario creado exitosamente"}

'''
@app.get("/api/users",tags=["Usuarios"])
async def get_users(token: str = Depends(token_auth_scheme)):
    user = allusers()
    result = VerifyToken(token.credentials).verify()
    if not result.get("status"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result.get("detail"))
    if user is None:
            raise HTTPException(status_code=404, detail="User not found")
    return user
'''

@app.get("/api/users/{id_auth}",tags=["Usuarios"])
async def get_users1(id_auth:str):
    # Verificar el token
    user = id_user(id_auth)
    '''
    #result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result.get("detail"))
    '''
    return user

@app.get("/laboratory/{testid}",tags=["Laboratorios"])
async def get_laboratory(testid: int):
    return select_laboratory(testid)

@app.post("/laboratory/",tags=["Laboratorios"])
async def agregar_laboratory(laboratory: Laboratory,token: str = Depends(token_auth_scheme)):
        result = VerifyToken(token.credentials).verify()
        if not result.get("status"):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result.get("detail"))
        insert_laboratory(laboratory.test1, laboratory.test2, laboratory.test3, laboratory.test4,laboratory.test5)
        return {"message": "Laboratory created successfully"}

@app.delete("/laboratory/{testid}",tags=["Laboratorios"])
async def delete_laboratory(testid: int):
    delete_laboratory(testid)
    return {"message": "Laboratory deleted successfully"}

@app.put("/update-role",tags=["Usuarios"])
async def update_role(person_update: PersonUpdateRole):
    try:
        update_person_role(person_update.id_auth, person_update.role)
        return {"message": "Role updated successfully"}
    except DatabaseError:
        raise HTTPException(status_code=500, detail="Database error")
