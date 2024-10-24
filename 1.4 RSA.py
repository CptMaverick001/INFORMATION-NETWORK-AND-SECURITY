from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
keypair = RSA.generate(1024)
pubKey = keypair.publickey()
print(f"Public Key: (n={hex(pubKey.n)}, e = {hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
print(f"Private Key: (n={hex(pubKey.n)}, d = {hex(keypair.d)})")
privKeyPEM = keypair.exportKey()
print(privKeyPEM.decode('ascii'))
#encryption
msg = b"Mahek"
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg) # Encode the message to bytes
print("Encrypted: ", binascii.hexlify(encrypted))
print("Sajid Ahmed")
