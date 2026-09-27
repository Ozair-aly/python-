class laptop:
    Brand = "default"
    RAM = "8gb"
    price = "1 lakh"

laptop1 = laptop()
laptop1.Brand = "macbook"
laptop1.price = "2 lakh"


laptop2 = laptop()
laptop2.Brand = "lenovo"

laptop2.RAM = "16gb"

print(laptop1.Brand,laptop1.price,laptop1.RAM)
print(laptop2.Brand,laptop2.price,laptop2.RAM)