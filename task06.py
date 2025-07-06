import json

with open("students.json", "r") as f1:
    names = json.load(f1)
    
with open("students.csv", "w") as f2:    
    for name in names:
        f2.write(f"maluotlar: {name}\n")
