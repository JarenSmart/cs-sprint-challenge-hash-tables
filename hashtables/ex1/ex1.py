def get_indices_of_item_weights(weights, length, limit):
    cache = {}  # create table
    # iterate with enumerate
    for index, v in enumerate(weights):
        if limit - v in cache:  # check in cache/hashtable for weight limit/value
            # get index of second value in weighed pair
            weighed_pair = cache.get(limit-v), index
            # returns weights in proper order
            return tuple(sorted(weighed_pair, reverse=True))
        else:
            # create entry if one is not in cache/hashtable
            cache[v] = index

    return None  # return None if weighed pair doesn't exist
