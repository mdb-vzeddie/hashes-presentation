#!/usr/bin/python3

from faker import Faker
import hashlib
import argparse
import random
import logging


class account:
    def __init__(self, username):
        self.username = username
        self.pw_plain = str()
        self.pw_md5 = str()
        self.pw_sha2 = str()
        self.pw_md5_salt = str()

"""
Params:
    n <- number of accounts to generate
    gen_type <- one of [plain|md5|sha2|md5_salt|all] (default: plain)
Returns:
    A dictionary with key = an account ID and value, an 'account' object with the appropriate attributes set
"""
def generate(n, gen_type, wordlist, perc_hpw):

    # Normalize the gen_type
    gen_type = gen_type.strip().lower()
    assert gen_type in ["plain", "md5", "sha2", "md5_salt", "all"]
    account_map = dict() 

    wl_fd = open(wordlist, 'r')

    # Since the wordlist file may be _huge_ (1mil+ lines), it would take forever to iteratively go through them every time we want a new line.
    # Let's employ "reservoir sampling" to get the random lines.
    def get_random_line():
        aline = next(wl_fd)
        for num, aline in enumerate(wl_fd, 2):
            if random.randrange(num): continue
            line = aline
        return line

    def generate_fake_base():
        for count in xrange(n):
            # Generate an email address as a username
            new_account = account(faker.email())
            # Generate a plaintext password
            if perc_hpw != 0:
                i = random.randint(1, 100)
                if i <= perc_hpw:
                    # Strong password
                    j = random.randint(0,1)
                    if j:
                        new_account.pw_plain = ''.join(faker.words(5))
                    else:
                        new_account.pw_plain = faker.uuid4()
                else:
                    # Weak password
                    new_account.pw_plain = "asdf"
            

    def summon_salt():
        pass

    #generate_fake_usernames()
    print(get_random_line())
    wl_fd.close()
    return account_map

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', "--generator-type", help="Generator type is one of: [plain|md5|sha2|md5_salt|all] (default: plain)", default="plain")
    parser.add_argument('-n', "--number", help="Number of accounts to create (default: 250)", default=250)
    parser.add_argument("--plaintext-wordlist", help="The list of words to be used as plaintext passwords", default="/usr/share/wordlists/rockyou.txt")
    parser.add_argument("--percent-random-hard-pw", help="Percentage of passwords that are difficult (0-100)", default=5)
    args = parser.parse_args()

    assert args.percent_random_hard_pw >= 0 and args.percent_random_hard_pw <= 100

    logging.info(f"Going to create {args.number} account(s) of type {args.generator_type}...")

    account_map = generate(args.number, args.generator_type, args.plaintext_wordlist, args.percent_random_hard_pw)
    print(account_map)
