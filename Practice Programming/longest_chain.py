def longest_chain(upto):
    largest = 0
    longestSeq = 0
    cache = {}
    for n in xrange(2, upto+1):
        Number = n
        counter = 0
        while Number > 1:
            if Number  in cache.keys()
                counter += cache[Number] - 1
            if Number % 2 == 0:
                Number = Number / 2
            else:
                Number = Number * 3 + 1
            counter += 1  # 4,8 example
 
        counter += 1
        cache[n] = counter
 
        if counter > longestSeq:
            longestSeq = counter
            largest = n
    return largest

print longest_chain(1000000)