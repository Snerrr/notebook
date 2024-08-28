from interface.inotebook import Inotebooke
from interface.itask import Itask

class Notebook(Inotebooke):
  def __init__(self, tasks : list[Itask] = []):
    self.tasks = tasks
  def append_task(self, task: Itask):
    self.tasks.append(task)
  def get_tasks(self) -> list:
    return self.tasks

  