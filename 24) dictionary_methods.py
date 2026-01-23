#create a variable and assign it the following dictionary:

#{"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
#make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

#print the length of the dictionary.

#use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.

#print all of the values from the dictionary using the .values() method.

#use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.

#use the .get() method to check the dictionary for the key

#"Promise of the Real"
#and create a message that will print if the key is not found in the dictionary.

sfg = {"Queen": "Bohemian Rhapsody", 
       "Bee Gees": "Stayin' Alive", 
       "U2": "One", 
       "Michael Jackson": "Billie Jean", 
       "The Beatles": "Hey Jude", 
       "Bob Dylan": "Like A Rolling Stone"
       }

print(len(sfg))

for artist in sfg.keys():
    print(artist)
    
print(sfg.values())

for key, value in sfg.items():
    print(key, value)

print(sfg.get("Promise of the Real", "Promise of the Real is not found in the dictionary."))
