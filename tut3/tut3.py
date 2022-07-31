# This is a comment
'''Use multiline string and 
don't assign it 
to create a multi line comment'''
print(2+2 / 4) # notice operator precedence
print(-3**2) # notice ** preceedence
stringVar, listVar,i = "Python", [1,2,3,4],0 # multiple assignment of variables. stringVar now becomes a immutable string.listVar becomes a list, i is an int
print(stringVar, stringVar[0], stringVar[-3], stringVar[len(stringVar)-1], stringVar[:3], sep=', ') #notice the use of sep keyword argument.
while i<len(listVar):
    listVar[i]**=2 #list is mutable so we modify it inplace , also notice the use of **= operator.
    i+=1
print(listVar) 
listVar=[] # we can clear a list like this
print(listVar)
