person = {
    "name": {
        "last_name": "Müller",
    },
    "hobbies": {
        "Skifahren",
        "Mathe",
        "Mathe",
    },
    "age": 23,
}
print(person)
#print(person["name"]["first_name"])
a = "not exist"
print(person.get("name").get("first_name", a))