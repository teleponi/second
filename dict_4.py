population = {
    'Berlin': 3748148,
    'Hamburg': 1822445,
    'München': 1471508,
    'Cologne': 1085664,
    'Frankfurt': 753056
}
deutschland = {
    "berlin": {
        "neukölln": 3,
        "kreuzberg": 4
    }
}
print(deutschland)
deutschland["berlin"].update({"kreuzberg": 14})
print(deutschland)

population.update({"Berlin":20000})
population.update({"Moskau":120000, "Dortmund": 50000})
b = population.get("Berlin")
population["Frankfurt"] = 0
berlin = population.pop("Berlin")
print("berlin:", berlin)
del population["Moskau"]

print(population)



for city, bewohner in population.items():
    # print(city, bewohner)
    pass

pairs = population.items()
#print(pairs)