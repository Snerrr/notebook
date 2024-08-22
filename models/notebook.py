from interface.inotebook import Inotebooke
from interface.itask import Itask

class Notebook(Inotebooke):
  def __init__(self, tasks : list[Itask]):
    self.tasks = tasks
  def append_task(self, task: Itask):
    pass
  def get_tasks(self) -> list:
    pass

  