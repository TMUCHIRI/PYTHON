country_file = open('countries.txt', 'r')
#print(country_file.readable()) # Check if the file is readable

#print(country_file.readline()) # Read the first line
#print(country_file.readline()) # Read the second line
#print(country_file.readline()) # Read the third line
#print(country_file.readline()) # Read the fourth line
#print(country_file.readline()) # Read the fifth line

#Reading the whole file
#print(country_file.read())

#Reading the whole file as a list
#print(country_file.readlines())

#Using a loop to read contents of a file
for content in country_file.readlines():
    print(content)
country_file.close()