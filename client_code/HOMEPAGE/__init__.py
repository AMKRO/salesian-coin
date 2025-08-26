from ._anvil_designer import HOMEPAGETemplate
from anvil import *

class HOMEPAGE(HOMEPAGETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('SEND_PAGE')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('SETTINGS_PAGE')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('SEND_PAGE')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('BUY_PAGE')
