import json

with open("output/student01.json", "w") as f1:
    
    data = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
]
    
    json.dump(data, f1, indent=4)
    
