from random import randint, uniform
from cs1lib import *


# Not bothering to make separate extra credit files. All classes and functions are defined in here.


# Copying and pasting city class.
class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):
        # Defining all instance variables.
        
        self.code = country_code
        self.name = name
        self.region = region
        
        self.population = population
        self.latitude = latitude
        self.longitude = longitude
        
    def __str__(self):
        # So that City object can be printed.
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)



# Using a randomized quicksort.


# Defining a simple comparison function for integers.
def compare_func(a, b):
    return a <= b

# A function for swapping the indices of a list.
def swap(the_list, i1, i2):

    temp = the_list[i1] # Storing one list element as a temporary variable.
    
    the_list[i1] = the_list[i2]
    the_list[i2] = temp
    
    
# Partition function.

def partition(the_list, p, r, compare_func):
    
    # Setting the pivot as the last item in the list.
    pivot_index = randint(p, r)
    pivot = the_list[r]
    
    # Setting i and j
    i = p - 1
    j = p
    
    # While the index incremented over the sublist of elements smaller than the pivot.
    while j < r:
        
        # Condition 1: If j is bigger than the pivot, don't do anything.
        if compare_func(pivot, the_list[j]):
            j = j + 1
        
        # Condition 2: If j is less than the pivot, move i up, switch i and j and increment j.
        elif compare_func(the_list[j], pivot):
            i = i + 1
            swap(the_list, i, j)
            j = j + 1
    
    # Switch the pivot to the place where it's between the sublists containing > and <= elements to it.       
    swap(the_list, i + 1, r)
    
    q = i + 1
    # Return the location of the pivot.
    return q


def quicksort(the_list, p, r, compare_func):
    
    # If the first index of the list is less than the last index.
    # This effectively takes care of the base case; when p = r, the list has one item in it.
    # So nothing will happen if the list has one item in it, the list will stay the same.
    if p < r:
        
        # Get the value returned from the partition function as the position of the pivot, q.
        q = partition(the_list, p, r, compare_func)
        
        # Recurse on the two halves of the list before q and after q. 
        quicksort(the_list, p, q - 1, compare_func)
        quicksort(the_list, q + 1, r, compare_func)
    

# Sorting entire list with quick sort.

def sort(the_list, compare_func):
    # Setting p and r to the following will sort the entire list.
    quicksort(the_list, 0, len(the_list) - 1, compare_func)

# Comparison functions

# Defining one to compare populations, turning most populated to least populated.

def compare_populations(city1, city2):
    population1 = city1.population
    population2 = city2.population
    return population1 >= population2

    
# Opening all the files necessary.
file1 = "world_cities.txt"
world_cities = open(file1, "r")


file2 = "cities_population_extra.txt"
cities_populations = open(file2, "w")


world_population_extra = []



# Looping over all lines in the text file.
for line in world_cities:
    
    # Stripping white space from end of each line and creating a list from text around commas.
    line = line.strip()
    city_list = line.split(",")
    
    # Making a new city object for every new line. 
    new_city = City(city_list[0], city_list[1], city_list[2], int(city_list[3]), float(city_list[4]), float(city_list[5]))

    # Appending each new city object reference to the empty list. 

    world_population_extra.append(new_city)

sort(world_population_extra, compare_populations)



# Loop for writing files. Puts each city in order with a carriage return.
for i in range(len(world_population_extra)):
    
    cities_populations.write(str(world_population_extra[i]) + "\n")


# Closing all .txt files.
world_cities.close()

cities_populations.close()















#### UP TO HERE IS ALL PAST STUFF COPIED AND PASTED FROM REGULAR LAB ASSIGNMENT #######













# starting extra credit.

# Features:

# Some initial animation and keyboard input to get animation going.
# Flickering cities and a nicer visualization.
# If you take off the comment symbol from the triangulation function call at the bottom, it will draw a triangle
# between three cities you specify via latitude and longitude raw_input and find the center of the triangle 
# More interesting: I wrote a function that computes the distance around the curvature of the earth between any two cities. Takes into account 
# varying latitude and longitude values and returns the distance between two cities (+/- 100 miles, as the input will only take integers, so
# can't input precise decimal values). If you're interested in the math I attached an image file of my working. 


WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360

image = load_image("world.png")

PIXEL_CONVERSION = 2 # 2 pixels per degree

LATITUDE_SHIFT = 180 # Degrees
LONGITUDE_SHIFT = 360 # Degrees

SQUARE_DIMENSION = 8


def flicker(lo, la, S_D):
    disable_stroke()

    set_fill_color(1, 0, 0)
    draw_rectangle(lo, la, S_D, S_D)
    sleep(0.07)
    request_redraw()
    set_fill_color(0, 1, 0)
    draw_rectangle(lo, la, S_D, S_D)
    sleep(0.07)
    request_redraw()
    set_fill_color(1, 0, 0)
    draw_rectangle(lo, la, S_D, S_D)
    sleep(0.07)
    request_redraw()
    set_fill_color(0, 1, 0)
    draw_rectangle(lo, la, S_D, S_D)
    sleep(0.07)
    request_redraw()
    set_fill_color(1, 0, 0)
    draw_rectangle(lo, la, S_D, S_D)
    sleep(0.07)
    request_redraw()
    set_fill_color(0, 1, 0)
    draw_rectangle(lo, la, S_D, S_D)
    sleep(0.07)
    request_redraw()
    
    set_fill_color(0, 0, 1)
    draw_rectangle(lo, la, S_D, S_D)
    sleep(0.05)
    
    
    
