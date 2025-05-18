'''
To work out the love score between two people:
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
2. Then check for the number of times the letters in the word LOVE occurs.
3. Then combine these numbers to make a 2-digit number and print it out.

e.g.

name1 = "Kanye West" name2 = "Kim Kardashian"
T occurs 1 times
R occurs 1 time
U occurs 0 times
E occurs 2 times
Total = 4

L occurs 0 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 2

Love Score = 42

Example Input
calculate_love_score("Kanye West", "Kim Kardashian")

Example Output
42
'''

def calculate_love_score(name1, name2):
    final_name = name1 + name2

    true_result = 0
    love_result = 0

    for ch in "TRUE":
        for char in final_name:
            if ch.lower() == char.lower():
                true_result += 1

    for ch in "LOVE":
        for char in final_name:
            if ch.lower() == char.lower():
                love_result += 1

    score = true_result * 10 + love_result

    print(score)

name1 = input("Please enter first person's name: ")
name2 = input("Please enter second person's name: ")

calculate_love_score(name1, name2)
