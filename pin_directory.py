import requests
from dotenv import load_dotenv
import os
import typing as tp

load_dotenv()

api_key = os.environ["api_key"]
api_secret = os.environ["api_secret"]
api_jwt = os.environ["api_jwt"]
api_token = os.environ["api_token"]


web3storage_headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + api_token
}

pinata_headers = {
  'pinata_api_key': api_key,
  'pinata_secret_api_key': api_secret
}

def get_all_files(directory: str) -> tp.List[str]:
    paths: tp.List[str] = []
    for root, dirs, files_ in os.walk(directory):        
        for file in files_:            
             paths.append(os.path.join(root, file))
    return paths

pinata_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
web3storage_url = "https://api.web3.storage/upload"

payload={}
all_files: tp.List[str] = get_all_files('./build')            
files = [('file', (file, open(file, "rb"))) for file in all_files]
print(files)

# # pin to Web3.Storage
# response = requests.request("POST", web3storage_url, headers=web3storage_headers, data=payload, files=files)
# print(response.text)
# ipfs_hash = response.json()['cid']
# print(ipfs_hash)

# pin to Pinata
response = requests.request("POST", pinata_url, headers=pinata_headers, data=payload, files=files)
print(response.text)
ipfs_hash = response.json()['IpfsHash']
print(ipfs_hash)

