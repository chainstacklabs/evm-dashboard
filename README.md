<img width="1200" alt="Labs" src="https://user-images.githubusercontent.com/99700157/213291931-5a822628-5b8a-4768-980d-65f324985d32.png">

<p>
 <h3 align="center">Chainstack is the leading suite of services connecting developers with Web3 infrastructure</h3>
</p>

<p align="center">
  <a target="_blank" href="https://chainstack.com/build-better-with-ethereum/"><img src="https://github.com/soos3d/blockchain-badges/blob/main/protocols_badges/Ethereum.svg" /></a>&nbsp;  
  <a target="_blank" href="https://chainstack.com/build-better-with-bnb-smart-chain/"><img src="https://github.com/soos3d/blockchain-badges/blob/main/protocols_badges/BNB.svg" /></a>&nbsp;
  <a target="_blank" href="https://chainstack.com/build-better-with-polygon/"><img src="https://github.com/soos3d/blockchain-badges/blob/main/protocols_badges/Polygon.svg" /></a>&nbsp;
  <a target="_blank" href="https://chainstack.com/build-better-with-avalanche/"><img src="https://github.com/soos3d/blockchain-badges/blob/main/protocols_badges/Avalanche.svg" /></a>&nbsp;
  <a target="_blank" href="https://chainstack.com/build-better-with-fantom/"><img src="https://github.com/soos3d/blockchain-badges/blob/main/protocols_badges/Fantom.svg" /></a>&nbsp;
</p>

<p align="center">
  <a target="_blank" href="https://chainstack.com/protocols/">Supported protocols</a> •
  <a target="_blank" href="https://chainstack.com/blog/">Chainstack blog</a> •
  <a target="_blank" href="https://docs.chainstack.com/">Chainstack docs</a> •
  <a target="_blank" href="https://docs.chainstack.com/api/">Blockchain API reference</a> •
  <a target="_blank" href="https://console.chainstack.com/user/account/create">Start for free</a>
</p>

# EVM Dashboard using Python

Script for collecting Ethereum Block data to build an excellent Web3-based dashboard on your own using a bit of Python and a Google spreadsheet.

Read the full tutorial on the Chainstack blog:
* [How to buidl your own Web3 dashboard](https://chainstack.com/how-to-buidl-your-own-web3-dashboard/)

## Project details

This repository holds the code used in the [How to buidl your web3 dashboard](https://chainstack.com/how-to-buidl-your-own-web3-dashboard/) tutorial. Unlike in the blog, the code in the repository is modularized into different files named according to its functionality. The code does the following: 

* Connect to Chainstack node via WSS endpoint
* Fetch the latest blocks
* Retrieves information from the block
* Adds the retrieved information to the specified google sheets

# Quick start

Before running the code, it is highly recommended that you go through the blog as it describes the whole logic of the code.

Clone this repository.

Install the Python dependencies:
  
```sh
pip install -r requirements.txt
```

Run the [get_transaction.py](get_transaction.py) file:

```sh
python get_transaction.py
```

## Prerequisites

* Python ^3.6
* A node RPC endpoint.

Deploy a node with Chainstack:

1. [Sign up with Chainstack](https://console.chainstack.com/user/account/create).  
1. [Deploy a node](https://docs.chainstack.com/platform/join-a-public-network).  
1. [View node access and credentials](https://docs.chainstack.com/platform/view-node-access-and-credentials). 

## Dependencies

* gspread ^5.4.0
* web3.py ^5.29.2
* websockets ^9.1

## Install

Install Python on your system:

* [Install Python](https://realpython.com/installing-python/)

Clone this repository.

Install the Python dependencies:
  
```sh
pip install -r requirements.txt
```
