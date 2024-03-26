list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]
tuple1 = ("man","women","male","femal")
dict1 = {"name":"ali", "age":27, "city":"tartus"}

# restult = zip(list1,list2)
# print(restult)

for item1, item2, item3, item4 in zip(list1,list2,tuple1,dict1):
    print("list 1 item is: ", item1)
    print("list 2 item is: ", item2)
    print("tuple 1 item is: ", item3)
    print("dict 1 key => ", item4, "###" , "value =>", dict1[item4])