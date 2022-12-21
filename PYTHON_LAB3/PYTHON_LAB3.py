from functools import reduce
import csv

with open("11.11.csv") as file:
	keys = file.readline()
	reader = csv.reader(file, delimiter=",")
	dataset = [x for x in reader]
keys = list(keys.split(","))

def to_dictionary(keys, values):
	dictionary = {}
	for i in range(len(keys)):
		dictionary[keys[i]] = values[i]
	return dictionary

dataset = list(map(lambda x: to_dictionary(keys, x), dataset))

ColPeople = list(map(lambda x: int(x['survived']), dataset))
ColSurvived = reduce(lambda x, y: x + y, ColPeople)
Percent = round(ColSurvived / len(ColPeople) * 100, 2)

print("Count of people:", len(ColPeople),"\nCount of survived:", (ColSurvived), "\nPercent of survived:", Percent)
#сдана
