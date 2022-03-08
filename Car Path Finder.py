#Car Path Finder.py --- code by Aaron Thiesen
#This is a path finding solution coded to with the A* algorithm to find paths between cities in Vancouver area and the lower mainland 


import random


#make a class to hold the data each city needs
class City:

    def __init__(self, index, distance):
    
        self.index = index
        self.distance = distance


#initialize all the cities as city classes with stored data on their distance to one another
#the order of the lists is the same order their distance to one another ie: VA.distance[1] = the distance between VA and NV and BU.distance[0] = the distance between BU and VA
#the units are all in km and are rounded to nearest integer
VA = City(0, [0, 18, 11, 13, 13, 28, 18, 24, 45, 67, 99, 150, 71])
NV = City(1, [18, 0, 10, 15, 29, 31, 27, 36, 48, 70, 103, 153, 74])
WV = City(2, [11, 10, 0, 25, 24, 42, 30, 35, 57, 79, 112, 162, 83])
BU = City(3, [13, 15, 25, 0, 22, 14, 7, 29, 35, 57, 90, 140, 61])
RI = City(4, [13, 29, 24, 22, 0, 29, 22, 16, 44, 75, 106, 156, 84])
SU = City(5, [28, 31, 42, 14, 29, 0, 7, 26, 20, 44, 77, 127, 54])
NW = City(6, [18, 27, 30, 7, 22, 7, 0, 29, 29, 51, 84, 134, 60])
DE = City(7, [24, 36, 35, 29, 16, 26, 29, 0, 33, 62, 98, 148, 80])
LA = City(8, [45, 48, 57, 35, 44, 20, 29, 33, 0, 29, 64, 114, 38])
AB = City(9, [67, 70, 79, 57, 75, 44, 51, 62, 29, 0, 35, 87, 18])
CH = City(10, [99, 103, 112, 90, 106, 77, 84, 98, 64, 35, 0, 52, 49])
HO = City(11, [150, 153, 162, 140, 156, 127, 134, 148, 114, 87, 52, 0, 81])
MI = City(12, [71, 74, 83, 61, 84, 54, 60, 80, 38, 18, 49, 81, 0])
    
#Here is our working list of cities for our graph
cities = [VA, NV, WV, BU, RI, SU, NW, DE, LA, AB, CH, HO, MI]




#create a function that will give us a heuristic value on two cities
def heuristic(city1, city2):

    min_distance = city1.distance[city2.index]
    
    random.seed()
    return (min_distance - randint(5, 10))

def PathFinder(start, finish, algorithm):






