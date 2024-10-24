def encrypt(text, s):
result = ""
#traverse text
for i in range(len(text)):
char = text[i]
#Encrypt uppercase characters
if(char.isupper()):
result += chr((ord(char) + s - 65) % 26 + 65)
#Encrypt lowercase letters
else:
result += chr((ord(char) + s - 97) % 26 + 97)
return result
#check above function
text = input("Enter the text to encrypt: ")
s = 3
print("Text: " +text)
str(s)
print("Cipher: " +encrypt(text,s))
print("Sajid Ahmed")
