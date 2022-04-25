# string concatenation (how to put strings together)
# we want to create a string that say "subcribe to _____"

youtuber = "Sipho M" # string variable

#a few ways to do this
print("subcribe to"  + youtuber)
print("subscribeto {}".format(youtuber))
print (f"subcribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input ("Verb: ")
famous_person = input("Famous Person:  ")

madlib = f"Computer Programming is so {adj}! it makes me so excited all the time because i love to{verb1}. Stay hydrated and  {verb2} like you are {famous_person}!"

print (madlib)
