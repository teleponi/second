gerichte = ["Pizza", "Sauerkraut", "Paella", "Hamburger", "Alfajores"]
laender = ["Italien", "Deutschland", "Spanien", "USA"]

def my_zip(a, b):
    out = []
    a = iter(a)
    b = iter(b)
    try:
        while True:
            i_a = a.__next__()
            i_b = b.__next__()
            out.append((i_a, i_b))
    except StopIteration:
        return out

zippy = my_zip(laender, gerichte)
for x in zippy:
    print("-", x)

d = dict(zip(laender, gerichte))
#d = dict(zippy)
print(d)
'''
for x in zippy:
    print("+", x)

for x in "Test":
    print(x)
'''

