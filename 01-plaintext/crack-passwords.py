#!/usr/bin/python3

with open('accounts.csv', 'r') as infile:
    print("----- CRACKING PASSWORD INITIATED -----")
    for line in infile:
        # Naive CSV splitting because this is a demo and it isn't a compsci class
        line = [_.strip()[1:-1] for _ in line.split(',')]
        print(f"Password found! #{line[0]} - {line[1]}:{line[2]}")
    print("----- CRACKING PASSWORD FINISHED -----")
