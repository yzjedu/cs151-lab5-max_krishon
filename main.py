# Read the README.md
# Read it again
# Your code here
# Delete these 4 lines of comments

# Set all values to their correspondent value
initial_balance = 1000
SENTINEL = 'E'
user_input = ''
total_balance = 1000

while user_input != 'E':
    print('What option would you like to choose?')
    print('D-Deposit\nW-Withdraw\nV-View Balance\nE-Exit')
    user_input = input().upper()
    if user_input == 'D':
        deposit_amount = int(input('How much would you like to deposit?'))
        if deposit_amount > 0:
            total_balance = (initial_balance + deposit_amount)
            print('Here is your total balance:$', total_balance)
        else:
            print('Input Invalid!')
    elif user_input == 'W':
        withdrawal_amount = int(input('How much would you like to withdraw?'))
        if withdrawal_amount > 0:
            total_balance = (initial_balance - withdrawal_amount)
            print('Here is your total balance:$', total_balance)
    elif user_input == 'V':
        print('$', total_balance)



