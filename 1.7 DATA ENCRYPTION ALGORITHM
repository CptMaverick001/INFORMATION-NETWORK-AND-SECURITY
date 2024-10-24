from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
def des_encrypt(plain_text, key):
# Create DES cipher object
cipher = DES.new(key, DES.MODE_ECB)
# Padding the plain text to be a multiple of 8 bytes
padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
# Encrypt the padded text
encrypted_text = cipher.encrypt(padded_text)
return encrypted_text
def des_decrypt(encrypted_text, key):
# Create DES cipher object
cipher = DES.new(key, DES.MODE_ECB)
# Decrypt the encrypted text
decrypted_padded_text = cipher.decrypt(encrypted_text)
# Unpad the decrypted text
decrypted_text = unpad(decrypted_padded_text, DES.block_size).decode('utf-8')
return decrypted_text
# Example Usage
if __name__ == "__main__":
# 8-byte key (64 bits)
key = b'8bytekey' # DES key must be exactly 8 bytes long
plain_text = "Hello, DES Algorithm!"
print(f"Original Text: {plain_text}")
# Encrypt the plain text
encrypted_text = des_encrypt(plain_text, key)
print(f"Encrypted Text: {encrypted_text.hex()}")
# Decrypt the encrypted text
decrypted_text = des_decrypt(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")
print("Sajid Ahmed")
