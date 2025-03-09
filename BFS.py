# Name: Ali Hassan
# Student ID: F22BDOCS1E02011
# Assignment: Assignment 1 - BFS.ipynb



#Breadth-First Search (BFS) code write in python
def find_shortest_way(places, start_point, end_point):

 check_these_places = [(start_point, [start_point])] # places to look at later

 places_i_already_went = set() # don't go back!



 while check_these_places:

  this_place_now, the_path_i_got = check_these_places.pop(0) # first one in, first one out?



  if this_place_now not in places_i_already_went:

   if this_place_now == end_point:

    return the_path_i_got # found it!



   places_i_already_went.add(this_place_now)



   for next_place_to_go in places.get(this_place_now, []):

    check_these_places.append((next_place_to_go, the_path_i_got + [next_place_to_go])) # add to the list



 return None # guess there's no way



my_place_connections = [

 ('S', 'A', 3), ('S', 'B', 6), ('S', 'C', 2),

 ('A', 'D', 3), ('B', 'E', 2), ('C', 'E', 1),

 ('D', 'F', 5), ('F', 'G', 5), ('E', 'H', 5),

 ('H', 'G', 5), ('B', 'G', 9), ('D', 'B', 4),

 ('E', 'F', 6)

]



connections_map = {} # make a thing to hold the places

for place_from, place_to, distance_between in my_place_connections:

 connections_map.setdefault(place_from, []).append(place_to)

 connections_map.setdefault(place_to, []).append(place_from) # both ways!



start_of_trip = 'S'

end_of_trip = 'G'



the_real_route = find_shortest_way(connections_map, start_of_trip, end_of_trip)



if the_real_route:

 print("Found the shortest way! It's:", the_real_route) # yay!

else:

 print("Couldn't find a route :(") # oh no