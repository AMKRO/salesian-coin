from ._anvil_designer import TRANSACTIONS_PAGETemplate
from anvil import *
import anvil.users
import anvil.server

class TRANSACTIONS_PAGE(TRANSACTIONS_PAGETemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    current_user = anvil.users.get_user()
    if current_user:
      current_user_id = current_user.get_id()
    else:
      current_user_id = None

    if current_user_id:
      transactions = anvil.server.call('get_transactions_for_user', current_user_id)
      self.data_grid_1.items = transactions
    else:
      self.data_grid_1.items = []

  def button_1_click(self, **event_args):
    open_form('HOMEPAGE')
