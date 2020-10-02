# 03 - sha2

The MD5 algorithm was published in [April 1992](https://en.wikipedia.org/wiki/MD5). One of the newer algorithms is SHA-256. It was [published in 2001](https://en.wikipedia.org/wiki/SHA-2). It's a stronger algorithm but even SHA-256 isn't recommended anymore for security.

Note: "SHA-2" is technically the name of a group of algorithms where SHA-256 was one of them. 

## Situation

TotallySecure had protected their passwords database with something a little stronger than a 30 year old hashing algorithm. 

Let's see how the SHA-256 algorithm stacks up to a dictionary attack...

## Why use a different algorithm?

There are some speed differences but *keyspace*, the length and character-set of the plaintext, is the most important determinant for how fast we can crack a password.

The longer the password, the longer it will take to crack the password.

## Keyspaces and hash attacks

However, there's also the factor of when you store a hash, it's a predetermined length.

All passwords from length 1 to an infinite length have to be able to map to a hash. A SHA-256 hash is always going to be 256 bits large (it looks like a 64-length string). Logically, it's impossible to have a different hash for each of these passwords; there have to be duplicates. Therefore, there exists multiple passwords that can authenticate to the same account! If you can find these "alternate valid passwords", you have yourself a [collision attack](https://en.wikipedia.org/wiki/Collision_attack)! 

We can see this with 2 pictures downloaded by the `hash-collision.sh` script.
