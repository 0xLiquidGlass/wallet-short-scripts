# #!/usr/bin/python3

import sys
import algosdk
import io
import qrcode

listHoldAddress = []

def gen_algo_key():
    privateKey, address = algosdk.account.generate_account()
    seedPhrase = algosdk.mnemonic.from_private_key(privateKey)

    listHoldAddress.append(address)
    
    print("Address: {}\n" .format(address))
    print("Seed Phrase: {}\n" .format(seedPhrase))

def obtain_address_qr():
    readData = None
    writeFile = None
    
    currentAddress = listHoldAddress[0]
    qr = qrcode.QRCode()
    qr.add_data(currentAddress)
    textStream = io.StringIO()
    qr.print_ascii(out=textStream)
    textStream.seek(0)
    with open("algo-address.txt", "w") as qrFile:
        readData = textStream.read()
        writeFile = qrFile.write(readData)

def help_me():
    with open("helpme.txt", "r") as readText:
        textToDisplay = readText.read()
        print(textToDisplay)

if __name__ == "__main__":
    execute = None
    for command in sys.argv[1:]:
        if command == str("--generate") or command == str("-g"):
            execute = gen_algo_key()
        if command == str("--qr") or command == str("-q"):
            execute = obtain_address_qr()
        if command == str("--help") or command == str("-h"):
            execute = help_me()
