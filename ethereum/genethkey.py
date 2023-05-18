# #!/usr/bin/python3

import sys
import bip44
import bip44.utils
import coincurve
import mnemonic
import io
import qrcode

listHoldAddress = []

def gen_eth_key(language, entropyStrength):
    mnemo = mnemonic.Mnemonic(language)
    seedPhrase = mnemo.generate(entropyStrength)
    seedPhraseLength = len(seedPhrase.split(" "))

    wallet = bip44.Wallet(seedPhrase)
    secretKey, publicKey = wallet.derive_account("eth", account=0)

    secretKey = coincurve.PrivateKey(secretKey)
    secretKey.public_key.format() == publicKey
    address = bip44.utils.get_eth_addr(publicKey)

    listHoldAddress.append(address)
    
    print("Address: {}\n" .format(address))
    print("Seed Phrase: {}\n" .format(seedPhrase))
    print("{} words\n" .format(seedPhraseLength))

def obtain_address_qr():
    readData = None
    writeFile = None
    
    currentAddress = listHoldAddress[0]
    qr = qrcode.QRCode()
    qr.add_data(currentAddress)
    textStream = io.StringIO()
    qr.print_ascii(out=textStream)
    textStream.seek(0)
    with open("eth-address.txt", "w") as qrFile:
        readData = textStream.read()
        writeFile = qrFile.write(readData)

def help_me():
    with open("helpme.txt", "r") as readText:
        textToDisplay = readText.read()
        print(textToDisplay)

if __name__ == "__main__":
    language = str("english")
    entropyStrength = int(256)
    execute = None
    
    for command in sys.argv[1:]:
        if command == str("--generate") or command == str("-g"):
            execute = gen_eth_key(language, entropyStrength)
        if command == str("--qr") or command == str("-q"):
            execute = obtain_address_qr()
        if command == str("--help") or command == str("-h"):
            execute = help_me()
