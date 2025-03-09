# Name: Ali Hassan
# Student ID: F22BDOCS1E02011
# Assignment: Assignment 1 - DFS.ipynb

# Depth first search (DFS) code write in python



def find_a_route(place_list, start_place, end_place):

 to_look_at = [(start_place, [start_place])] # make a list of places to check

 already_seen = set() # keep track of where i went



 while to_look_at:

  current_spot, the_route_so_far = to_look_at.pop() # get the last one?



  if current_spot not in already_seen:

   if current_spot == end_place:

    return the_route_so_far # found it!



   already_seen.add(current_spot)



   for next_place in place_list.get(current_spot, []):

    to_look_at.append((next_place, the_route_so_far + [next_place])) # add more to check



 return None # guess there's no route?



my_places_and_roads = [

 ('S', 'A', 3), ('S', 'B', 6), ('S', 'C', 2),

 ('A', 'D', 3), ('B', 'E', 2), ('C', 'E', 1),

 ('D', 'F', 5), ('F', 'G', 5), ('E', 'H', 5),

 ('H', 'G', 5), ('B', 'G', 9), ('D', 'B', 4),

 ('E', 'F', 6)

]



connections_between_places = {} # make a thing to hold the connections

for place1, place2, distance in my_places_and_roads:

 connections_between_places.setdefault(place1, []).append(place2)

 connections_between_places.setdefault(place2, []).append(place1) # both ways!



start_trip_here = 'S'

end_trip_there = 'G'



the_path_we_need = find_a_route(connections_between_places, start_trip_here, end_trip_there)



if the_path_we_need:

 print("Found the path! It's:", the_path_we_need) # yay!

else:

 print("Couldn't find a path :(") # oh no