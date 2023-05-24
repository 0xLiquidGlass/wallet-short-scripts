import sys
import mnemonic
import bip44
import bech32
import hashlib
import io
import qrcode

derivationPath = str("m/84'/0'/0'/0/0")
witnessVersion = int(0)

mainnetVersionByte = b'\x00'

listHoldAddress = []

def gen_btc_key(language, entropyStrength):
    mnemo = mnemonic.Mnemonic(language)
    seedPhrase = mnemo.generate(entropyStrength)

    wallet = bip44.Wallet(seedPhrase)

    publicKey = wallet.derive_public_key(derivationPath)

    publicKeyHashed = hashlib.sha256(publicKey).digest()

    ripemd160Hash = hashlib.new('ripemd160', publicKeyHashed).digest()

    extendedHash = mainnetVersionByte + ripemd160Hash

    extendedHashSum = bech32.bech32_create_checksum("bc", extendedHash)

    bech32Address = bech32.encode("bc", witnessVersion, ripemd160Hash)

    listHoldAddress.append(bech32Address)

    print("Address: {}\n" .format(bech32Address))
    print("Seed Phrase: {}\n" .format(seedPhrase))
    print("Derivation Path: {}\n" .format(derivationPath))

def obtain_address_qr():
    readData = None
    writeFile = None
    
    currentAddress = listHoldAddress[0]
    qr = qrcode.QRCode()
    qr.add_data(currentAddress)
    textStream = io.StringIO()
    qr.print_ascii(out=textStream)
    textStream.seek(0)
    with open("btc-address.txt", "w") as qrFile:
        readData = textStream.read()
        writeFile = qrFile.write(readData)

def help_me():
    with open("helpme.txt", "r") as readText:
        textToDisplay = readText.read()
        print(textToDisplay)

if __name__ == "__main__":
    language = str("english")
    entropyStrength = int(128)
    execute = None

    for command in sys.argv[1:]:
        if command == str("--generate") or command == str("-g"):
            execute = gen_btc_key(language, entropyStrength)
        if command == str("--qr") or command == str("-q"):
            execute = obtain_address_qr()
        if command == str("--help") or command == str("-h"):
            execute = help_me()
