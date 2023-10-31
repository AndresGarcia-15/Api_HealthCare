from pydantic import BaseModel
class Appointment(BaseModel):
    date: str
    time: str
    doctor: str
    prescription: str

class Person(BaseModel):
    typeperson: str
    occupation: str

class Medicalhistorial(BaseModel):
    fullname: str
    age: int
    daybirthday: str
    genre: str
    placebirth: str
    emergency_person: str
    diseases: str
    allergies: str


