#!/usr/bin/python3
#we create the list
fruit_data = ["apple",    "banana",  "cherry", "orange"  ,  "pear"]
#create cleaner list
clean_fruit_data = [item.strip().split(",") for item in fruit_data]
#and print
print(fruit_data)
print(clean_fruit_data)
print(clean_fruit_data[0])
print(clean_fruit_data[1])
print(clean_fruit_data[0:2])
print(clean_fruit_data[-1])
print(clean_fruit_data[-2])	
