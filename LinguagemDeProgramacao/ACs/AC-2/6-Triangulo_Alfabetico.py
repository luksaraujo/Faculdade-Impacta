import string
a = list(string.ascii_uppercase)
n = int(input())
for i in range(n):
    print(a[i] * (i + 1))
