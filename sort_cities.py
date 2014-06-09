from quicksort import *
from city import City
from string import lower

# Defining various comparison functions.

# Defining one to compare names. It takes two city object references as two parameters
# and sets them as variable names, sets them to lower case for even comparison, and returns
# the result of comparing them.

def compare_names(city1, city2):
    name1 = city1.name
    name2 = city2.name
    lower(name1)
    lower(name2)
    return name1 <= name2

# Defining one to compare populations, turning most populated to least populated.

def compare_populations(city1, city2):
    population1 = city1.population
    population2 = city2.population
    return population1 >= population2

# Same thing as compare_names, but with different instance variable.

def compare_latitudes(city1, city2):
    latitude1 = city1.latitude
    latitude2 = city2.latitude
    return latitude1 <= latitude2
    
# Opening all the files necessary.
file1 = "world_cities.txt"
world_cities = open(file1, "r")

file2 = "cities_alpha.txt"
cities_alpha = open(file2, "w")

file3 = "cities_population.txt"
cities_population = open(file3, "w")

file4 = "cities_latitude.txt"
cities_latitude = open(file4, "w")

# Initializing all the relevant lists as empty.
world_alpha = []
world_population = []
world_latitude = []



# Looping over all lines in the text file.
for line in world_cities:
    
    # Stripping white space from end of each line and creating a list from text around commas.
    line = line.strip()
    city_list = line.split(",")
    
    # Making a new city object for every new line. 
    new_city = City(city_list[0], city_list[1], city_list[2], int(city_list[3]), float(city_list[4]), float(city_list[5]))

    # Appending each new city object reference to the empty list. 
    world_alpha.append(new_city)
    world_population.append(new_city)
    world_latitude.append(new_city)
 
# Sorting each list with the relevant comparison function.   
sort(world_alpha, compare_names)

sort(world_population, compare_populations)

sort(world_latitude, compare_latitudes)

# Loop for writing files. Puts each city in order with a carriage return.
for i in range(len(world_alpha)):

    cities_alpha.write(str(world_alpha[i]) + "\n")
    
    cities_population.write(str(world_population[i]) + "\n")
    
    cities_latitude.write(str(world_latitude[i]) + "\n")



# Closing all .txt files.
world_cities.close()
cities_alpha.close()
cities_population.close()
cities_latitude.close()



