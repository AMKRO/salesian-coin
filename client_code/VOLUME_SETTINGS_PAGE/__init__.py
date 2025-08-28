from ._anvil_designer import VOLUME_SETTINGS_PAGETemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class VOLUME_SETTINGS_PAGE(VOLUME_SETTINGS_PAGETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
