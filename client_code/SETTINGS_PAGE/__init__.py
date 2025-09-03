from ._anvil_designer import SETTINGS_PAGETemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
import plotly.graph_objects as go

class SETTINGS_PAGE(SETTINGS_PAGETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('HOMEPAGE')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('HOMEPAGE')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('VOLUME_SETTINGS_PAGE')
  
