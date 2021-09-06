# todo vars for 1-10 Ex's
stringVar = "Some string type variable"
intVar = 16
floatVar = 25.4
byteVar = bytes(10)
listVar = ['s', 'p', 'i', 's', 'o', 'k']
tupleVar = ('t', 'u', 'p', 'l', 'e')
setVar = {'a', 'b', 'c'}
frozensetVar = frozenset('abcd')
dictVar = {'id': 1, 'city': 'Moscow'}

# todo vars for Ex 11
stringOne = 'First string '
stringTwo = 'Second string'
stringResult = stringOne+stringTwo

# todo vars for Ex's 12-16
intOne = 10
intTwo = 255
intResultAdd = intOne + intTwo
intResultDiv = intTwo / intOne
intResultMult = intOne * intTwo
intResultDiv2 = intTwo // intOne
intResultDiv3 = intTwo % intOne

# todo list of vars to print
varStorage = [stringVar, intVar, floatVar, byteVar, listVar, tupleVar, setVar, frozensetVar, dictVar]

# todo "for" cycle that prints vars value and type
for i in varStorage:
    print(i, type(i))

# todo printing Ex 11 result
print(stringResult)

# todo printing Ex's 12-16 results
print('Our vars are ' + str(intOne) + ' and ' + str(intTwo))
print('Addition result =  ' + str(intResultAdd))
print('Division result =  ' + str(intResultDiv))
print('Multiplication result =  ' + str(intResultMult))
print('Integer division result =  ' + str(intResultDiv2))
print('Remainder of division result =  ' + str(intResultDiv3))
