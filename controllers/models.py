from pydantic import BaseModel

class PersonIn(BaseModel):
    """
    name(str): The name of the person.
    email(str): The email of the person.
    telephone(str): The telephone number of the person.
    id(int): The identification number of the person.
    """
    id: int
    typePerson:str
    ocupation:str
class AppointmentsIn(BaseModel):
    """
    date(int): The date of the appointment.
    time(int): The time of the appointment.
    doctor(str): The doctor of the appointment.
    prescription(str): The prescription of the appointment.
    """
    date: str
    time: str
    doctor: PersonIn
    prescription: str
    id_cita: int


