n=int(input("introdu nr: "))
i = 0
while n != 0:
    c = n % 10
    i = i * 10 + c
    n = n // 10
print("numaru inversat este: ", i)