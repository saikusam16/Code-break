# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:48:32 2020

@author: edala
"""
import des_full, des3_aes, rsa, playfair, hill, row_transposition, caesar, vigenere, feistel, rail_fence

print("\nWelcome to CodeBreak. The following algorithm decryptions are possible.\n")
print("1. Playfair cipher") # Contributed by Mounika
print("2. Hill cipher") # Contributed by Prabhu
print("3. Row transposition cipher") # Contributed by Bhavana
print("4. Caesar cipher") # Contributed by Kusam
print("5. Data Encryption Standard") # Contributed by Abhiram
print("6. Rail fence cipher") # Contributed by Amey
print("7. Rivest Shamir Adleman") # Contributed by Steve and Naveen(keygen)
print("8. Vigenere cipher") # Contributed by Purna Sai
print("9. Feistel cipher") # Contributed by Manan
print("10. Triple Data Encryption Standard")
print("11. Advanced Encryption Standard")

choice = 0
while True:
    try:
        choice = int(input("Enter the index number of the decryption algorithm required: "))
    except:
        print("Invalid input. Try again.")
    else:
        break

if (choice == 1):
    key = input("Enter the key: ")    # Example key: "Sample key"
    message = input("Enter the ciphertext message: ")   # Example ciphertext: "RI DL DL MA XS BN NS SB NP KE NB QL DE AM DY"
    print("\nBEGINNING DECRYPTION PROCESS\n")
    print("The plaintext is", playfair.decryptor(key, message))
    
if (choice == 2):
    hill.decryptor() # Example key: "HILL", Example ciphertext: "CVUCUCQQTNHLOGTVDHYKMEOOXB"
    
if (choice == 3):
    key = int(input("Enter the key: "))    # Example key: "8"
    message = input("Enter the ciphertext message: ")   # Example ciphertext: "Cenoonommstmme oo snnio. s s c"
    print("\nBEGINNING DECRYPTION PROCESS\n")
    print("The plaintext is", row_transposition.decryptor(key, message))
    
if (choice == 4):
    key = int(input("Enter the key: "))    # Example key: "3"
    message = input("Enter the ciphertext message: ")   # Example ciphertext: "wrehruqrwwreh"
    print("\nBEGINNING DECRYPTION PROCESS\n")
    print("The plaintext is", caesar.decryptor(key, message))

if (choice == 5):
    ciphertext = input("Enter your text: ") # Example text: "C0B7A8D05F3A829C"
    key = input("Enter the round key: ") # Example key: "AABB09182736CCDD"
    print("\n BEGINNING DECRYPTION PROCESS \n")
    print("\nThe plaintext is:", des_full.decryption(ciphertext, key))
    
if (choice == 10 or choice == 11):
    ciphertext = input("Enter any text: ") # Example input: "0123456789abcdef"
    key = input("Enter any 16 or 24 byte key: ") # Example key: "sixteen byte key"
    print("\nBEGINNING TRANSFORMATION PROCESS")
    if (choice == 10):
        des3_aes.decryption_DES3(ciphertext, key)
    else:
        des3_aes.decryption_AES(ciphertext, key)
        
if (choice == 7):
    s = print("Do you want to encrypt a new message? (y or n): ")
    if (s=="y"):
        message = print("Enter your plaintext: ")
        rsa.action("encrypt", message)
    else:
        print("Using keys from group_2_pubkey.txt and group_2_privkey.txt")
        print("Decoding encrypted text from rsa_buffer.txt")
        rsa.action("decrypt")
        

if (choice == 8):
    key = input("Enter the key: ")   # Example key: "sample"
    message = input("Enter the ciphertext message: ")   # Example ciphertext: "lhuhtwlhqezawraugmyeztci"
    print("\nBEGINNING DECRYPTION PROCESS\n")
    print("The plaintext is", vigenere.decryptor(key, message))

if (choice == 9):
    message = input("Enter any text message: ")
    print("\nBEGINNING ENCRYPTION/DECRYPTION PROCESS\n") # Example input "Group two is sending a message to you"
    feistel.action(message)

if (choice == 6):
    rail_fence.decryptor() # Example ciphertext: "Ti samsaefo ru whsi  esg rmgopto", Example key: 2