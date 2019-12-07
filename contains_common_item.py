def has_common_item(arr1, arr2):
    """Checks if any of the itmes in first array is in the second array"""
    for item in arr1:
        if item in arr2:
            return True 
    return False

if __name__ == '__main__':

    a1 = ('a', 'b', 'c', 'x')
    a2 = ('z', 'y', 'i')
    print(has_common_item(a1, a2))    # should return False

    a1 = ('a', 'b', 'c', 'x')
    a2 = ('z', 'y', 'x')
    print(has_common_item(a1, a2))    # should return True
