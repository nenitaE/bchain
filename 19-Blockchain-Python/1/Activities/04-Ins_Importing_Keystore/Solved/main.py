import os
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from eth_account import Account

from pathlib import Path
from getpass import getpass

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

account_one = Account.from_key(os.getenv("PRIVATE_KEY"))

# with open(Path("./keystore")) as keyfile:
with open(Path("./UTC--2021-06-24T20-52-13.876Z--93c7dc7636a6870e850cc09c6665aae21a27e285")) as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(
        encrypted_key, getpass("Enter keystore password: ")
    )
    account_two = Account.from_key(private_key)


def create_raw_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }


def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()


print(account_one.address)
print(account_two.address)
