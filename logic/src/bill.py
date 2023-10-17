class Bill(object):
  def __init__(self, id: int=0):
    self.id =id
  
  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, value) -> None:
      self._id = value

  #def generatebill(self):

  #def processpayment(self):