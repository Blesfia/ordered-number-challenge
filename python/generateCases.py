import random
# Generate list of samples
cases = [random.randint(0, 10**18) for x in range(0, 100000)]
# Generate input.txt file
with open('input.txt', 'w') as f:
  print(100000, file=f)
  for n in cases:
    print(str(n), file=f)
