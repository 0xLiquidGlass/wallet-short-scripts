import sys
import pycardano
import mnemonic
import io
import qrcode

listHoldAddress = []

def gen_ada_key(language, entropyStrength):
    paymentPath = str("m/1852'/1815'/0'/0/0")
    stakingPath = str("m/1852'/1815'/0'/2/0")
    
    mnemo = mnemonic.Mnemonic(language)
    seedPhrase = mnemo.generate(entropyStrength)

    hdWallet = pycardano.crypto.bip32.HDWallet
    masterKey = hdWallet.from_mnemonic(seedPhrase)
    
    paymentKeyPath = masterKey.derive_from_path(paymentPath)
    paymentPublicKey = paymentKeyPath.public_key

    stakingKeyPath = masterKey.derive_from_path(stakingPath)
    stakingPublicKey = stakingKeyPath.public_key

    paymentVerificationKey = pycardano.key.PaymentExtendedVerificationKey(paymentPublicKey)
    stakingVerificationKey = pycardano.key.StakeExtendedVerificationKey(stakingPublicKey)

    address = pycardano.Address(payment_part = paymentVerificationKey.hash(),
                                     staking_part = stakingVerificationKey.hash(),
                                     network = pycardano.Network.MAINNET)

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
    with open("ada-address.txt", "w") as qrFile:
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
            execute = gen_ada_key(language, entropyStrength)
        if command == str("--qr") or command == str("-q"):
            execute = obtain_address_qr()
        if command == str("--help") or command == str("-h"):
            execute = help_me()
