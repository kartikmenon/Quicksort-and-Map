

from city import City
from sort_cities import *
from quicksort import *
from cs1lib import *

from cs1lib import *

# Some variables.

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360

image = load_image("world.png")

PIXEL_CONVERSION = 2 # 2 pixels per degree

LATITUDE_SHIFT = 180 # Degrees
LONGITUDE_SHIFT = 360 # Degrees

SQUARE_DIMENSION = 8
    
def draw_cities():
    draw_image(image, 0, 0) # Drawing the background image
    
    # Looping over 0 - 49 of the first highest populations in the list of sorted populations.
    for i in range(50):
        
        # Converting latitude and longitude degree measure to pixels and shifting
        latitude = world_population[i].latitude * PIXEL_CONVERSION + LATITUDE_SHIFT
        longitude = world_population[i].longitude * PIXEL_CONVERSION + LONGITUDE_SHIFT
        
        # Some aesthetics.
        set_fill_color(1, 0, 0)
        disable_stroke()
        
        # Drawing each rectangle in the right place.
        draw_rectangle(longitude, latitude, SQUARE_DIMENSION, SQUARE_DIMENSION)
        
        # Napping and forcing draw.
        sleep(1)
        request_redraw()
        
# Flipped_y = True
        
start_graphics(draw_cities, "The World", WINDOW_WIDTH, WINDOW_HEIGHT, True)




