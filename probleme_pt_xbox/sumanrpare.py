n = int(input("introdu nr:"))
s = 0
if n < 0:
    n = -n
while n != 0:
    c = n % 10
    if c % 2 == 0:
        s = s + c
    n = n // 10
print("Suma cifrelor pare este:", s)
