'''
Problem Statement:
At places, sometimes when friends meet up at a restaurant, they follow a strange procedure to identify who will pay the bill.
All of them put their business cards in a bowl and asks the waiter to pick up a card from the bowl.
THe person whose card is pulled out by the waiter pays the complete bill
'''

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

'''
Solution 1: We are generating a random number between 0 and (length of the list - 1) 
and then use this generated value as index to reference the item in the list
'''
random_index = random.randint(0,4)
print(friends[random_index])

'''
Solution 2: We can directly use a function choice() from the random module that takes a list as a parameter 
and returns a random element from the list as a result.
'''
print(random.choice(friends))
