"""
  Algorithm to retrieve the greater ordered number from a N number
  This algorithm follows a Backtracking implementation
  Complexity is log(n)
"""

def needsImprove(number):
  """
    Define if a string number needs to be improved based on first 2 digits
    for example:
      10  needs to be improved
      1   DONT need to be improved
      01  needs to be improved
      100 DONT need to be improved
    Keyword arguments:
      number -- string number to check, all characters needs to be a digit
  """
  # Base case with less than 2 digits
  if len(number) <= 1:
    return False
  # General case
  return int(number[0]) < int(number[1])

def decreaseDigit(number):
  """
    Decrease an string number based on first 2 digits
    for example:
      0 will be 0
      9 will be 0
      09 will be 98
      67 will be 57

    Keyword arguments:
      number -- string number to decrease, all characters needs to be a digit
  """
  # Base case with less than 2 digits
  if len(number) <= 1:
    return number
  # Case when first digit is 0, then return 9 & (n2-1)
  if number[0] == "0":
    return "9" + str(int(number[1]) - 1)
  # General case, then return (n1 - 1) & n2
  return str(int(number[0]) - 1) + number[1]

def processNumber(number):
  """
    Main process to order a number
    Keyword arguments:
      number -- string number to process
  """
  # Base case when number is less than 10
  if len(number) <= 1:
    return number
  # Case when number is not ordered
  if needsImprove(number[0:2]):
    # Decrease first 2 digits
    n = decreaseDigit(number[0:2])
    # Return the process of the new number
    return processNumber (n + number[2:])
  # Case when number is ordered
  else:
    # Process the number since its second digit
    result = processNumber(number[1:])
    # If first digit of result is 9, change previous number to 9
    if (result[0] == '9'):
      return '9' + result
    # Return first improved digit and the result
    return number[0] + result

def start(number):
  """
    Start the process to improve a number
  """
  #Reverse the input, process reversed, input and reverse the output 
  return int(processNumber(number[::-1])[::-1])

# Logic to docks with challenge input
with open('entrada.txt', 'r') as input:
  with open('salida.txt', 'w') as output:
    content = input.read().splitlines()
    cases = int(content[0])
    for lineNumber in range(1, cases + 1):
      n = content[lineNumber]
      print(start(n), file=output)