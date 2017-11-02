import random


def luhn_digit(n):
    n = 2 * n
    if (n > 9):
        return n - 9
    else:
        return 9


def luhn_checksum(n):
    l = len(n)
    sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i + 1) % 2 == 0:
                sum += int(n[i])
            else:
                sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i + 1) % 2 == 0:
                sum += luhn_digit(int(n[i]))
            else:
                sum += int(n[i])
    return sum % 10


def generate(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n


def is_luhn_valid(n):
    return luhn_checksum(n) == 0


def luhn_checksum_wikipedia(card_number):
    def digit_of(n):
        return [int(d) for d in str(n)]
    digits = digit_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digit_of(d * 2))  # 我觉得 "d * 2" 前面不需要加 digit_of
    return checksum % 10


def is_luhn_valid_wikipedia(card_number ):
    return luhn_checksum_wikipedia(card_number) == 0


def check(pref, l, num):
    if len(num) != l:
        return False
    preflen = len(pref)
    if num[:preflen] != pref:
        return False
    return is_luhn_valid(num)

pref = "372542"

for i in range(10000):
    n = generate(pref, 15)
    assert check(pref, 15, n)

# N = 100000
# valid = 0
# for i in range(N):
#     n = str(random.randint(0, 1000000000000000)).zfill(15)  # convert to a zero-fill string
#     if check(pref, 15, n):
#         valid += 1
# print(str(valid) + " valid out of " + str(N))
