def multsum(below):

    count3  = below // 3
    count5  = below // 5
    low3    = 3
    low5    = 5
    high3   = count3 * 3
    high5   = count5 * 5
    sum3    = (low3 + high3) * count3 // 2
    sum5    = (low5 + high5) * count5 // 2

    return sum3 + sum5

print(multsum(9))
