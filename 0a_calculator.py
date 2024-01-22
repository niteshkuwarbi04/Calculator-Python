def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return 'Cannot divide by zero'

while True:
    print('Enter choices :')
    print('1. Addition')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')

    choice = input('Enter any one operation (1, 2, 3, 4) :')

    if choice in ('1', '2', '3', '4'):
        number1 = float(input('Enter first number : '))
        number2 = float(input('Enter second value : '))

        if choice == '1':
            print(f'{number1} + {number2} = ', add(number1, number2))
        
        elif choice == '2':
            print(f'{number1} - {number2} = ', sub(number1, number2))
        
        elif choice == '3':
            print(f'{number1} X {number2} = ', mul(number1, number2))

        elif choice == '4':
            print(f'{number1} % {number2} = ', div(number1, number2))

        else: 
            print('Invalid input.')

    repeat = input("Enter 'yes' to continue or tap enter to exit : ")
    if (repeat.lower() != 'yes'):
        break

    else:
        print(f'Invalid Input')