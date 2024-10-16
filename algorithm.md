# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
1. Set the initial balance at $1000
2. Set Sentinel to value 'E'
3. Set user option to empty string
3. While user input is not SENTINEL:
   1. Ask user to input what option they want
   2. If user input = 'D'
      1. Ask user how much they wish to deposit
      2. If user input > 0:
         1. Calculate (initial_balance + new_deposit)
         2. Set value
         3. Output value
      3. Otherwise, output 'Amount Invalid!"
   3. Otherwise if user input = 'W'
      4. If user input > 0:
         4. Calculate (initial_balance - new_withdrawal)
         5. Set value
         6. Output value
         7. If total balance < 0
            1. Output 'You will be charged 5% interest!'
      5. Otherwise, output 'Amount Invalid'
   4. Otherwise if user input = 'V'
      6. Output most recent balance to user
      7. If total balance < 0
         1. Output 'You will be charged 5% interest!'