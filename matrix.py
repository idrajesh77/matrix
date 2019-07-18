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

def findMax(matrix, len):
    
    a = np.array([ int(x) for x in matrix.split() ]).reshape(len,len)
    print (a)
    b = a[::-1,]

    maxprod = 0

    for i in range(len):
        for j in range(len):
            r = np.prod( a[i][j:j+4] )
            c = np.prod( a[:,j][i:i+4] )
            k = min(i,j)
            d1 = np.prod( np.diagonal(a, j-i)[ k:k+4 ] )
            d2 = np.prod( np.diagonal(b, j-i)[ k:k+4 ] )
            maxprod = max([maxprod,r,c,d1,d2])
    
    return maxprod

def countOfThrees(data, len):
    maxcount=0

    return maxcount

maxm = findMax(grid, 10)
print (maxm)

count = countOfThrees(grid, 10)
print (count)