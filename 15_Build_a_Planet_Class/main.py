class Planet:
    def __init__(self, name, planet_type, star):
        # Input validation
        if not (isinstance(name, str) and isinstance(planet_type, str) and isinstance(star, str)):
            raise TypeError('name, planet type, and star must be strings')
        if not (name and planet_type and star):
            raise ValueError('name, planet_type, and star must be non-empty strings')
        # Initializing attributes
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'    

# Instances
planet_1 = Planet('Earth', 'Life', 'Sun')
planet_2 = Planet('Venus', 'Nearby', 'Sun')
planet_3 = Planet('Mars', 'Red', 'Sun')

# Print the objects
print(planet_1)
print(planet_2)
print(planet_3)

# Print the output of orbit() on objects
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
