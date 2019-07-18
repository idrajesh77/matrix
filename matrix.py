import numpy as np

grid = \
        '''
        8	2	22	97	38	15	0	40	0	75
        49	49	99	40	17	81	18	57	60	87
        81	49	31	73	55	79	14	29	93	71
        52	70	95	23	4	60	11	42	69	24
        22	31	16	71	51	67	63	89	41	92
        24	47	32	60	99	3	45	2	44	75
        32	98	81	28	64	23	67	10	26	38
        67	26	20	68	2	62	12	20	95	63
        24	55	58	5	66	73	99	26	97	17
        21	36	23	9	75	0	76	44	20	45'''

def countOfThrees(matrix, n, m, adjNums):
    if adjNums <= 0: return ZeroDivisionError

    count=0
    a = np.array([ int(x) for x in matrix.split() ]).reshape(n,m)
    
    b = a[::-1,]
    # print (b)
    # print (np.shape(b))

    for i in range(n):
        for j in range(m):
            if  len( a[i][j:j+adjNums]) == adjNums:
                r = len( a[i][j:j+adjNums] )/adjNums
            if len( a[:,j][i:i+adjNums] ) == adjNums:
                c = len( a[:,j][i:i+adjNums] )/adjNums
            k = min(i,j)
            if len(np.diagonal(a, j-i)[ k:k+adjNums ]) == adjNums:
                d1 = len( np.diagonal(a, j-i)[ k:k+adjNums ] )/adjNums
            if len( np.diagonal(b, j-i)[ k:k+adjNums ]) == adjNums:
                d2 = len( np.diagonal(b, j-i)[ k:k+adjNums ] )/adjNums
            count = sum([count,r,c,d1,d2])
      
    return count 

def findMax(matrix, n, m, adjNums):
    if adjNums <= 0: return ZeroDivisionError

    maxprod = 0

    a = np.array([ int(x) for x in matrix.split() ]).reshape(n,m)
    
    b = a[::-1,]
    # print (b)
    # print (np.shape(b))

    for i in range(n):
        for j in range(m):
            if  len( a[i][j:j+adjNums]) == adjNums:
                r = np.prod( a[i][j:j+adjNums] )
            if len( a[:,j][i:i+adjNums] ) == adjNums:
                c = np.prod( a[:,j][i:i+adjNums] )
            k = min(i,j)
            if len(np.diagonal(a, j-i)[ k:k+adjNums ]) == adjNums:
                d1 = np.prod( np.diagonal(a, j-i)[ k:k+adjNums ] )
            if len( np.diagonal(b, j-i)[ k:k+adjNums ]) == adjNums:
                d2 = np.prod( np.diagonal(b, j-i)[ k:k+adjNums ] )
            maxprod = max([maxprod,r,c,d1,d2])
    
    return maxprod

def printMe():
    count = countOfThrees(grid, 10, 10, 3)
    print ("max count of 3 adjacent number: %s" % (count))
    maxm = findMax(grid, 10, 10, 3)
    print ("max product of 3 adjacent number: %s" % (maxm))

printMe()