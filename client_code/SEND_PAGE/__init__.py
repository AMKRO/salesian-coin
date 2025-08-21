from ._anvil_designer import SEND_PAGETemplate
from anvil import *

class SEND_PAGE(SEND_PAGETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
