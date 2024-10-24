import java.util.Scanner;
public class MonoalphabeticCipher {
private static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
private static final String CIPHER_ALPHABET =
"QWERTYUIOPASDFGHJKLZXCVBNM"; // Example cipher alphabet
// Encrypts the plaintext using the cipher alphabet
public static String encrypt(String plaintext) {
StringBuilder ciphertext = new StringBuilder();
for (char c : plaintext.toUpperCase().toCharArray()) {
if (ALPHABET.indexOf(c) != -1) {
int index = ALPHABET.indexOf(c);
ciphertext.append(CIPHER_ALPHABET.charAt(index));
} else {
ciphertext.append(c); // Non-alphabet characters are added unchanged
}
}
return ciphertext.toString(); // Corrected
}
// Decrypts the ciphertext using the cipher alphabet
public static String decrypt(String ciphertext) {
StringBuilder plaintext = new StringBuilder();
for (char c : ciphertext.toUpperCase().toCharArray()) {
if (CIPHER_ALPHABET.indexOf(c) != -1) {
int index = CIPHER_ALPHABET.indexOf(c);
plaintext.append(ALPHABET.charAt(index));
} else {
plaintext.append(c); // Non-alphabet characters are added unchanged
}
}
return plaintext.toString(); // Corrected
}
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
System.out.print("Enter the plaintext: ");
String plaintext = scanner.nextLine();
String ciphertext = encrypt(plaintext);
System.out.println("Encrypted text: " + ciphertext);
System.out.print("Enter the ciphertext to decrypt: ");
String inputCiphertext = scanner.nextLine();
String decryptedText = decrypt(inputCiphertext);
System.out.println("Decrypted text: " + decryptedText);
scanner.close();
}
}
