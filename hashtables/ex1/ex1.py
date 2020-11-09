def get_indices_of_item_weights(weights, length, limit):
    # length is simply length of weights array
    length = len(weights)
    # create a dict or hash table
    hash_table = dict()

    # return none if we only have one item in our array
    if length <= 1:
        return None

    # for i in array
    for i in range(length):
        # w is weight at current index
        w = weights[i]
        # if weight is in our hash table
        if w in hash_table:
            # store it as a value
            val = hash_table[w]
            # return the index and the value in an ordered array
            return [i, val]
        # else take the difference of the limit minus the current weight, set to i
        else:
            hash_table[limit-w] = i
    # return empty array
    return []

    return None

weights = [4, 6, 10, 15, 16] 
length = 5 
limit = 21
print(get_indices_of_item_weights(weights, length, limit))

#Example:
#input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
#output: [ 3, 1 ] -> since these are the indices of weights 15 and 6 whose sum equals 21