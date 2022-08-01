def ex1() :
    ''' example 1 '''
    print('exampleple 1\n')
    dict1={'name': 'ABCD', 'age': 123, 'height': 157, 'weight': 56}
    # use of for loops and if statement. Also note the use of in keyword.
    for key,val in dict1.items():
        print(key,val,sep=': ')
    print('\n\n')
def ex2(name, age, living=True, *pargs, awards=0,**kwargs) :
    '''example 2
    function arguments
    '''
    print(' example 2\n')
    print('name',name,'and age',age,'are positional arguments.')
    print('living',living,'is a default positional argument')
    print('awards',awards,'is a keyword argument')
    for arg in pargs:
        print(arg,'is an unpacked positional argument')
    for kw in kwargs:
        print(kw, 'is the keyword for', kwargs[kw])
    print('\n\n')

ex1()
ex2('ABCD',23,True,'computers',[12,13],10,awards=100,life='good',lang='py')

