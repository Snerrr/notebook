import datetime
class Create_task():
  def __init__(self):
    pass
  def create_text(self):
    text = str(input("Введите задачу"))
    return text
  def create_date(self):
    date = datetime.datetime.strptime(input("Введите дату"), "%d.%m.%Y")
    return date