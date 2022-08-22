import asyncio
from process_store_data import addDataToSheet 
import websockets
import json
from web3 import Web3

#setting the wsss endpoint
CHAINSTACK_WSS_ENDPOINT = "<CHAINSTACK-NODE-WSS-ENDPOINT>"

#function to 
# -> establish connection
# -> send the required rpc object
# -> receive and process the corresponding the response
# returns result

async def send_receive_data(_request_data):
    async with websockets.connect(CHAINSTACK_WSS_ENDPOINT) as websocket:
        await websocket.send(json.dumps(_request_data))
        resp = await websocket.recv()    
        return json.loads(resp)["result"]

#function to fetch the filter id
async def get_filter_id():
    #prepping the request
    request_data = {
        "jsonrpc": "2.0",
        "method": "eth_newBlockFilter",
        "params": [],
        "id": 1
    }
    #fetching the id
    filter_id = await send_receive_data(request_data)
    return filter_id


#function to 
# -> fetch the new blocks that gets added to the chain
#
async def get_block_details():
    #get the filter id
    filter_id = await get_filter_id()
    #prepare request using filter id
    request_data = {
    "jsonrpc": "2.0",
    "method": "eth_getFilterChanges",
    "params": [filter_id],
    "id": 0
    }
    #connect to  a chainstack node
    w3 = Web3(Web3.WebsocketProvider(CHAINSTACK_WSS_ENDPOINT))
    while True:
        new_block_hash = await send_receive_data(request_data)
        #pass the hash value list to get_transaction_detail
        if(len(new_block_hash) != 0):
        #fetch the block details
           block =  w3.eth.get_block(new_block_hash[0])
           addDataToSheet(block)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_block_details())
    loop.close()



# use ctrl + z to break the loop
