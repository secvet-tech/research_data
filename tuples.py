#!/usr/bin/python3
import datetime
#we create our tuple
names_members = ("Elio", "Joss", "kentho")
#we copy the first tuple and add a datetime
dated_names_members = names_members + (datetime.datetime.now().isoformat(),)
#we print the len of the tuples
print(len(names_members))
print(len(dated_names_members))
#and print the copy tuple
print(dated_names_members)
