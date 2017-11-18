def isDecin(num):
    inc = False
    dec = False 
    r_digit = num % 10
    num = num // 10
    while num > 0:
        l_digit = num % 10
        if l_digit < r_digit:
            inc = True
        elif l_digit > r_digit:
            dec = True
        r_digit = l_digit
        num = num // 10
        if inc and dec:
            return True
    return False

count = 0
i = 99
while count < 0.99 * i:
    i += 1
    if isDecin(i):
        count += 1
print i