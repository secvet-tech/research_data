#!/usr/bin/python3
#we create our set
classic_rock = {"AC/DC", "Black Sabbath", "Fleetwood Mac"}
rap = {"Run The Jewel", "T.I.", "Aesop Rock"}
#we bind the 2 with union
some_artists = classic_rock.union(rap)
#we print
print(some_artists)
