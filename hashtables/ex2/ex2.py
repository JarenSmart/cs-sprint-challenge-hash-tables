#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}  # create cache/hashtable of boarding passes
    itinerary = []  # list of destinations
    for t in tickets:  # for loop that adds all 'flights' to created cache/hashtable
        cache[t.source] = t.destination

    itinerary.append(cache['NONE'])  # first flight out

    for d in range(1, length):
        next_stop = itinerary[d-1]
        if next_stop in cache:
            itinerary.append(cache[next_stop])  # add trip to list

    return itinerary
