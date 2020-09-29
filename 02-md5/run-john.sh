# Runs the John The Ripper cracker
john --format=raw-md5 --wordlist=/home/vz/hashes-presentation/top-1000000-passwords.txt hashes.txt
# Show the results
john --show --format=raw-md5 hashes.txt
