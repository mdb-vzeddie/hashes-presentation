```python
__author__ = "Vincent Zhen"
__email__ = "vincent.zhen@mongodb.com"
__description__ = "00-situation"
```

# Summary

This is a MongoDB Cybersecurity Month presentation about hashes, password protections, rainbow tables, etc...

The things we cover here will be very basic and pared down so that we can get an overview about password security/protection.

## General Knowledge

I personally have more than 900 accounts scattered across the internet. This includes everything from Google, Amazon, Facebook- to random online stores.

Each of these companies/organizations have to have some way of authenticating me. These would be my *credentials*- my username and password.

It's up to each individual organization to protect your credentials.

## Situation

You've signed up for an account at a website called [http://totally-secure.buy-things-here.com](https://example.com).

One day, they get hacked! Shocking, I know. 

It takes TotallySecure® 3 months to divulge to the public that they had been breached<sup>1</sup>. The hackers were able to get away with usernames, passwords (more on this), etc... We'll focus on the usernames and passwords for now.

## Parallel Universes

<p align="center"> <img src="https://cdn3.whatculture.com/images/2013/03/community-dice-600x338.jpg"> </p>

We will explore 6 different parallel universes where each successive universe has a version of our company, TotallySecure, with stronger password protections (it isn't the most riveting use of scifi multiverses but ¯\\_(ツ)_/¯)

1. They stored credentials in plaintext

2. They stored credentials with a weak hashing algorithm (MD5)

3. They stored credentials with a stronger hashing algorithm (SHA256)

4. They stored credentials with a weak hasing algorithm plus a salt

5. TODO

6. TODO

### Footnotes

1. [Different states have different laws regarding breach notifications. Sometimes it's up to the organization's policy and sometimes the state mandates a certain notification timeline or the company faces penalties](https://www.itgovernanceusa.com/data-breach-notification-laws#:~:text=Notification%20shall%20be%20made%20without,provided%20to%20the%20Attorney%20General.)
2. ["On average, companies take about 197 days to identify and 69 days to contain a breach". This doesn't account for the monetary penalties, lost business, and reputational damage](https://www.ibm.com/security/digital-assets/cost-data-breach-report/#/)
