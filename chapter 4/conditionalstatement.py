#conditional statement

marks = int(input("Enter your marks: "))
age = int(input("Enter your age: ")) 

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")


if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

    
