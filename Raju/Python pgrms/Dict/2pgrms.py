from collections import defaultdict

d = defaultdict(int)



fruits = ["Apple", "Orange", "Banana", "Orange","Apple", "Banana","Apple",
         "Peach", "Apple", "Banana"]

for fruit in fruits:
    d[fruit] += 1
    



print(d)




