l = []
with open("a.txt", "rb") as f:
    result = f.read()
    words = result.split()
    for i in words:
        l.append(i)

x = []
with open("c.txt", "rb") as f:
    result = f.read()
    words = result.split()
    for i in words:
        for j in l:
            if i == j:
                l.remove(i)

print l

#flag{h1dden_7cp^C5g_lol}
