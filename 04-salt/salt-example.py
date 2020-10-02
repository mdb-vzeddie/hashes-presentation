#!/usr/bin/python3

import hashlib
import random

pw = "MY_PASSWORD"

print("Your password is: {}".format(pw))
print("---------------------------")
salt = str(random.randint(100,999))
print("Your salt is now: {}".format(salt))
s1 = pw + salt
print("The SHA-256 hash is: {}".format(hashlib.sha256(s1.encode()).hexdigest()))

salt = str(random.randint(100,999))
print("Your salt is now: {}".format(salt))
s2 = pw + salt
print("The SHA-256 hash is: {}".format(hashlib.sha256(s2.encode()).hexdigest()))
