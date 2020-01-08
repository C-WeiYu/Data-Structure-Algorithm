def adjacentElementsProduct(inputArray):
    b=[]
    for i in range(0,len(inputArray)-1):
        num=inputArray[i]*inputArray[i+1]
        b.append(num)
    return max(b)
