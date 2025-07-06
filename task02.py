import json

with open("output/student02.json", "r") as f:
    students = json.load(f)
    
for student in students:
    print(f"ismi {student['name']} {student['age']} yosh")
