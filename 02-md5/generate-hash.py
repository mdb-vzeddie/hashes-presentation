#!/usr/bin/python3

import argparse
import hashlib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--password", '-p', help="the password you want to hash", required=True)
    parser.add_argument('--algorithm', '-a', help="the algorithm to generate a rainbow table for. one of md5, sha1, sha256, or sha512", default="md5")
    args = parser.parse_args()

    args.algorithm = args.algorithm.lower()
    assert args.algorithm in ["md5", "sha1", "sha256", "sha512"]

    if args.algorithm == "md5":
        h = hashlib.md5(args.password.encode()).hexdigest()
    elif args.algorithm == "sha1":
        h = hashlib.sha1(args.password.encode()).hexdigest()
    elif args.algorithm == "sha256":
        h = hashlib.sha256(args.password.encode()).hexdigest()
    elif args.algorithm == "sha512":
        h = hashlib.sha512(args.password.encode()).hexdigest()
    print(f"{h}:{args.password}")
