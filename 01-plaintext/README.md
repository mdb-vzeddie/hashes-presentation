# 01 - Plaintext

In the year 2020, there aren't many online companies who would store their customers' account information in plaintext but truth is often stranger than fiction.

In this universe, TotallySecure shows incredible hubris:

They attest that their firewall completely defends against attackers. They even naively invite hackers to attack their database and say that they don't even need to encrypt their customers' credentials!

For a couple days, their firewall stops every attack: SQL injection, password brute-forcing, utilizing known exploits, etc... Nothing works! 

However, early in the morning, an employee hasn't had their cup of coffee yet and logs in to their email to find that they received an email from their CEO saying they need to send the CEO their username and password to them:

```
From: john.doe@tota11ysecure.com
To: em.ployee@totallysecure.com
Subject: Super Urgent Request!!!
----------
Dear my employee,

This is your CEO, John Doe. I'm writing to inform you about a very urgent matter. I need your username and password right this instant. 
Do not ask questions.

From,
Jon Doe
```

The employee groggily responds to the email with their username and password.

The malicious actors now have credentials to an internal system! Pivoting around, they manage to hit a lower environment server which they listen for connections from other users. One other user is a database administrator who uses the same credentials for this lower environment server as the target database server! 

The lesson is that there is the security concept of "Defense-in-Depth". Even if you have security measures to protect you in some way, there are gains to be had by protecting your data in other ways.

The hackers now have access to a database of plaintext credentials. Let's "crack" them.

### Footnotes

* Defense-in-depth: https://en.wikipedia.org/wiki/Defense_in_depth_(computing)
