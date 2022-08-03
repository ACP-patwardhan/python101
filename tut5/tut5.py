def ex1() :
    '''example 1 describing what list comprehensions are'''
    '''This is how you would generate l2 using for loops
       for x in l1:
        for y in l2:
            if(x!=y):
                l3.append((x,y))
    '''
    l1 = range(6)
    l2 = [x**2 - 3*x for x in l1]
    l3 = [(x,y) for x in l1 for y in l2 if x!=y]
    print('example 1:')
    print(l1,l2,l3,len(l3))
    print('')



def ex2():
    '''example describing nested list comprehension'''
    '''This is how you would create a 3x3 matrix using for loops.
    l=[]
    for x in range(3):
        sl=[]
        for y in range(3):
            sl.append(3*x+y+1)
        l.append(sl)
    '''
    l = [[3*x+y+1 for y in range(3)] for x in range(3)]
    print('example 2:')
    print(l)
    print()

def ex3():
    '''example describing lambda functions and zip function'''
    x = lambda : print('I\'m lamb')
    l = [[3*x+y+1 for y in range(3)] for x in range(3)]
    c = lambda x: list(x)
    z =list( [c(x) for x in zip(*l)])
    print('example 3:')
    x()
    print('transpose  of', l, 'is' ,z)
    print()

ex1()
ex2()
ex3()
