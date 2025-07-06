import json

print("\n____datur ishga tushirish uchun 1 ni bosing_____\n")

def run():
    data = {
        "name": "Ali",
        "age": 20,
        "grade": "A"
    }
    with open("student.json", "w") as file:
        json.dump(data, file, indent=4)
    return 'json file yozildi: studentttt.json'

tanlov = input('1 ni bosing: ')

if tanlov == '1':
    print(run())
