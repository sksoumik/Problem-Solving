# Take input from user
number = int (input("Enter a number to check"))
#Now check
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'is not a prime number')
            # Print the reason for not being prime
            print('Because', i, 'times', number//i, 'is', number)
            break

    else:
        print(number, 'is a prime number')

else:
    print(number, 'is not a prime number')
