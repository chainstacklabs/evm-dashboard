# EVM-Dashboard
Script for collecting Ethereum Block data and adding it to a google script
# Description

This is repo contains the codes used in the " How to buidl your own web3 dashboard " blog. Unlike in the blog, the code in the repository has been modularized into different files that are named according to its functionality. The code does the following 

* Connect to Chainstack node via wss endpoint
* Fetch latest blocks
* Retrieves information from the block
* Adds the retrieved information to the specified google sheets

# Getting started

Before running the code, it is highly recommended that you go through the blog as it describes the whole logic of the code. Once you have a proper idea, you can run the code by

* Installing all the required python packages
  
    ```
    pip install -r requirements.txt
    ```

* Running the [get_transaction.py](get_transaction.py) file
  
    ```
    python get_transaction.py
    ```