def draw_city(lo, la, S_D):
    disable_stroke()
    
    set_fill_color(0, 0, 1)
    draw_rectangle(lo, la, S_D, S_D)

def linear_distance(lo1, la1, lo2, la2):    
    return sqrt((lo1 - lo2) ** 2 + (la1 - la2) ** 2)

    
def triangulate(lo1, la1, lo2, la2, lo3, la3):
    enable_smoothing()
    set_fill_color(0, 0.6, 0.6)
    draw_triangle(lo1, la1, lo2, la2, lo3, la3)
    
    centerx = (lo1 + lo2 + lo3) / 3
    centery = (la1 + la2 + la3) / 3
    
    set_fill_color(1, 1, 1)
    draw_circle(centerx, centery, 3)
    
    set_fill_color(1, 1, 1)
    enable_stroke()
    draw_text("Point equidistant from three cities", centerx, centery + 5)
    request_redraw()

from math import *

def spherical_distance(lo1, la1, lo2, la2):
    deg_rad = pi/180.
    
    # phi and beta represent the equatorial angle (i.e., in the xyz coordinates,
    # phi and beta are the distance from the z axis to the city in question.
    
    # theta and gamma represent the angle around the xy-plane intersecting the middle of the earth.
    # i.e., degrees to the right of the meridian.
    
    
    
    phi = (90. - la1) * deg_rad
    beta = (90. - la2) * deg_rad
    
    theta = lo1 * deg_rad
    gamma = lo2 * deg_rad

    # Distance over a sphere is the same as taking the line integral
    # over the path of the level surface of the sphere.
    # Skipping a bit of the math: (I attached a little bit of the work in photo.JPG in the lab project file
    # on the off chance that you're interested). 
    
    a = (sin(phi) * sin(beta) * cos(theta - gamma) + cos(phi) * cos(beta))
    arc = acos(a) # Arc length computed over sphere surface
    earth_radius = 3963 # miles
    
    return arc * earth_radius

    
    
def draw_cities():
    
    n = 720
    m = 0
    
    while n >= 0:
        
        draw_image(image, n, m)
        draw_text("A map of the most populous", 5, 170)
        draw_text("cities of the world", 5, 150)
        draw_text("PRESS SPACE TO BEGIN ANIMATION", 5, 130)
        n = n - 1
        
            
        sleep(0.001)
        request_redraw()
        
    
    request_redraw
    
    while not is_key_pressed(" "):
        pass
    
    
    draw_image(image, 0, 0) # Drawing the background image
    
    # Looping over 0 - 49 of the first highest populations in the list of sorted populations.
    sleep(1)
    for i in range(10):

        
        # Converting latitude and longitude degree measure to pixels and shifting
        latitude = world_population_extra[i].latitude * PIXEL_CONVERSION + LATITUDE_SHIFT
        longitude = world_population_extra[i].longitude * PIXEL_CONVERSION + LONGITUDE_SHIFT
        
        enable_stroke()
        
        set_stroke_color(1, 0.1, 0.5)
        set_font_bold()
        
        draw_text(str(world_population_extra[i].name), longitude - SQUARE_DIMENSION, latitude + SQUARE_DIMENSION)

        
        flicker(longitude, latitude, SQUARE_DIMENSION)
        # Napping and forcing draw.
        
        request_redraw()
        sleep(1)
        clear()
        
        draw_image(image, 0, 0)
        
        for j in world_population_extra[:i + 1]:
            
            latitude = j.latitude * PIXEL_CONVERSION + LATITUDE_SHIFT
            longitude = j.longitude * PIXEL_CONVERSION + LONGITUDE_SHIFT
            
            draw_city(longitude, latitude, SQUARE_DIMENSION)
            
            request_redraw()
        
    
    
# 
#     lo1 = int(raw_input("Enter longitude in integer degrees of first city: ")) * PIXEL_CONVERSION + LONGITUDE_SHIFT
#     la1 = int(raw_input("Enter latitude in integer degrees of first city: ")) * PIXEL_CONVERSION + LATITUDE_SHIFT
#     lo2 = int(raw_input("Enter longitude in integer degrees of second city: ")) * PIXEL_CONVERSION + LONGITUDE_SHIFT
#     la2 = int(raw_input("Enter latitude in integer degrees of second city: ")) * PIXEL_CONVERSION + LATITUDE_SHIFT
#     lo3 = int(raw_input("Enter longitude in integer degrees of third city: ")) * PIXEL_CONVERSION + LONGITUDE_SHIFT
#     la3 = int(raw_input("Enter latitude in integer degrees of third city: ")) * PIXEL_CONVERSION + LATITUDE_SHIFT
#             
#     
#             
#     triangulate(lo1, la1, lo2, la2, lo3, la3)
    
    

    lo1 = int(raw_input("Enter longitude in integer degrees of first city: ")) 
    la1 = int(raw_input("Enter latitude in integer degrees of first city: ")) 
    lo2 = int(raw_input("Enter longitude in integer degrees of second city: ")) 
    la2 = int(raw_input("Enter latitude in integer degrees of second city: "))
    
    d = spherical_distance(lo1, la1, lo2, la2)    
    
    print "The two cities you clicked on are " + str(d) + " miles apart."
        

# Flipped_y = True
        
start_graphics(draw_cities, "The World", WINDOW_WIDTH, WINDOW_HEIGHT, True)

    



