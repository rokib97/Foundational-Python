# key value pair 

# create dict 

my_dict = {
    "name":"rokib",
    "age":21
}

my_dict2 = {
    "name":"sriti",
    "isCute":True
}
# print(my_dict)
# print(my_dict2)
# print(type(my_dict2))
# print(len(my_dict))

# access items in dict 
# print(my_dict["name"])
# print(my_dict2.get("name"))

# list all keys and value
# print(my_dict.keys())
# print(my_dict2.values())

# list of key /value pairs as tuple 
result = my_dict.items()
# print(result)

# verify a key exist in a dick 
# print("name" in my_dict)

# change values in dict
my_dict["name"] = "my_name"
my_dict.update({"age":69}) #update existing data
my_dict.update({"is_married":False}) #insert new data data
# print(my_dict)


# remove items 
# print(my_dict.pop("name")) #resturn the value
# print(my_dict)

my_dict['is_married'] = False
# print(my_dict)
# print(my_dict.popitem()) #return a tuple which was last added
# print(my_dict)

# Delet and clear item 
# print(my_dict2)
# del my_dict2["name"] #delete specific items
# print(my_dict2)

# empty the dict 
my_dict2.clear() #return {}
# print(my_dict2)
del my_dict2 #completely delete the dict


# copy dict 
my_dict2 = my_dict #create e reference
# print(my_dict)
# print(my_dict2)

# Bad Copy !
my_dict2["new_value"] = "I am new Value" # assigned to both dict beacuse its the same reference
# print(my_dict)

# good way to copy

new_dict = my_dict.copy()
new_dict["greet"] = "Hello"
# print(new_dict)
# print(my_dict)

# or use the constructor fucntion 
my_test_dict = dict(name="sunny", relation = "Bro") 
# or 
my_dict_three = dict(my_dict)
my_dict_three["new_add_value"] = "i am newly added"
# print(my_dict)
# print(my_dict_three)

# nested dict 
member_one = {
    "Name": "Samsung",
    "Price":540000
}
member_two = {
    "Name": "Iphone",
    "Price":1540000
}


phones = {
    "Gorib" : member_one,
    "Bruluks": member_two
}
# print(phones["Gorib"]["Name"])
# print(phones.get("Gorib").get("Name"))



# Sets 

nums = {1,2,3,4}
nums2 = set((1,2,3,4))
# print(nums)
# print(nums2)
# print(type(nums2))
# print(len(nums))

# no duplicate allowed in set 

nums= {5,2,3,4,4}
# print(nums) # {1,2,3,4} => 4 allowed once  and its comes with order

# True means 1, False means 0 

# print({False, 1, 2, 3, True, 4 , 5, False, 0})


# check if a value exits in set 
# print(True == 1) 
# print(2 in nums)

# You can not use indexing nad key *********

# Adding / Updating Set 

nums.add(121)
# print(nums)

# add elements from one set to another 

more_nums = {5, 7, 9, 7}
nums.update(more_nums)
# print(nums)

# Merge two sets to create new set 
one = {1, 2,3}
two = {5, 6,7}
new_set = one.union(two)
# print(new_set)

# More use ful method for sets 

# keep only duplicates 
one = {1, 2,3}
two = {5,3,2,6,7}
# one.intersection_update(two) # not create new but returns inside one
# print(one)

# keep everything except the duplicates 
one = {1, 2,3}
two = {5,3,2,6,7}
one.symmetric_difference_update(two) 
print(one)
