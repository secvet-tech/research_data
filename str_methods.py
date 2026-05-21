#!/usr/bin/python3
#we start with data
inputs = ["jdoe123", "Alice", "1990", "   ", "password!"]
#we create our dict to hold users
users = {}
#we loop through our data
for i, val in enumerate(inputs, 1):
    users[f"user{i}"] = val
#we print the users
print(users["user1"])
print(users["user2"])
