def isPerfect(text):
  ''' Check if a text is a ordered number '''
  min = text[0]
  for letter in text[1:]:
    if min > letter:
      return False
    min = letter
  return True

def bruteForce(text):
  ''' Algorithm to get the greater ordered number by brute force '''
  number = int(text)
  while not isPerfect(str(number)):
    number -= 1
  return number

with open('salida.txt', 'r') as input:
  content = input.read().splitlines()
  for line in content:
    result = isPerfect(line)
    if not result:
      print('Error in', line)
print('Check finished')
