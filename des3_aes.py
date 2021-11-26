# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:51:16 2020

@author: edala
"""

from Crypto.Cipher import DES3, AES

def decryption_DES3(ciphertext, key):
    cipher = DES3.new(key)
    encrypted_data = cipher.encrypt(ciphertext)
    print("Encrypted text is: ", encrypted_data)
    print("Upon decryption of above cipher, we are returned: ",cipher.decrypt(encrypted_data))

def decryption_AES(ciphertext, key):
    cipher = AES.new(key)
    encrypted_data = cipher.encrypt(ciphertext)
    print("Encrypted text is: ", encrypted_data)
    print("Upon decryption of above cipher, we are returned: ",cipher.decrypt(encrypted_data))