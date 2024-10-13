# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
1. Set the initial balance at $1000
2. Set Sentinel to value 'E'
3. Set user option to empty string
3. While user input is not SENTINEL:
   1. Ask user to input what option they want
   2. if user input = 'D'
      1. Ask user how much they wish to deposit
      2. if user input > 0:
         1. Calculate (initial_balance + new_deposit)
         2. Set value
         3. Output value
      3. Otherwise, output 'Amount Invalid!"
   3. Otherwise if user input = 'W'
      6. if user input > 0:
         7. Calculate (initial_balance - new_withdrawal)
         8. Set value
         9. Output value
      7. Otherwise, output 'Amount Invalid'
   4. Otherwise if user input = 'V'
      7. Output most recent balance to user