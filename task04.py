import json

with open("output/student04.json", "w") as f1:
    ism = input("ismingizni kiritng: ")
    familiya = input("familiyangizni kiritng: ")
    yosh = input("yoshingizni kiritng: ")

    data = [
        {"name": ism, "surname": familiya, "age": yosh}
    ]

    json.dump(data, f1, indent=4)

    print("Kiritilgan ma'lumotlar:")
    print(json.dumps(data, indent=4))
    
