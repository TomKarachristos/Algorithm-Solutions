#!/bin/python3

import os
import sys

dis = {}


def is_prime(n):
    if (n in dis):
        return True
    return False


# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 
      
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print 2, 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print i, 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print n 
          
# Driver Program to test above function 
  
n = 315
primeFactors(n) 
  
# This code is contributed by Harshit Agrawal 


def sieveOfAtkin(limit):
    sieve = [False] * (limit + 1)
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5): sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7: sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11: sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False
    for p in range(5, limit):
        if sieve[p]:
            dis[p] = True
    dis[2] = True
    dis[3] = True

n = 7
sieveOfAtkin(99999)
primeDigitSums(n)

file = open("testfile.txt","w")

for i in valid_nonPrime_number:
    file.write("isValid[" + str(i) + "] = " +  "True" + "\n")

