import json

with open("students.json", "r") as f1:
    students = json.load(f1)
studint = len(students)
print(f"umumiy: {studint}")