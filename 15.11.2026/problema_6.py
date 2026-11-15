n=int(input(""))
a=int(input(""))
b=int(input(""))
lg=2
lgmax=0
for i in range (3, n):
    c=int(input(""))
    if c-b == b-a:
        lg=lg+1
    elif lg > lgmax:
        lgmax = lg
        lg = 2
    a = b
    b = c
print (lgmax)