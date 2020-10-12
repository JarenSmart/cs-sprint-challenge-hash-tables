def has_negatives(a):
    cache = {}
    result = []
    for v in a:  # loop through list and add them to cache
        if -v in cache:  # if neg value in list
            if v > -v:
                result.append(v)  # add value to list
            else:
                result.append(-v)  # add neg value to list
        else:
            cache[v] = ""  # throw value in cache

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
