# #!/usr/bin/python3

import sys
import algosdk

def gen_algo_key():
    privateKey, address = algosdk.account.generate_account()
    seedPhrase = algosdk.mnemonic.from_private_key(privateKey)
    print("Address: {}\n" .format(address))
    print("Seed Phrase: {}\n" .format(seedPhrase))

def help_me():
    with open("helpme.txt", "r") as readText:
        textToDisplay = readText.read()
        print(textToDisplay)

if __name__ == "__main__":
    execute = None
    for command in sys.argv[1:]:
        if command == str("--generate") or command == str("-g"):
            execute = gen_algo_key()
        if command == str("--help") or command == str("-h"):
            execute = help_me()
