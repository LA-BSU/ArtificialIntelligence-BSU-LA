

import csv

from collections import Counter

columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]

with open("car.data") as carFile:
    carRows = [dict(zip(columns, row)) for row in csv.reader(carFile) if row]


rules = [ ({"safety": "low"}, "unacc"),
         ({"persons": "2"}, "unacc"),
         ({"buying": "vhigh", "maint": "vhigh"}, "unacc"),

         
]

def classify(car):
    for conditions, answer in rules:
        if all(car[a] == v for a, v in conditions.items()):
            return answer
    return "unacc"

accuracy = sum(classify(car) == car["class"] for car in carRows) / len(carRows)
print(f"3-rule accuracy: {accuracy:.2f}")



group = [car for car in carRows if car["buying"] == "vhigh" and car["maint"] == "vhigh"]
print(len(group), Counter(car["class"] for car in group))


group = [car for car in carRows if car["safety"] == "low"]
print(len(group), Counter(car["class"] for car in group))

group = [car for car in carRows if car["persons"] == "2"]
print(len(group), Counter(car["class"] for car in group))

print(Counter(car["class"] for car in group))