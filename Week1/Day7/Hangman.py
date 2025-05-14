import random
import HangmanWords
import HangmanArt

print(HangmanArt.game_name)

# Below function prints Right if the letter matches a letter in the word else it prints Wrong
def replace_guessed_letter_in_chosen_word(letter, word, result):
    for i in range(len(word)):
        if word[i] == letter:
            result = result[:i] + letter + result[i+1:]
        else:
            continue
    return result

def is_letter_present_in_chosen_word(letter, word):
    letter_present = False
    for ch in word:
        if ch == letter:
            letter_present = True
    return letter_present

lives = 6
wrong_guess_counter = 0

# Randomly choose a word from the list word_list and assign it to a variable called chosen_word
chosen_word = random.choice(HangmanWords.hangman_words)

# Create a placeholder with same no. of blanks as the no. of letters in the chosen word
placeholder = ""
for ch in chosen_word:
    placeholder += "_"
print(placeholder)

while lives > 0 and placeholder.__contains__("_"):
    guess = input("\nGuess a letter: ").lower()
    if is_letter_present_in_chosen_word(guess, chosen_word):
        placeholder = replace_guessed_letter_in_chosen_word(guess, chosen_word, placeholder)
        print(placeholder)
    else:
        lives -= 1
        print(HangmanArt.hangman_states[wrong_guess_counter])
        print(f"*****************{lives}/6 Lives left*****************")
        wrong_guess_counter += 1
        print(placeholder)

if lives == 0:
    print("\n**********************************You Lost the game**********************************")
    print(f"The chosen word was: {chosen_word}")
else:
    print("\n**********************************You won**********************************")
