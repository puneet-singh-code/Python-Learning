# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# fruits[1] = "orange"
# print(len(fruits))



# list = [i for i in range(1,11)]
# print(list)
# print(list[0:3])
# print(list[-3:])



# numbers = [5, 2, 9, 1, 7]
# numbers.sort()
# print(numbers)
# numbers.append(10)
# print(numbers)
# numbers.remove(2)
# print(numbers)



# names = ["Alice", "Bob", "Charlie"]
# names.insert(1,"David")
# print(names)



# coordinates = (10, 20)
# print(coordinates[0])
# print(coordinates[1])
# # coordinates[0] = 50
# corlist = list(coordinates)
# corlist[0] = 50
# coordinates = tuple(corlist)
# print(coordinates)



# my_set = {1, 2, 3, 3, 4}
# print(my_set)
# my_set.add(5)
# my_set.remove(2)
# print(my_set)



# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))



# student = {"name": "John", "age": 20, "grade": "A"}
# print(student["name"])
# student["grade"] = "A+"
# print(student)
# student["city"] = "Delhi"
# print(student)



# mydict = {
#     "Harry": 9563248570,
#     "John Doe": 1236547890,
#     "Donald Trump": 7539514602
# }
# print(mydict.keys())
# print(mydict.values())

# for key, value in mydict.items():
#     print(key,value)



# def remove_duplicates(num):
#     return list(set(num))
# num = (1,1,2,2,3,3,4,5,6,6,7,7)
# print("original_num",num)
# print("without_duplicate",remove_duplicates(num))





# def most_expensive_product(products):
#     return max(products.items(), key=lambda x: x[1])



# products = {
#     "Laptop": 80000,
#     "Phone": 60000,
#     "Tablet": 35000,
#     "Monitor": 15000
# }
# product,price = most_expensive_product(products)
# print(f"Most expensive product is {product} with price of {price}")



# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}

# d1.update(d2)
# print(d1)