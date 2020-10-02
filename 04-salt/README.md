# 04 - Salts

People aren't as original as you'd expect and lots of people use the same passwords like "123456" or "password123". If you hash the same password, you get the same resulting hash. Therefore, if multiple people have the same password, if you crack 1, you crack the accounts of everyone with that password.

We can see this in previous situations too!

## Situation

TotallySecure decided to ramp up their security and use *salts* to make sure that different users who use the same password won't have the same hash.

## Salts

A "salt" is a small string of characters that you append to the plaintext _before_ you hash it.

Run the `salt-example.py` script to see an example of different hashes produced by the same plaintext password _but_ with a randomly selected salt.
