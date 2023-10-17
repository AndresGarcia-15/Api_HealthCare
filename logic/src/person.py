from uuid import uuid4 as uid
class Person(object):
  def __init__(self, id: int=0, typePerson: str ="typePerson", ocupation: str="ocupation"):
    self.id = id
    self.typePerson =typePerson
    self.ocupation = ocupation

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, value) -> None:
      self._id = value 
    
  @property
  def typePerson(self) -> str:
    return self._typePerson

  @typePerson.setter
  def typePerson(self, value) -> None:
      self._typePerson = value 

  @property
  def ocupation(self) -> str:
    return self._ocupation

  @ocupation.setter
  def ocupation(self, value) -> None:
      self._ocupation = value 
      
  def __str__(self):
    return dict(id=self.id, typePerson=self.typePerson, ocupation=self.ocupation).__str__()
    