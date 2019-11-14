def primsMST(g):

    mstSet = set()

    keys = [0] + [float('inf')]*(len(g)-1)

    cost = 0

    i = 0



    while len(g) is not len(mstSet)+1:

        mstSet.add(i)



        for k in range(len(g[i])):

            keys[k] = min(keys[k], g[i][k])

        

        x = float('inf')

        for k in range(len(keys)):

            if k not in mstSet:

                x = min(x, keys[k])



        cost += x 

        i = keys.index(x)

    return cost





g =[ [float('inf'), 4, 3, float('inf'), float('inf'), float('inf')],

     [4, float('inf'), 1, 2, float('inf'), float('inf')],

     [3, 1, float('inf'), 4, float('inf'), float('inf')],

     [float('inf'), 2, 4, float('inf'), 2, float('inf')],

     [float('inf'), float('inf'), float('inf'), 2, float('inf'), 6],

     [float('inf'),float('inf'),float('inf'),float('inf'),6,float('inf')]

   ]



print(primsMST(g))
