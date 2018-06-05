a = []
n = int(input("enter the number of element you want to enter: "))
for i in range(n):
    s = int(input("enter the number: "))
    a.append(s)
a.sort(reverse=True)
print(a)