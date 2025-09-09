from ._anvil_designer import TRANSACTIONS_PAGETemplate
from anvil import *
import anvil.users
import anvil.server

class TRANSACTIONS_PAGE(TRANSACTIONS_PAGETemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    transactions = anvil.server.call('get_all_transactions')
    print(f"Transactions fetched: {transactions}")  # DEBUG
    self.data_grid_1.items = transactions

  def button_1_click(self, **event_args):
    open_form('HOMEPAGE')
