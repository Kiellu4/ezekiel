from Crypto.PublicKey import RSA    #RSA: To handle RSA key import.
from Crypto.Cipher import PKCS1_OAEP    #PKCS1_OAEP: A padding scheme used for secure RSA encryption.
import base64   #base64: For decoding the public key and encoding the ciphertext.

def encrypt_with_public_key(public_key_b64, plaintext):
    # Decode the Base64-encoded public key
    public_key_der = base64.b64decode(public_key_b64)
    public_key = RSA.import_key(public_key_der)
    
    # Create cipher with OAEP padding
    cipher = PKCS1_OAEP.new(public_key)
    
    # Encrypt the plaintext
    encrypted_data = cipher.encrypt(plaintext.encode('utf-8'))
    
    # Return Base64-encoded ciphertext
    return base64.b64encode(encrypted_data).decode('utf-8')

if __name__ == "__main__":
    # Get Base64 public key from user input
    print("\nEnter Base64-encoded RSA public key: ")
    public_key_b64 = input().strip()
    
    # Get plaintext to encrypt
    print("\nEnter plaintext to encrypt: ")
    plaintext = input().strip()
    
    # Encrypt and display result
    try:
        ciphertext_b64 = encrypt_with_public_key(public_key_b64, plaintext)
        print("\nEncrypted Data (Base64): ")
        print(ciphertext_b64)
    except Exception as e:
        print(f"\nError during encryption: {e}")
