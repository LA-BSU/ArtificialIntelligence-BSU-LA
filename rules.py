

import csv
import random
from collections import Counter

columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
classes = ["unacc" "acc", "good", "vgood"]

with open("car.data") as carFile:
    carRows = [dict(zip(columns, row)) for row in csv.reader(carFile) if row]



rules = [ ({"safety": "low"}, "unacc"), #576/576
    ({"persons": "2"}, "unacc"), #576/576
    ({"buying": "vhigh", "maint": "vhigh"}, "unacc"), #108/108
    ({"buying": "vhigh", "maint": "high"}, "unacc"), #108/108
    ({"buying": "high", "maint": "vhigh"}, "unacc"), #108/108

    ({"safety": "high", "lug_boot": "big", "buying": "med", "maint": "med"}, "vgood"), #8/12
    ({"safety": "high", "lug_boot": "big", "buying": "low"}, "vgood"), #24/48
         
   ##CANT find any "good" rules=

    ({"safety": "high", "persons": "4"}, "acc"), #108/192
    ({"safety": "high", "persons": "more"}, "acc"), #96/192

         
         

         
]

def classify(car):
    for conditions, answer in rules:
        if all(car[a] == v for a, v in conditions.items()):
            return answer
    return "unacc"

accuracy = sum(classify(car) == car["class"] for car in carRows) / len(carRows)
print(f"currnent total rule accuracy: {accuracy:.2f}")



# 1 
group = [car for car in carRows if car["safety"] == "low"]
print(len(group), Counter(car["class"] for car in group))
#2

group = [car for car in carRows if car["persons"] == "2"]
print(len(group), Counter(car["class"] for car in group))
#3
group = [car for car in carRows if car["buying"] == "vhigh" and car["maint"] == "vhigh"]
print(len(group), Counter(car["class"] for car in group))

#4
group = [car for car in carRows if car["buying"] == "vhigh" and car["maint"] == "high"]
print(len(group), Counter(car["class"] for car in group))


#5
group = [car for car in carRows if car["buying"] == "high" and car["maint"] == "vhigh"]
print(len(group), Counter(car["class"] for car in group))

#6
group = [car for car in carRows if car["safety"] == "high" and car["lug_boot"] == "big" and car["buying"] == "med" and car["maint"] == "med"]
print(len(group), Counter(car["class"] for car in group))

# 7
group = [car for car in carRows if car["safety"] == "high" and car["lug_boot"] == "big" and car["buying"] == "low"]
print(len(group), Counter(car["class"] for car in group))


# 8

group = [car for car in carRows if car["safety"] == "high" and car["persons"] == "4"]
print(len(group), Counter(car["class"] for car in group))

# 9
group = [car for car in carRows if car["safety"] == "high" and car["persons"] == "more"]
print(len(group), Counter(car["class"] for car in group))

