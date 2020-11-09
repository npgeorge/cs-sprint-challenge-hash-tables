def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # stop on non-computable arrays
    length = len(arrays)
    if length <= 1:
        return print('Not enough arrays to compute...')

    # create hashing dictionary
    hash_dict = dict()
    
    # starting with the first array in list of arrays
    for first_index in arrays[0]:
        # set first index to 1
        hash_dict[first_index] = 1

    # dealing with the rest
    for current in arrays[1:]:
        # for index in current
        for index in current:
            try:
                if hash_dict[index]:
                    hash_dict[index] += 1
            except:
                pass
    
    # initialize result array
    result = []
    # for key value pair in our hashing dict
    for (key, value) in hash_dict.items():
        # if our value equals our arrays length
        if value == len(arrays):
            # append the key to results array
            result.append(key)
    
    return result

#arrays = [[1,2,3], [1,4,5], [1,6,7]]
#print(intersection(arrays))

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
