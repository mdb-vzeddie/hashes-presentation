#!/usr/bin/python3

import timeit

setup8 = """import random
import string
import hashlib
alphanumeric = string.ascii_lowercase + string.ascii_uppercase + string.digits
wordlist = [''.join(random.choices(alphanumeric, k=8)) for _ in range(0, 1000)]"""

setup128 = """import random
import string
import hashlib
alphanumeric = string.ascii_lowercase + string.ascii_uppercase + string.digits
wordlist = [''.join(random.choices(alphanumeric, k=128)) for _ in range(0, 1000)]"""

test_sha = "[hashlib.sha256(_.encode()).hexdigest() for _ in wordlist]"
test_md5 = "[hashlib.md5(_.encode()).hexdigest() for _ in wordlist]"

print("Running tests...")
sha256_setup8_time = timeit.timeit(setup=setup8, stmt=test_sha, number=1000)
md5_setup8_time = timeit.timeit(setup=setup8, stmt=test_md5, number=1000)
sha256_setup128_time = timeit.timeit(setup=setup128, stmt=test_sha, number=1000)
md5_setup128_time = timeit.timeit(setup=setup128, stmt=test_md5, number=1000)
print("---- SHA-256 timing (1000 rounds of a 1000-length array - 8 chracter password -----")
print("Average time: " + str(sha256_setup8_time))
print("---- MD5 timing (1000 rounds of a 1000-length array - 8 chracter password -----")
print("Average time: " + str(md5_setup8_time))


print("---- SHA-256 timing (1000 rounds of a 1000-length array - 128 chracter password -----")
print("Average time: " + str(sha256_setup128_time))
print("---- MD5 timing (1000 rounds of a 1000-length array - 128 chracter password -----")
print("Average time: " + str(md5_setup128_time))

print("---- Ratio of timing between cracking an 8-length password vs a 128-length password (1:16 ratio) -----")
print("SHA-256: {} times slower".format(float(sha256_setup128_time/sha256_setup8_time)))
print("MD5: {} times slower".format(float(md5_setup128_time/md5_setup8_time)))
