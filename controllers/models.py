from pydantic import BaseModel
from pydantic import BaseModel, constr, conint, validator
from datetime import datetime, time
from typing_extensions import Optional

class Appointment(BaseModel):
    date: constr(strip_whitespace=True, min_length=10, max_length=10)
    time: constr(strip_whitespace=True, min_length=5, max_length=5)
    doctor: constr(max_length=100)
    prescription: constr(max_length=200)

    @validator('date')
    def validate_date_format(cls, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Formato de fecha no válido. Debe ser 'YYYY-MM-DD'")
        return value

    @validator('time')
    def validate_time_format(cls, value):
        try:
            time.fromisoformat(value)
        except ValueError:
            raise ValueError("Formato de hora no válido. Debe ser 'HH:MM'")
        return value

class Person(BaseModel):
    typeperson: constr(max_length=50)
    occupation: constr(max_length=50)

class Medicalhistorial(BaseModel):
    fullname: constr(max_length=75)
    age: conint(ge=0, le=150)
    daybirthday: constr(min_length=10, max_length=10)
    genre: constr(max_length=10)
    placebirth: constr(max_length=50)
    emergency_person: constr(max_length=20)
    diseases: constr(max_length=50)
    allergies: constr(max_length=50)

    @validator('daybirthday')
    def validate_daybirthday_format(cls, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Formato de día de cumpleaños no válido. Debe ser 'YYYY-MM-DD'")
        return value
    

class Diagnosticimaging(BaseModel):
    
    diagnostico_principal: constr(max_length=75)
    diagnosticos_secundarios: constr(max_length=75)
    plan_de_tratamiento: constr(max_length=75)
    medicamentos_recetados: constr(max_length=75)
    procedimientos_realizados: constr(max_length=75)
    diagnosticimages: bytes

class User(BaseModel):
    idClient: constr(max_length=150)
    email: constr(max_length=150)
    username: constr(max_length=150)
    #typeperson: constr(max_length=50)

class Laboratory(BaseModel):
    test1: constr(max_length=75)
    test2: constr(max_length=75)
    test3: constr(max_length=75)
    test4: constr(max_length=75)
    test5: constr(max_length=75)