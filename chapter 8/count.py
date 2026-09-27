import os

try:
    with open("ntext.txt","r") as f:
        data = f.readlines()
        print(len(data))
except:
    print("sorrry")



