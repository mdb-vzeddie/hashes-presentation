#!/usr/bin/python3

from faker import Faker
import hashlib
import argparse
import random
import logging
import json
import uuid
import string

n = 100

faker = Faker()

types = ["plain", "md5", "sha2", "md5_salt"]
alphanumeric = string.ascii_letters + string.digits
account_map = dict()

wordlist = './top-1000000-passwords.txt'

perc_hpw = 25

# Generate a list of fake passwords
with open(wordlist, 'r') as infile:
    wordlist = infile.readlines()
    wordlist = random.choices(wordlist, k=n)
    wordlist = [_.strip() for _ in wordlist]

used_pws = list()
for count in range(0, n):
    # Generate an email address as a username
    new_username = faker.email()
    # Generate a plaintext password
    if perc_hpw != 0:
        i = random.randint(1, 100)
        if i <= perc_hpw:
            # Strong password
            j = random.randint(0,1)
            if j:
                pw_plain = ''.join(faker.words(5))
            else:
                pw_plain = ''.join(random.choices(alphanumeric, k=8))
        else:
            # Weak password
            j = random.randint(0,10)
            if j != 0:
                pw_plain = wordlist[count]
                used_pws.append(wordlist[count])
            else:
                pw_plain = random.choice(used_pws)
                print("Reusing password for: {} -> {}".format(new_username, pw_plain))
    pw_plain = pw_plain.encode()
    pw_md5 = hashlib.md5(pw_plain).hexdigest()
    pw_sha2 = hashlib.sha256(pw_plain).hexdigest()
    salt = str(random.randint(100, 999)).encode()
    pw_md5_salt = hashlib.md5(pw_plain + salt).hexdigest()
    account_map[count + 1] = {"username": new_username, "pw": pw_plain.decode('ascii'), 'md5': pw_md5, 'sha2': pw_sha2, 'salt': salt.decode('ascii'), 'pw_md5_salt': pw_md5_salt}

import pprint
pprint.pprint(account_map)

with open('accounts.json', 'w') as outfile:
    outfile.write(json.dumps(account_map))
