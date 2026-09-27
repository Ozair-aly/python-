#methods in list
#list is mutable in python
#string is immutable in python

marks = [90, 100 ,95, 98]
marks1 = [20,90,50,66]
print(marks)
marks[1] = 85
print(marks)
print(marks[1:3])
print(max(marks))
print(min(marks))
print(len(marks))
marks.append(99)
print(marks)
marks.insert(4,78)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)
marks.pop(5)
print(marks)
list1 = marks + marks1
list1.sort()
print(list1)