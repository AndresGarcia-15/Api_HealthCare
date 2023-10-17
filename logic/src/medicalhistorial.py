class MedicalHistoial(object):
  def __init__(self, fullname: str="fullname", id: int=0, age: int=0, dayBirthday: int=0, genre: str="genre", placeBirth: str="placeBirth", emergencyPerson: str="emergencyPerson", diseases: str="diseases", allergies: str="alergies"):
    self.fullname = fullname
    self.id = id
    self.age =age
    self.dayBirthday = dayBirthday
    self.genre = genre
    self.placeBirth = placeBirth
    self.emergencyPerson = emergencyPerson
    self.diseases = diseases
    self.allergies = allergies

  @property
  def fullname(self) -> str:
    return self._fullname

  @fullname.setter
  def fullname(self, value) -> None:
      self._fullname = value 
    
  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, value) -> None:
      self._id = value 
    
  @property
  def age(self) -> int:
    return self._age

  @age.setter
  def age(self, value) -> None:
      self._age= value 
    
  @property
  def dayBirthday(self) -> int:
    return self._dayBirthday

  @dayBirthday.setter
  def dayBirthday(self, value) -> None:
      self._dayBirthday= value 
    
  @property
  def genre(self) -> int:
    return self._genre

  @genre.setter
  def genre(self, value) -> None:
      self._genre = value 
    
  @property
  def placeBirth(self) -> int:
    return self._placeBirth

  @placeBirth.setter
  def placeBirth(self, value) -> None:
      self._placeBirth = value 
    
  @property
  def emergencyPerson(self) -> int:
    return self._emergencyPerson

  @emergencyPerson.setter
  def emergencyPerson(self, value) -> None:
      self._emergencyPerson = value 
    
  @property
  def diseases(self) -> int:
    return self._diseases

  @diseases.setter
  def diseases(self, value) -> None:
      self._diseases = value
    
  @property
  def allergies(self) -> int:
    return self._allergies

  @allergies.setter
  def allergies(self, value) -> None:
      self._allergies = value

  def updatedata(self):
    return f"Updated data for patient {self.fullname} (ID: {self.id})"