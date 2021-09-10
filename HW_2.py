stringOne = 'Some string'
stringTwo = 'Another string'

intOne = 12
intTwo = 26
intThree = 42
intFour = 81

flOne = 1.5
flTwo = 1.775
flThree = 3.44


if intOne > intTwo:
    print('First int is greater than second one')
elif intOne == intTwo:
    print('First int is equal to second one')
else:
    print('Second int is greater than first')

if intThree >= intFour:
    if intThree == intFour:
        print('Third int is equal to fourth')
    else:
        print('Third int is greater than fourth')
elif intThree < intFour:
    print('Fourth int is greater than third')

if intOne <= intFour:
    if intOne == intFour:
        print('First int is equal to fourth')
    else:
        print('Fourth int is greater than first')
elif intOne > intFour:
    print('First int is greater than fourth')

if intTwo != intThree:
    print('Second int is not equal to third')
elif intTwo == intThree:
    print('Second int is equal to third')

if intOne == intThree:
    print('First int is equal to third')
elif intOne != intThree:
    if intOne > intThree:
        print('First int is greater than third')
    else:
        print('Third int is greater than first')

if intFour >= intOne + intTwo:
    if intFour == intOne + intTwo:
        print('Fourth int is equal to first and second combined')
    else:
        print('Fourth int is greater than first and second combined')
else:
    print('First and second int combined are greater than fourth')

if flOne > flTwo:
    print('First float is greater than second')
elif flOne < flTwo:
    print('Second float is greater than first')
else:
    print('First float is equal to second')

if flOne <= flThree:
    if flOne == flThree:
        print('First float is equal to third')
    else:
        print('Third float is greater than first')
elif flOne > flThree:
    print('First float is greater than third')

if flThree >= flTwo:
    if flThree == flTwo:
        print('Third float is equal to second')
    elif flThree > flTwo:
        print('Third float is greater than second')
elif flThree < flTwo:
    print('Second float is greater than third')

if intOne < intFour and not intTwo == intFour:
    print('Fourth int is greater than first and not equal to second')
elif intOne > intFour and not intTwo == intFour:
    print('First int is greater than fourth and second is not equal to fourth')
elif intOne == intFour and intTwo != intFour:
    print('First int is equal to fourth and second is not equal to them')
elif intOne >= intFour and intTwo > intFour:
    print('First int is greater than fourth or equal to it and second is greater than fourth')
elif intOne < intFour or intTwo == intFour:
    print('Fourth int is greater than first or second is equal to fourth')

if not intOne == intThree and not intTwo == intThree:
    if intOne > intThree and intTwo > intThree:
        print('First and seconds ints are greater than third')
    elif intOne < intThree and intTwo < intThree:
        print('Third int is greater than first and second')
elif intOne == intThree or intTwo == intThree:
    print('First or second int is equal to third')
elif intOne == intThree and intTwo == intThree:
    print('First, second and third int are equal')
