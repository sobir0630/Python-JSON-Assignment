import json

with open("output/student03.json", "w") as f1:
    
    data = [
        {"name": "Shahzoda", "surname": "Nazarova", "age": 22}
    ]
    
    json.dump(data, f1, indent=4)
    
