import abc
import datetime


class Itask(abc.ABC):
  @abc.abstractmethod
  def get_text(self) -> str:
    pass

  @abc.abstractmethod
  def get_date(self) -> datetime:
    pass