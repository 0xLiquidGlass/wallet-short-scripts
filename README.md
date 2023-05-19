# wallet-short-scripts
This repo contains scripts for cryptocurrencies. They have minimal functionality so these scripts are only capable of generating a new keypair only

I created this repo as a response to the news that Ledger has implemented Ledger Recover because I believe that we should be owning our keys, not others


## What's new?
### 2023 May 19
- QR code functionality for generated address
- Support for generating Cardano address


## To use the scripts
For this example, I will be using `ethereum/genethkey.py` . All scripts that uses Python will operate the same way unless stated

The `ethereum/` directory contains a script, `genethkey.py` , that allows you to generate a new address (keypair) and the resources needed to make the script work properly

To setup `genethkey.py`, do:

`pip install -r requiements.txt`

To make a new path for your wallet, do:

`mkdir "wallet"`

To generate a new keypair and save it, do:

`python3 genethkey.py --generate > "wallet/SomeEthAddress.txt"`

OR

`python genethkey.py --generate > "wallet/SomeEthAddress.txt"` if you are on Windows


## A makeshift cold wallet THAT YOU FULLY CONTROL

1. Find the directory that is suited for your cryptocurrency (e.g. algorand/)

2. Go to `Code -> Download Zip`

3. Extract the `.zip` file and find the directory identified from point 1 to your external storage device

4. Go into the directory and set up the script

5. Ready to use

## Donations
This is completely optional. To support me, you can donate to me via this address:

```
Ethereum, Matic: 0x96b939aaA7E5660591e51c7d6BA46587532e607A

Algorand: KJVALCPBBTGT4YPVUZIYZYBERU3SVE5Q32MP5I7HVU2GK4JWD56PLRAE7E

Cardano: addr1qyu5v5nh02ueyc08jrf37jamdu7ej85zzfya47fvgh6w3y3af3f65uukq77xtxgcws6qpljyh8sp04r8hlc74scwk5js7mzwqm
```

As more scripts for a specific cryptocurrency has been added, I will list those here as a means of donations