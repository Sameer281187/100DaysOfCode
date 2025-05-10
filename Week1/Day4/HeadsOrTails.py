import random

# Here we are generating a random number, either 0 or 1, and saving the generated value to variable result
result = random.randint(0,1)

# Below we will check based on the random value generated and print a result based on the generated value.
# 0 - Tails, 1 - Heads
if result > 0:
    print("Heads")
else:
    print("Tails")