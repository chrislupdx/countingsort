def countingsort(A):
    greatest = max(A)
    ol = [0] * (greatest + 1)

    for val in A:  #mark off how many count of numbers
        ol[val] = ol[val] + 1

    val = 0 #Calculate the number of distinct values
    for i in ol:
        if(i > 0):
            val = val + 1

    sl = ol
    temp = sl[0] 
    i = 1
    while(i <= len(sl) - 1): #this adds the current iterated value into the next 
        sl[i] = sl[i] + temp
        temp = sl[i]
        i = i + 1

    #for val in sl:
    #    print(val)

    #go from right to left and replace values to the 0th position to get the first address of each value
    freqlist = [0] * (greatest + 1)
    i = len(sl) - 1
    while(i > 0):
        freqlist[i] = sl[i - 1]
        i= i - 1

    print("printing freqlist")
    for item in freqlist:
       print(item)
    #produce an array the length of A
    sortedList = [0] * len(A)

    #print("aval print")
    #iterate through A from position 0->n
    #for aVal in A:
    #    print(aVal)

    limit = len(A)
    i = 0
    while(i < limit): #for each item in A
        j = 0 
        flen = len(freqlist)
        while (j < flen): #traverse the frequency list
            if A[i] == j: #if the item in our array matches the value of the position in the frequency list
                position = freqlist[j]  #grab the position that we should be putting A[i] into the sorted array
                sortedList[position] = A[i]
                freqlist[j] = freqlist[j] + 1
            j = j + 1
        i = i + 1

            #put aVal into sortedList[matchlocation] #we might need to do this in a while loop
    print('printing sorted list')
    for i in sortedList:
        print(i)

A = [1, 0, 3, 1, 3, 1]
countingsort(A)
