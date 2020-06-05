en_de = {
    "house" : "Haus",
    "cat": "Katze",
    "black": "schwarz",
}
print(en_de)

# auf Dictionary zugreifen per Schlüssel
print(en_de["house"])

# Fehler: Schlüssel existiert nicht!
# print(en_de["dog"])

if "dog" in en_de:
    print("der Schlüssel Dog ist im Dict enthalten")

'''
b = [1,2,2]
a = ["a","b","b"]

d = {"b": 1, "b": 3}
s = {"a", "a"}
print(s)
print(d)

z = zip(a,b)
for x in z:
    print(x)
p = dict(z)
print(p)
'''