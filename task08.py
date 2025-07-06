import json

with open("students.json", "r") as f1:
    students = json.load(f1)

max_age = max(studint['age'] for studint in students)
print(f"eng katta yosh: {max_age}")
