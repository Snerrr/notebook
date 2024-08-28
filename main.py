from models.notebook import Notebook
from view.console_view import Console_view
from presenter.presenter import Presenter
if __name__ == "__main__":
  model = Notebook()
  view = Console_view()
  presenter = Presenter(model, view)
  presenter.run()