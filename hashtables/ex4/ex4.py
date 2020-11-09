def has_negatives(a):
    """
    YOUR CODE HERE
    """
    #set up hashable array
    hash_table = dict()
    #initiate list
    result = []
    
    for i in a:
        get_negative = hash_table.get(i * -1)
        if get_negative:
            if i >= 0:
                result.append(i)
            else:
                result.append(i * -1)
        else:
            hash_table[i] = i
    print(result, ' have negative values.')
    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
