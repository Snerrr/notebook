import datetime
from interface.itask import Itask


class Task(Itask):
  def __init__(self, date:datetime, text: str):
    self.date = date
    self.text = text
  def get_text(self) -> str:
    return self.text
  def get_date(self) -> datetime:
    return self.date