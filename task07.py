import json

with open("students.json", "r") as f1:
    students = json.load(f1)

total_age = sum(studint['age'] for studint in students)
assigin = total_age / len(students)


print(f"urtacha yosh: {assigin}")
