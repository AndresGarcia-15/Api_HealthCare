

class Appoitments(object):
  def __init__(self, date: str= "date", time: str ="time", doctor: str="doctor", prescription: str="prescription", id_cita: int=0):
    self.date = date
    self.time = time
    self.doctor = doctor
    self.prescription = prescription
    self.id_cita = id_cita 

  @property
  def date(self) -> str:
    return self._date

  @date.setter
  def date(self, value) -> None:
      self._date = value 
    
  @property
  def time(self) -> str:
    return self._time

  @time.setter
  def time(self, value) -> None:
      self._time = value 

  @property
  def doctor(self) -> str:
    return self._doctor

  @doctor.setter
  def doctor(self, value) -> None:
      self._doctor = value 
    
  @property
  def prescription(self) -> str:
    return self._prescription

  @prescription.setter
  def prescription(self, value) -> None:
      self._prescription = value

  @property
  def id_cita(self) -> int:
    return self._id_cita
  
  @id_cita.setter
  def id_cita(self, value) -> None:
      self._id_cita = value

  def __str__(self):
    return dict(date=self.date, time=self.time, doctor=self.doctor, prescription=self.prescription, id_cita=self.id_cita).__str__()