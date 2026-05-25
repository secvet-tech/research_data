#!/usr/bin/python3
import datetime
names_members = ("Elio", "Joss", "kentho")
newest_members = ("Al", "Ed")
#then we make 2 into 1
all_members = names_members + newest_members
#we print
print(all_members)
#next we slice and add datetime
og_members = names_members + (datetime.datetime.now().isoformat(),)
#print
print(og_members)
#next extract author
author_tuple = names_members[2]
print(author_tuple)
