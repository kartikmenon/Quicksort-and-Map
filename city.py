# Defining City Class
# May 2013
# Kartikeya Menon


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
    
