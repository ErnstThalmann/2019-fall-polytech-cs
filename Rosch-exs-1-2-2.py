def factorial(Number):
 factorial_value = 1
 for i in range(1, Number+1):
   factorial_value *= i
 return factorial_value

def distribution_options_top3(func):
  print(abs(func(Number)//(func(Number-3))))

def distribution_options_all(func):
  print(abs(func(Number)))

print("Enter number of attendees: ")
Number = int(input())
print('value of combinations at top three positions: ')
distribution_options_top3(factorial)
print('value of combinations at all positions : ')
distribution_options_all(factorial)

 






    