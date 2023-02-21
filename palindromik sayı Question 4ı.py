
# en büyük polindrom bulma

a = 999
b = 999
max = 0
while True:
    a -= 1
    if (a == 100):
        b -= 1
        a = 999
        continue
    if (b == 100):
        break
    c = a*b

    d = str(c)
    if (d == d[::-1]):
        e = int(d)

        if (e > max):
            max = e
            g = a
            l = b

        continue
    else:
        continue
print(max)
print(g)
print(l)
