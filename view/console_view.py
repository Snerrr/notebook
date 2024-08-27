import datetime
from interface.itask import Itask
class Console_view():
  def __init__(self):
    pass
  def view_tasks(self, tasks : list[Itask]):
    if len(tasks) == 0: print("Нет задач")
    else :
      for element in tasks:
        print(element.get_date, element.get_text)
  def append_task(self):
    date = datetime.datetime.strptime(input("Введите дату в формате dd.mm.yyyy"),"%d.%m.%Y")
    text = str(input("Введите задачу"))
    return date, text
  