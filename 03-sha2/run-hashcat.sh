hashcat -a 0 -m 1400 hashes.txt ../top-1000000-passwords.txt -O

# -a 0 -> use a dictionary attack
# -m 1400 -> SHA-256
