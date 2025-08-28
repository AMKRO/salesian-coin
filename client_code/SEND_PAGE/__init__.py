from ._anvil_designer import SEND_PAGETemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class SEND_PAGE(SEND_PAGETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    while True:
      if self.amount_textbox.text is not None and self.userID_Textbox.text is not None:
        self.submit_button.visible = True
        
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('HOMEPAGE')

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
