# 1. Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]

# 2. Access the first list from the list of lists in step 1 by index then print it.

# 3.Access the 14 from the list in step 1 then print it.

#4. Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]

#5. Use a negative integer to access "chair" from the variable in step 4 by index then print it.

#6. Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.

#7. Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]
#8. Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.

#9. Print the slice [8.76, 6.54] from the variable you created in step 7.

#10. Print the slice [0.98, 8.76] from the variable you created in step 7.

list = [[0,2],[4,6],[8,10],[12,14]] #!

print(list[0]) #@

print(list[3][1]) #3

list2 = ["chair", "table", "desk", "lamp", "bed"] #4

print(list2[-5]) #5

print("Most people own at least " + str(list[0][1]) + " " + list2[0] + "s.") #6

list3 = [0.98,8.76,6.54,4.32] #7

print(list3[1:4]) #8

print(list3[1:3]) #9

print(list3[:2]) #10
