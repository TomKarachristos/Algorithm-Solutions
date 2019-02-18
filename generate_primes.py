#!/bin/python3

import os
import sys

dis = {}


def is_prime(n):
    if (n in dis):
        return True
    return False


valid_nonPrime_number = []
def check_valid_numbers(ninenine, real_n):
    valid_numbers = 0
    for number in range(10 ** (real_n - 1), int(ninenine)):
        if (checkRules(number, real_n)):
            valid_numbers = valid_numbers + 1
            valid_nonPrime_number.append(number)
    return valid_numbers


def checkRules(number, real_n):
    digits = [int(i) for i in str(number)]
    digital_len = len(digits)
    for index in range(real_n - 2):
        if (index < digital_len - 2):
            string_3_digit = digits[index] + digits[index + 1] + digits[index + 2]
            if (not is_prime(string_3_digit)):
                return False

        if (index < digital_len - 3):
            string_4_digit = string_3_digit + digits[index + 3]
            if (not is_prime(string_4_digit)):
                return False
        if (index < digital_len - 4):
            string_5_digit = string_4_digit + digits[index + 4]
            if (not is_prime(string_5_digit)):
                return False
    return True


#
# Complete the primeDigitSums function below.
#
def primeDigitSums(n):
    search_until_number = n * "9"
    return check_valid_numbers(search_until_number, n)


import math


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

