#paste these 2 dictionaries into your file

#internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
#another_one = {"shroud": "Twitch"}
#use .update() to add the contents of another_one to internet_celebrities.

#create a variable and assign it a copy of internet_celebrities.

#use the .clear() method to get rid of the contents of internet celebrities.

#print internet_celebrities.

#print the variable you created in step 3.

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
copy_internet_celebrities = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(copy_internet_celebrities)

