from ._anvil_designer import SEND_PAGETemplate
from anvil import *

class SEND_PAGE(SEND_PAGETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('HOMEPAGE')

  def image_1_mouse_down(self, x, y, button, keys, **event_args):
    """This method is called when a mouse button is pressed on this component"""
    open_form('HOMEPAGE')
    