from models.notebook import Notebook
from view.console_view import Console_view
from models.task import Task
from view import text

class Presenter():
  def __init__(self, model: Notebook, view : Console_view):
    self.model = model
    self.view = view
  def create_task(self):
    date, text = self.view.append_task()
    new_task = Task(date, text)
    self.model.append_task(new_task)
  def view_tasks(self):
    tasks = self.model.get_tasks()
    self.view.view_tasks(tasks)
  def run(self):
    while True:
      print(text.menu)
      choise = int(input("Введите пункт меню: "))
      if choise == 1:
        self.view_tasks()
      if choise == 2:
        self.create_task()
      if choise == 3:
        print(text.menu_close)
        break