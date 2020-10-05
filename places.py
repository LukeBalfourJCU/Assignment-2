"""..."""


# Create your Place class in this file
"""TO DO LIST:

Define the class attributes
Class string - Priority, Name, Country, Visited Status
Make two methods to mark the place as unvisited/visited
Make method to determine importance ( if X <=2 )

"""

class Place:
    """..."""
    def __init__(self, name, country, priority, visited):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.country = country
        self.priority = 0
        self.visited = False

    def is_important(self, priority, important):
        if priority >= 2:
            important = True

        return important

    def __str__(self):
        print("Priority: {} | {}, {}, {}").format(self.priority, self.name, self.country, self.visited)


    pass