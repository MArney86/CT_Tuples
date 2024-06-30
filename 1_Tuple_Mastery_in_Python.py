#Task 1:

def format_itineraries(itineraries): #a function that returns a string of formatted travel itineraries from the list of itinerary tuples
    formatted_string = "" #initialize string for formatted itineraries
    i = 1 #counter for formatted itineraries
    for itinerary in itineraries: #iterate through list of itineraries
       formatted_string = formatted_string + f"Itinerary {i}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}\n" #construct the formatted string and add to end of the existing string
       i += 1 #update the counter for next iteration
    return formatted_string #return the formatted string

travel_itineraries = [('Janet', 'Tokyo', 'Hong Kong'), #list of travel itenerary tuples
                      ('Jose', 'New York','Austin'),
                      ('Harold', 'Cincinnati', 'Mexico City'),
                      ('Carl', 'Atlanta', 'Kingston'),
                      ('Sheryl', 'Oslo', 'Boston')]

print(format_itineraries(travel_itineraries)) #print formatted itineraries string