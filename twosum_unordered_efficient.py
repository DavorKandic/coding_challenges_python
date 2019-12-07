def has_pair(arr, tgt):
    complements = set()
    i=0
    while i < len(arr):
        comp = tgt - arr[i]
        if comp in complements:
            return True 
        complements.add(comp) 
        i += 1 
    return False


if __name__ == '__main__':

    ans = has_pair((1,2,4,4), 8)
    print(f'Array has respective pair? {ans}')

    ans = has_pair((1,2,3,9), 8)
    print(f'Array has respective pair? {ans}')