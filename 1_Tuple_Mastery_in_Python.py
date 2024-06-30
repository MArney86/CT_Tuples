#Task 1:

def format_itineraries(itineraries):
    formatted_string = ""
    i = 1
    for itinerary in itineraries:
       formatted_string = formatted_string + f"Itinerary {i}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}\n"
       i += 1
    return formatted_string

travel_itineraries = [('Janet', 'Tokyo', 'Hong Kong'),
                      ('Jose', 'New York','Austin'),
                      ('Harold', 'Cincinnati', 'Mexico City'),
                      ('Carl', 'Atlanta', 'Kingston'),
                      ('Sheryl', 'Oslo', 'Boston')]

print(format_itineraries(travel_itineraries))