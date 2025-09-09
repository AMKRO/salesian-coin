import anvil.tables as tables
from anvil.tables import app_tables
from datetime import datetime
import anvil.server

@anvil.server.callable
def get_all_transactions():
  tx_list = []
  for block in app_tables.blockchain.search():
    date_str = datetime.fromtimestamp(block['timestamp']).strftime("%d/%m/%Y")
    for tx in block['transactionList']:
      tx_list.append({
        'date': date_str,
        'sender': tx.get('sender', ''),
        'recipient': tx.get('recipient', ''),
        'amount': tx.get('amount', ''),
        'type': 'N/A'
      })
  print(f"Returning {len(tx_list)} transactions from server")
  return tx_list

def get_transactions_for_user(user_id):
  tx_list = []
  for block in app_tables.blockchain.search():
    date_str = datetime.fromtimestamp(block['timestamp']).strftime("%d/%m/%Y")
    for tx in block['transactionList']:
      sender = tx.get('sender')
      recipient = tx.get('recipient')
      amount = tx.get('amount')

      if sender == user_id:
        tx_list.append({
          'date': date_str,
          'sender': sender,
          'recipient': recipient,
          'amount': amount,
          'type': 'Outgoing'
        })
      elif recipient == user_id:
        tx_list.append({
          'date': date_str,
          'sender': sender,
          'recipient': recipient,
          'amount': amount,
          'type': 'Incoming'
        })
  return tx_list
