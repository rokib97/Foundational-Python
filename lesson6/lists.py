# declare list 

users = ["Sara","Rokib","sabrina","ambrin","sriti"] 
numbers = [10, 20, 69, 99]
data = ["rokib", 99, True, False]
empty_list = []

# ==========exist(READ) or not========== 
# print("Rokib".lower() in users)
# print([] in empty_list)


#========== accessing(READ) list items ==========
# print(numbers.index(69))
# print(numbers[-1])
# print(numbers[0:])
# print(numbers[0:2])
# print(numbers[-2:4])
# print(len(data))

# ==========adding(CREATE) itesm to list ==========
# numbers.append(120)
# print(numbers)

#========== joining(CREATE) two list ==========
# numbers += [12,25,30]
# numbers.extend([1,2,3])
# numbers.extend(data)

#  ====== insert(CREATE) item at specefic position ==========
# numbers.insert(0,1000)
# numbers[2:2] = [100, 200]
# my_list = ["element"] + numbers


#========== replace(UPDATE) value in the list ==========
# numbers[1:2] = [15,10]
# numbers[2:4] = [15,10]



#========== delete(DELETE) item value from the list ==========
# print(numbers)
# numbers.remove(69)
# print(numbers.pop())
# del numbers[0] 
# del numbers # delete entire list 
# numbers.clear() #returns empty []



#========== sorting list ==========
users.sort(key=str.lower) #to count the lowercase also for sorting
# numbers.sort()
# data.sort()
# print(users)

nums = [10,4,69,22,15,150,2]
# nums.reverse()
# nums.sort(reverse=True)
# print(nums)

# keeping the orginal list and then make new sorted list 
# new_sorted = sorted(nums, reverse=True)
# print(nums)
# print(new_sorted)
# print(nums)

# anotherway  make copy of an list
my_first_copy = nums.copy()
# print("First Copy: ", my_first_copy)
my_second_copy = nums[:]
# print("Second Copy: ", my_first_copy)
my_third_copy = list(nums)
# print("Third Copy: ", my_third_copy)

# now make sort 
my_second_copy.sort()
# print("Original List: ", nums)
# print("Sorted List: ", my_second_copy)

# print(type(nums))

# list constructor 
my_list = list([1,"Neil",True])
# print(my_list)



# Tuples 
# create tuple 
my_tuple = (10,20,30)
# print(my_tuple)
another_tuple = tuple((10,20,30,40,40,40))
# print(another_tuple)
# print(type(another_tuple))
# print(isinstance(another_tuple,tuple))


# update tuple using list [it creates new tuple]

new_list = list(another_tuple)
new_list.append("rokib")
new_tuple = tuple(new_list)
# print(another_tuple,  new_tuple)

(first, *second, rest) = new_tuple
# (first, second, *rest) = new_tuple
# print(first)
# print(second)
# print(rest)

# check method available 
print(new_tuple.count(40))