#Car Path Finder.py --- code by Aaron Thiesen
#This is a path finding solution coded to with the A* algorithm to find paths between cities in Vancouver area and the lower mainland 


import random


#make a class to hold the data each city needs including values for heuristics and cost which are only used during the algorithms
class City:

    def __init__(self, index, distance, name, heuristic = None, cost = None):
    
        self.index = index
        self.distance = distance
        self.name = name
        self.heuristic = heuristic
        self.cost = cost

#make a class to return from the algorithm to have more organized data
class Route:

   def __init__(self, total_distance, path):
    
        self.total_distance = total_distance
        self.path = path

#initialize all the cities as city classes with stored data on their distance to one another
#the order of the lists is the same order their distance to one another ie: VA.distance[1] = the distance between VA and NV and BU.distance[0] = the distance between BU and VA
#the units are all in km and are rounded to nearest integer
VA = City(0, [0, 18, 11, 13, 13, 28, 18, 24, 45, 67, 99, 150, 71], "Vancouver")
NV = City(1, [18, 0, 10, 15, 29, 31, 27, 36, 48, 70, 103, 153, 74], "North Vancouver")
WV = City(2, [11, 10, 0, 25, 24, 42, 30, 35, 57, 79, 112, 162, 83], "West Vancouver")
BU = City(3, [13, 15, 25, 0, 22, 14, 7, 29, 35, 57, 90, 140, 61], "Burnaby")
RI = City(4, [13, 29, 24, 22, 0, 29, 22, 16, 44, 75, 106, 156, 84], "Richmond")
SU = City(5, [28, 31, 42, 14, 29, 0, 7, 26, 20, 44, 77, 127, 54], "Surrey")
NW = City(6, [18, 27, 30, 7, 22, 7, 0, 29, 29, 51, 84, 134, 60], "New Westminster")
DE = City(7, [24, 36, 35, 29, 16, 26, 29, 0, 33, 62, 98, 148, 80], "Delta")
LA = City(8, [45, 48, 57, 35, 44, 20, 29, 33, 0, 29, 64, 114, 38], "Langley")
AB = City(9, [67, 70, 79, 57, 75, 44, 51, 62, 29, 0, 35, 87, 18], "Abbotsford")
CH = City(10, [99, 103, 112, 90, 106, 77, 84, 98, 64, 35, 0, 52, 49], "Chilliwack")
HO = City(11, [150, 153, 162, 140, 156, 127, 134, 148, 114, 87, 52, 0, 81], "Hope")
MI = City(12, [71, 74, 83, 61, 84, 54, 60, 80, 38, 18, 49, 81, 0], "Mission")

#locations is used to tell if user input is valid 
locations = ["VA", "NV", "WV", "BU", "RI", "SU", "NW", "DE", "LA", "AB", "CH", "HO", "MI"]


#create a function that will give us a heuristic value on two cities
def heuristic(city1, city2):

    min_distance = city1.distance[city2.index]
        
    #since the heuristic function has random elements I can't call it directly during the loop or else it will sometimes give a different heuristic value for one city
    #which allows for the city to be chosen twice in a row sometimes, so to solve this I seed using the index of the city getting the heuristic, this lets me call the function during the loop
    #this could also be fixed by running all the heuristics once before the loop then referencing them
    #random.seed(city1.index)
    return (min_distance - random.randint(5, 10))

#Here is our parent function that will drive whichever algorithm is chosen to find the optimal path between cities.
def PathFinder(start, finish, algorithm):

    if algorithm == 'A_Star' or algorithm == 'a_star' or algorithm == 'A_star' or algorithm == 'A*':
        result = A_star(start, finish)
    
    else:
        print("UNDEFINED ALGORITHM CHOSEN!")
    
    #print the returned path from whichever algorithm was chosen
    print("The optimal path from %s to %s is:" %(start.name, finish.name))
    
    for i in range(len(result.path)):
        print(result.path[i])
    
    print("With a total distance of %s km" %(result.total_distance))
    print(result.total_distance)



def A_star(start, finish):

    #Here is our working list of cities for our graph
    cities = [VA, NV, WV, BU, RI, SU, NW, DE, LA, AB, CH, HO, MI]
    

    #set the heuristic of the goal to zero and the cost of start to zero
    cities[finish.index].heuristic = 0
    start.cost = 0
    
    #make our starting node the starting city
    current = start
    
    #result is a class variable used to track the data we want to return
    result = Route(0, [])
    
    #add the starting point to the results path
    result.path.append(start.name)
    
    #lowesth is a variable used to track what the next current node will be based on the lowest heuristic
    lowesth = None
    
    
    #THIS IS TEST CODE FOR IF YOU WANT TO ELIMINATE DIRECT ROUTES
    #This will set the  direct distance between the start and finish nodes arbitrarily high as to make the code find a non-direct route through other cities
    #finish.distance[start.index] = 999

    
    
    #only exit the loop once we have located the goal
    while (current.index != finish.index):
        
        #remove the current city from the list --- thanks to https://stackoverflow.com/questions/9140857/oop-python-removing-class-instance-from-a-list for this code
        for i in range(len(cities)):
            if cities[i].index == current.index:
                del cities[i]
                break

        for i in range(len(cities)):
            
            #if the iterated city node has not had their cost calculated or if it is larger than the current
            if (cities[i].cost == None or cities[i].cost > current.cost + cities[i].distance[current.index]):
                
                #then update the costs based on current cost + cost to travel from current
                cities[i].cost = current.cost + cities[i].distance[current.index]
                
            #update the heuristic for each city node
            cities[i].heuristic = cities[i].cost + heuristic(cities[i], finish)


        
        

        #choose the next current node based on their lowest heuristic value 
        #this is where some of the randomness in our heuristic function can lead to the algorithm not choosing the best path,
        #sometimes the randomized heuristic is chosen for a non-optimal path
        for i in range(len(cities)):      
            if (lowesth == None or cities[i].heuristic < lowesth.heuristic or lowesth == current):
                lowesth = cities[i]
        
        #swap the current over, first saving it as a parent to easily calculate total distance
        parent = current
        current = lowesth

        #store the current node in our path and update the total distance
        result.path.append(current.name)
        result.total_distance = result.total_distance + current.distance[parent.index]
        
    return result

validinput = False
while (validinput != True):

    print("Please choose a STARTING location from the list below:")
    startinput = input("VA, NV, WV, BU, RI, SU, NW, DE, LA, AB, CH, HO, MI\n")

    if locations.count(startinput) > 0:
        validinput = True


validinput = False
while (validinput != True):

    print("Please choose an ENDING location from the list below:")
    destinationinput = input("VA, NV, WV, BU, RI, SU, NW, DE, LA, AB, CH, HO, MI\n")
    
    if locations.count(destinationinput) > 0:
        validinput = True    

validinput = False
while (validinput != True):

    print("Please choose an Algorithm:")
    algorithm = input("A_Star\n")
    
    if algorithm == 'A_Star' or algorithm == 'a_star' or algorithm == 'A_star' or algorithm == 'A*':
        validinput = True    


PathFinder(eval(startinput), eval(destinationinput), algorithm)