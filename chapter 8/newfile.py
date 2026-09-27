with open("newtext.txt","r")  as f:
    data0 = f.readline()
    data1 = f.readline()
    data2 = f.readline() 
    data4 = f.read()
    print(data0,data1,data2,data4)