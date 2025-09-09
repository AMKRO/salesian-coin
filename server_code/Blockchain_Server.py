import time
import hashlib
from anvil.tables import app_tables
import anvil.server

difficulty = 1

class Block:
  def __init__(self, previousHash, timestamp, nonce, hash, transactions):
    self.previousHash = previousHash
    self.timestamp = timestamp
    self.nonce = nonce
    self.hash = hash
    self.transactions = transactions

class LinkedList:
  def __init__(self):
    self.chain = self.load_chain()

  def load_chain(self):
    chain = []
    for block_row in app_tables.blockchain.search():
      block = Block(
        block_row['previous_hash'],
        block_row['timestamp'],
        block_row['nonce'],
        block_row['hash'],
        block_row['transactionList']
      )
      chain.append(block)
    chain.sort(key=lambda b: b.timestamp)
    return chain

  def add_block(self, block):
    app_tables.blockchain.add_row(
      previous_hash=block.previousHash,
      timestamp=block.timestamp,
      nonce=block.nonce,
      hash=block.hash,
      transactionList=block.transactions
    )
    self.chain.append(block)

  def get_last_hash(self):
    if len(self.chain) == 0:
      return "0"*64
    else:
      return self.chain[-1].hash

class Generate:
  def calcHash(self, transactions, timestamp, previous_hash, nonce):
    block = str(transactions) + str(timestamp) + str(previous_hash) + str(nonce)
    return hashlib.sha256(block.encode()).hexdigest()

  def generateBlock(self, transactions, linked_list):
    previous_hash = linked_list.get_last_hash()
    nonce = 0
    while True:
      timestamp = time.time()
      tempHash = self.calcHash(transactions, timestamp, previous_hash, nonce)
      if tempHash.startswith('0' * difficulty):
        return Block(previous_hash, timestamp, nonce, tempHash, transactions)
      else:
        nonce += 1

generator = Generate()
linked_list = LinkedList()

@anvil.server.callable
def add_transaction(transaction):
  # transaction is expected as a dict with keys like "recipient" and "amount"
  if not isinstance(transaction, dict):
    raise ValueError("Transaction must be a dictionary")

  transactions_list = [transaction]  # blockSize = 1 for simplicity
  block = generator.generateBlock(transactions_list, linked_list)
  linked_list.add_block(block)
  return block.hash
