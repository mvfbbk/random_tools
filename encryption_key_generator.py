#!/usr/bin/python

"""
Programme:  EncryptionKeyGenerator
File:       encryption_key_generator.py
Version:    Alpha0.3
Date:       2021.01.18
Function:   Generate encryption keys of specific lengths from a dictionary
            of possible characters
Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2021
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX
---------------------------------------------------------------------------
GPL v3
---------------------------------------------------------------------------
Description:
============
The script will create a random string to help with file encryption within
openssl processes. The script uses a combined dictionary of ASCII letter 
Characters, digits and puntucation marks. As some punctuation will break 
command-line processes the script will check the genearated password 
against a dictionary of characters known to break CLI functions and replace
these with digits.
---------------------------------------------------------------------------
Usage:
======
This script:
- is written for python 3.7+ and requires only imports from the
  stand python library.
- needs to be called via it's full path and will act on the current working
  directory.
- produces 1 output wich will be the encryption key you will need
- has a default key length of 32 characters if no imput is provided
---------------------------------------------------------------------------
Revision History:
=================
A0.1    04.01.21    Alpha   By: MVF
A0.2    10.01.21    Alpha   By: MVF     Comment: included loop to check 
                                                generated password for 
                                                CLI-breaking characters and
                                                replace these with digits.
A0.3    18.01.21    Alpha   By: MVF     Comment: added default value to
                                                function
"""

import random
import string

def get_random_password_string(length, default=32):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    bad_characters = [" ", "!", '"', "#", "$", "&", "'", "(", ")", "*", ",", ";", "<", ">", "?", "[", "\\", "]", "^", "`", "{", "|", "}"]
    for i in password:
        if i in bad_characters:
            password = password.replace(i, random.choice(string.digits))

    print("Your key is: ", password)

if __name__ == '__main__':
    key_len = int(input("How long to you need your key be be: "))
    get_random_password_string(key_len)
