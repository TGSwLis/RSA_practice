import math

# Implement Euclidean algorithm
def gcd(a, b):

    if a < b:
        c = a
        a = b
        b = c

    while b != 0:
        a, b = b, a % b

    return a

# Implement Extended Euclidean algorithm
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

# For big number modulo operation
def fastMod(base, exp, mod):
    # We don't consider the cases that exp < 0 or exp is fraction
    if exp == 0:
        return 1
    elif exp == 1:
        return base % mod

    # Convert the exponent part into base-2 number
    baseTwoExp = []
    while exp > 0:
        baseTwoExp.append(exp % 2)
        exp = exp // 2

    index = len(baseTwoExp) - 1
    result = base % mod
    while index >= 0:
        if index == len(baseTwoExp) - 1:
            index -= 1
            continue
        else:
            if baseTwoExp[index] == 0:
                result = (result * result) % mod
                index -= 1
            else:
                result = (result * result) % mod
                result = (result * (base % mod)) % mod
                index -= 1

    return result


# Using RSA algorithm to encrypt the integer
# 1. Randomly pick two appropriate prime number
# Prime numbers need to be big enough
prime1 = 712910974150897
prime2 = 863113070614841

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

# print("Done!")

# 5. Testing
originNum = 7355808
print("Original Number:", originNum)

encryptNum = fastMod(originNum, e, n)
print("Encrypted Number:", encryptNum)

decrpytNum = fastMod(encryptNum, d, n)
print("Decrpyted Number:", decrpytNum)
