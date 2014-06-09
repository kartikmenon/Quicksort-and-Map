# Reading in the file world_cities.txt, creating all city bodies and writing out to cities_out.txt
# May 2013
# Kartikeya Menon


from city import City
from cs1lib import *

# Opening file and reading it

file1 = "world_cities.txt"
world_cities = open(file1, "r")

# Writing the new file. cities_out.txt is initially just a blank textedit file.

file2 = "cities_out.txt"
cities_out = open(file2, "w")

# Initializing the list of City object references to the empty list.
world_list = []

# Looping over all lines in the text file.
for line in world_cities:
    
    # Stripping white space from end of each line and creating a list from text around commas.
    line = line.strip()
    city_list = line.split(",")
    
    # Making a new city object for every new line. 
    new_city = City(city_list[0], city_list[1], city_list[2], int(city_list[3]), float(city_list[4]), float(city_list[5]))

    # Appending each new city object reference to the empty list. 
    world_list.append(new_city)
    
for i in range(len(world_list)):
    # Writing the new list.
    cities_out.write(str(world_list[i]) + "\n")

# Closing the open files.
world_cities.close()
cities_out.close()


    
