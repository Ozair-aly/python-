students = {
    "name": "ozair",
    "city": "hyderabad",
    "age": 21,
    "roll number": 18,
    "name": "ali"
}
print(type(students))
print(students)
print(students["name"])
print(students["age"])
print(students["city"])
#updating a dict
students["roll number"] = 25
#adding an item
students["salary"] = "80 lpa"
print(students)
students.pop("age")
print(students.keys())
print(students.values())
print(students.items())
print(students.get("salary"))