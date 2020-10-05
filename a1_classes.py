"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from places import Place
from placecollection import PlaceCollection

MENU = """
L \t---- List places
A \t---- Add new place
M \t---- Mark a place as visited
Q \t---- Quit
>>> 
"""

FILENAME = "visitList.csv"

"""
def load_places(self):
    place_list = []
    inputFile = open(FILENAME, "w")
    for places in inputFile:
        parts = places.strip().split(',')
        print(places)


def save_places(self):
    self.places.append(Place)


def add_places(self, Place):
    self.places.append(Place)
"""

def main():


    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            PlaceCollection.print_place(PlaceCollection)
        elif choice == "A":
            PlaceCollection.add_places(PlaceCollection)
        elif choice == "M":
            print("Derp")
#            visit_place(Place, PlaceCollection)
        else:
            print("Invalid menu choice")
        choice = input(MENU).upper()
    PlaceCollection.save_places(PlaceCollection)

main()