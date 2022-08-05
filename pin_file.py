import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ["api_key"]
api_secret = os.environ["api_secret"]
api_token = os.environ["api_token"]

# Pin File
pinata_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
web3storage_url = "https://api.web3.storage/upload"

payload={}
files=[
  ('file',('test.png',open('test.png','rb'),'image/png'))
]

pinata_headers = {
  'pinata_api_key': api_key,
  'pinata_secret_api_key': api_secret
}

web3storage_headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + api_token
#   'Content-Type': 'multipart/form-data'
}

# # pin to Web3.Storage
# response = requests.request("POST", web3storage_url, headers=web3storage_headers, data=payload, files=files)
# print(response.text)
# ipfs_hash = response.json()['cid']
# print(ipfs_hash)

# pin to pinata
response = requests.request("POST", pinata_url, headers=pinata_headers, data=payload, files=files)
print(response.text)
ipfs_hash = response.json()['IpfsHash']
print(ipfs_hash)

