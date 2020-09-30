#!/usr/bin/python3

import argparse
import hashlib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--wordlist', '-w', help="the wordlist to generate a rainbow table for", default="../top-1000000-passwords.txt")
    parser.add_argument('--algorithm', '-a', help="the algorithm to generate a rainbow table for. one of md5, sha1, sha256, or sha512", default="md5")
    args = parser.parse_args()

    args.algorithm = args.algorithm.lower()
    assert args.algorithm in ["md5", "sha1", "sha256", "sha512"]

    with open(args.wordlist, 'r') as infile:
        for line in infile:
            if args.algorithm == "md5":
                h = hashlib.md5(line.encode()).hexdigest()
            elif args.algorithm == "sha1":
                h = hashlib.sha1(line.encode()).hexdigest()
            elif args.algorithm == "sha256":
                h = hashlib.sha256(line.encode()).hexdigest()
            elif args.algorithm == "sha512":
                h = hashlib.sha512(line.encode()).hexdigest()
            print(f"{h}:{line.strip()}")
