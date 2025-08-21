#WORKING WITH LOOPS(FOR LOOPS AND WHILE LOOPS)

#A WHILE LOOP THAT PRINTS ODD NUMBERS
#i = 1
#while i < 100:
#    print(i)
#    if i == 49:
#        print("Halfway there!")
#    i += 2

#A FOR LOOP THAT LOOPS OVER A LIST
#my_list = ['Tim','Josh','Sly','John','Jane','Charles','Dawn','Don','Daniel']

#for x in my_list:
#    if x == 'Jane':
#        print("Found Jane!")
#        continue
#    print(x)

#FOR LOOP USING RANGE FUNCTION TO PRINT EVEN NUMBERS
#for j in range(0,100,2):
#    if j == 50:
#        print("Halfway there!")
#    print(j)

#NESTED LOOPS
#adj = ["red", "big", "tasty", "sweet","small"]
#fruits = ["apple", "banana", "cherry"]

#for x in adj:
#  for y in fruits:
#    print(x,y)

#2D LISTS
my_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for sublist in my_list:
    for item in sublist:
        print(item)