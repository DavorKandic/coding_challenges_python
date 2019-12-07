def find_twosum(array, target):
    """Finds two numbers in array that add up to the target"""
    is_found = False
    start = 0
    end = len(array) - 1
    result = (None, None)
    while start < end:
        s = array[start] + array[end]
        if s == target:
            is_found = True
            result = (array[start], array[end])
            return is_found, result
        elif s < target:
            start += 1
        else:
            end -= 1
    return is_found, result

        
if __name__ == '__main__':
    
    answer, pair = find_twosum((1,2,4,4), 8)
    print(f'Pair exists? {answer},\n and it is {pair}')
