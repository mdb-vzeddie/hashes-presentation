# 02 - MD5

## What is a hash?

In a sentence, a *hash* is a one-way obfuscation function. The idea is that you can get from a plaintext (secret) item to an obfuscated item _but_ you can't easily get from the obfuscated item back to the plaintext.

For example, we can the small `generate-hash.py` script included in this repo:

```bash
>$ ./generate-hash.py --password MY_PASSWORD --algorithm md5
de28f5c96dd578824fbe879f4c47e96e:MY_PASSWORD
```

The random letters and numbers preceding the colon (':') is the _hash_ while the plaintext is on the right.

## Why use a hash?

When you authenticate to a service online, you are sending some credentials to a server. The server needs to know if your password matches what you registered with.

For example, if you registered to TotallySecure using a password: `MY_PASSWORD`, you can tell TotallySecure that your password is `MY_PASSWORD`, it would compare `MY_PASSWORD` (your input) to `MY_PASSWORD` (the stored password). Since they're the same, you're authenticated.

However, we've seen previously that storing credentials in plaintext is a ticking time bomb.

Enter: the hash-

Suppose TotallySecure stored a _hash_ instead of the plaintext password; they store `de28f5c96dd578824fbe879f4c47e96e` instead of `MY_PASSWORD`. 

When you authenticate, you send `MY_PASSWORD` to the server. The server takes `MY_PASSWORD` and hashes it with the hashing algorithm and gets `de28f5c96dd578824fbe879f4c47e96e`. Now it can compare `de28f5c96dd578824fbe879f4c47e96e` (your input) to `de28f5c96dd578824fbe879f4c47e96e` (the stored credential). Since they're the same, you're authenticated!

...and now if the hackers steal the database, they won't simply have your credentials immediately.

## The MD5 hash

The MD5 hash is one of the earlier hashes to be used in the internet. It has since been depcrecated and shouldn't be used for security purposes: https://tools.ietf.org/id/draft-lvelvindron-tls-md5-sha1-deprecate-01.html#:~:text=MD5%20has%20been%20deprecated%20by,potential%20for%20brute%2Dforce%20attack.

The reason why we don't use it anymore is because there have been exploits discovered against the hash. These exploits include things like the "chosen-plaintext attack" or the "ciphertext-only attack". The specifics of those attacks are outside the scope of this demo though.

However, it's really fast nowadays and I will use the MD5 hashing algorithm to showcase some cracking tools!

## Tools

### John The Ripper (JTR)

Seen as more of a CPU-bound cracker, it is one of the easier tools for cracking passwords. Usually used if you have a wordlist and if the passwords are short.

### Hashcat 

Seen as more GPU-bound. It is extensible and powerful but requires significant hardware resources to effectively utilize.

### Others

The above 2 password cracking tools are good to use but they're definitely not the be-all-end-all of cracking toolsets. In addition, I'm running this in a virtual machine with virtual resources so it's not the most efficient. The above tools I used are generally used to crack local lists of hashes, not over the internet or other protocols.

Other tools include:

* [oclhashcat](https://hashcat.net/wiki/doku.php?id=oclhashcat) - more efficiently utilizes the GPU 
* [aircrack-ng](https://www.aircrack-ng.org/) - generally specialized for wifi security cracking
* [hydra](https://github.com/vanhauser-thc/thc-hydra) - usually used for cracking internet accounts

## Footnotes

* Cipher attacks: https://en.wikipedia.org/wiki/Cryptanalysis#Amount_of_information_available_to_the_attacker
* [GPU acceleration can be 20x the speed without GPU acceleration](https://vk5uj.com/hashcat-versus-oclhashcat-speed/#:~:text=If%20you're%20familiar%20with,is%20the%20GPU%20version%2C%20oclHashcat.&text=While%20this%20will%20get%20you,be%20weeks%2Fmonths%2Fyears.)
