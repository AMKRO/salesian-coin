from ._anvil_designer import SEND_PAGETemplate
from anvil import *
import anvil.server

class SEND_PAGE(SEND_PAGETemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.submit_button.visible = False  # hide initially

    # Set event handlers for textboxes
    self.userID_Textbox.set_event_handler('change', self.on_text_change)
    self.amount_textbox.set_event_handler('change', self.on_text_change)

  def on_text_change(self, **event_args):
    # Show button only if both fields have text
    if self.userID_Textbox.text and self.amount_textbox.text:
      self.submit_button.visible = True
    else:
      self.submit_button.visible = False

  def submit_button_click(self, **event_args):
    import anvil.users    
    user_id = self.userID_Textbox.text.strip()
    amount = self.amount_textbox.text.strip()

    current_user = anvil.users.get_user()
    if current_user:
      sender_id = current_user.get_id()  # or current_user['email'], depending on your setup
    else:
      sender_id = "unknown"

    transaction = {
      "sender": sender_id,
      "recipient": user_id,
      "amount": amount
    }
    
    if not user_id or not amount:
      alert("Please enter both recipient and amount.")
      return

    try:
      block_hash = anvil.server.call('add_transaction', transaction)
      alert(f"Block mined! Hash: {block_hash}")

      # Clear inputs and hide button
      self.userID_Textbox.text = ""
      self.amount_textbox.text = ""
      self.submit_button.visible = False
    except Exception as e:
      alert(f"Error: {str(e)}")

  def button_1_click(self, **event_args):
    open_form('HOMEPAGE')
    pass
