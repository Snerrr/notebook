import abc
from interface.itask import Itask

class Inotebooke(abc.ABC):
  @abc.abstractmethod 
  def append_task(self, task : Itask):
    pass

  @abc.abstractmethod 
  def get_tasks(self) -> list:
    pass


