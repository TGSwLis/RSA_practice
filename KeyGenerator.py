# prime1, prime2 should be random number
# e should be random number as well
import random
import math


def gcd(a, b):

    if a < b:
        c = a
        a = b
        b = c

    while b != 0:
        a, b = b, a % b

    return a


def egcd(a, b):

    s0, s1 = 1, 0
    t0, t1 = 0, 1

    if b == 0:
        return 1, 0, a
    else:
        while b != 0:
            q = a // b
            a, b = b, a - q * b
            s0, s1 = s1, s0 - q * s1
            t0, t1 = t1, t0 - q * t1

    return s0, t0, a


def fastMod(base, exp, mod):
    # We don't consider the cases that exp < 0 or exp is fraction
    if exp == 0:
        return 1
    elif exp == 1:
        return base % mod

    # Convert the exponent part into base-2
    baseTwoExp = []
    while exp > 0:
        baseTwoExp.append(exp % 2)
        exp = exp // 2

    index = len(baseTwoExp) - 1
    result = base % mod
    while index >= 0:
        if index == len(baseTwoExp) - 1:
            index = index - 1
            continue
        else:
            if baseTwoExp[index] == 0:
                result = (result * result) % mod
                index = index - 1
            else:
                result = (result * result) % mod
                result = (result * (base % mod)) % mod
                index = index - 1

    return result


# def phi(n):
#     count = 0
#     for k in range(1, n + 1):
#         if gcd(k, n) == 1:
#             count += 1
#     return count


# # AKS primality test (TODO)
# # Give up = =
# def isPrime(n):
#     # part 1
#     for b in range(2, int(math.log2(n) + 1)):
#         a = n ** (1 / b)
#         if a == math.floor(a):
#             return False

#     # part 2
#     nextR = True
#     r = 1
#     while nextR == True:
#         r = r + 1
#         nextR = False
#         k = 1
#         while k <= math.log2(n) and not nextR:
#             nextR = fastMod(n, k, r) == 1 or fastMod(n, k, r) == 0
#             k = k + 1

#     # part 3
#     for a in range(2, r + 1):
#         if 1 < gcd(a, n) and gcd(a, n) < n:
#             return False

#     # part 4
#     if n < 5690034:
#         if n <= r:
#             return True
#         else:
#             return False

#     # part 5
#     for a in range(1, math.floor(phi(r) * math.log2(n)) + 1):
#         if False:
#             pass

#     return True


# Using RSA algorithm to encrypt the text
# 1. Randomly pick two appropriate prime number
# Prime numbers need to be big enough, and the difference between them cannot be too huge
# e.g. 757, 787, 2207, 99194853094755497, 3314192745739
prime1 = 712910974150897
prime2 = 863113070614841
# primeFlag = True
# gapFlag = False

# while not primeFlag or gapFlag:
#     prime1 = random.randint(2, 1000000)
#     prime2 = random.randint(2, 1000000)
#     primeFlag = isPrime(prime1) and isPrime(prime2)
#     gapFlag = (prime1 / prime2 > 1000) or (prime2 / prime1 > 1000)

# 2. Compute n and phi
# note: n should be greater than the message to be encrypted
n = prime1 * prime2
phi = (prime1 - 1) * (prime2 - 1)
# print("n:", n)
# print("phi:", phi)

# 3. Choose an integer e, which should be a prime number
# e.g. 65537
e = 65537

# 4. Compute modular multiplicative inverse for private key
x, y, a = egcd(e, phi)
d = x
if d < 0:
    d = d + phi

# print("d:", d)

publicFile = open("PublicKey.txt", "w+")
publicFile.write("n: %d" % n)
publicFile.write("\ne: %d" % e)
publicFile.close()
privateFile = open("PrivateKey.txt", "w+")
privateFile.write("n: %d" % n)
privateFile.write("\nd: %d" % d)
privateFile.close()

print("Done!")
