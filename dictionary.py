numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)
print(type(numbers))
print(numbers[3])

people = {
    1: {
        "name": "John",
        "age": 20,
        "city": "New York"
    },
    2: {
        "name": "Jane",
        "age": 22,
        "city": "London"
    }
}
print(people[1]["name"])
print(people[2]["age"])

# การอ่านคีย์ทั้งหมด
print(numbers.keys())
print(numbers.values())
print(people.keys())
print(people.values())
print(people[1].values())

# loop อ่าน
for key, value in numbers.items():
    print(key, value)

    print("-------------------")
row = 1
for key, value in people.items():
    print('row', row)
    for k, v in value.items():
        print(k, v)
print("-------------------")
row += 1
