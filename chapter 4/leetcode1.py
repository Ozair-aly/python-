s = input("Enter a string sentence:")
words = s.split()
if words:
    print(len(words[-1]))
else:
    print(len(s))