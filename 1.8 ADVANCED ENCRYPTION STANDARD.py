from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
def aes_encrypt(plain_text, key):
# Create AES cipher object with CBC mode
cipher = AES.new(key, AES.MODE_CBC)
# Padding the plain text to be a multiple of 16 bytes (AES block size)
padded_text = pad(plain_text.encode('utf-8'), AES.block_size)
# Encrypt the padded text
encrypted_text = cipher.encrypt(padded_text)
# Return the encrypted text along with the initialization vector (IV)
return base64.b64encode(cipher.iv + encrypted_text).decode('utf-8')
def aes_decrypt(encrypted_text, key):
# Decode the base64 encoded encrypted text
encrypted_text = base64.b64decode(encrypted_text)
# Extract the IV and the actual encrypted text
iv = encrypted_text[:AES.block_size]
encrypted_text = encrypted_text[AES.block_size:]
# Create AES cipher object with the extracted IV
cipher = AES.new(key, AES.MODE_CBC, iv)
# Decrypt the encrypted text
decrypted_padded_text = cipher.decrypt(encrypted_text)

# Unpad the decrypted text
decrypted_text = unpad(decrypted_padded_text, AES.block_size).decode('utf-8')
return decrypted_text
# Example Usage
if __name__ == "__main__":
# 16-byte key (128 bits)
key = get_random_bytes(16) # AES key must be 16, 24, or 32 bytes long
plain_text = "Hello, AES Algorithm!"
print(f"Original Text: {plain_text}")
# Encrypt the plain text
encrypted_text = aes_encrypt(plain_text, key)
print(f"Encrypted Text (Base64): {encrypted_text}")
# Decrypt the encrypted text
decrypted_text = aes_decrypt(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")
print("Sajid Ahmed")
