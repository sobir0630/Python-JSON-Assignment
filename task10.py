import json

with open("students.json", "r") as f1:
    data = json.load(f1)

# Yosh bo'yicha tartiblash
sorted_students = sorted(data, key=lambda x: x['age'], reverse=False)

# Natijani chiqarish
for data in sorted_students:
    print(f"Ismi: {data['name']}, Yoshi: {data['age']}")