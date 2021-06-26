import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

print("Balance", w3.eth.getBalance("0x93C7Dc7636a6870e850CC09C6665AAe21a27e285"))

private_key = os.getenv("PRIVATE_KEY")

print(private_key)
