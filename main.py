# Read the README.md
# Read it again
# Your code here
# Delete these 4 lines of comments
# Programmed by Max Rice and Krishon Pinkins
# Loyola CS151, Professor Zee
# Lab Assignment: 05


# Set all values to their correspondent value
initial_balance = 1000
SENTINEL = 'E'
user_input = ''
total_balance = 1000

# While user input is not the string 'E", ask user which input they would like to choose
while user_input != 'E':
    print('What option would you like to choose?')
    print('D-Deposit\nW-Withdraw\nV-View Balance\nE-Exit\n')

# Convert user input to uppercase
    user_input = input().upper()

# If user input is equal to 'D', ask user how much they would like to deposit, add it to the total balance, and output value
    if user_input == 'D':
        deposit_amount = int(input('How much would you like to deposit?: '))
        if total_balance < 0:
            print('You will be charged 5% interest!')

# If user deposits an amount greater than 0, run calculation
        if deposit_amount > 0:
            total_balance = (initial_balance + deposit_amount)
            print('Here is your total balance:$', total_balance)

# If user deposits an amount smaller than zero, output 'Invalid Input'
        else:
            print('Input Invalid!')
# If user input is equal to 'W', ask user how much they would like to withdraw, subtract it to the total balance,/
# and output value
    elif user_input == 'W':
        withdrawal_amount = int(input('How much would you like to withdraw?: '))

# If user withdrawal is greater than zero, run calculation
        if withdrawal_amount > 0:
            total_balance = (initial_balance - withdrawal_amount)
            print('Here is your total balance:$', total_balance)

# If total balance is less than 0, output 'You will be charged 5% interest!'
            if total_balance < 0:
              print('You will be charged 5% interest!')

# If user deposits an amount smaller than zero, output 'Invalid Input'
        else:
            print('Input Invalid!')

# If user input is equal to 'V', output total balance
    elif user_input == 'V':
        print('$', total_balance)
        if total_balance < 0:
            print('You will be charged 5% interest!')




