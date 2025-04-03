import csv, json

#CSV
with open("Chapter_5/Test.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["1", "John", "21"])
    writer.writerow(["2", "Cap", "20"])

with open("Chapter_5/Test.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        for col in row:
            print(col, end=" ")
        print()

#JSON
data = [
    {"ID": 1, "Name": "John", "Age": 21},
    {"ID": 2, "Name": "Cap", "Age": 20}
]

with open("Chapter_5/Test.json", "w") as file:
    json.dump(data, file) #Object to JSON

with open("Chapter_5/Test.json", "r") as file:
    data = json.load(file) #JSON to Object
    print(data)