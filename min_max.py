def find_max_min (x):
    # this function fails if the list length is 0 
    # at start min is equal to max value which is the value at the fisrt index
    #loop through to each value to compare
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum: maximum = i
    if minimum == maximum:
      return [len(x)]
    return [minimum,maximum]