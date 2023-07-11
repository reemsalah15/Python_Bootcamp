import random
import hangman_words
import hangman_art
#Step 1 


word_list = hangman_words.word_list
logo = hangman_art.logo
stages = hangman_art.stages
lives = 6

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2: - Create an empty List called display.
print(logo)
chosen_word = random.choice(word_list)
display = []
len_word = len(chosen_word)
End_Game = False 


print(chosen_word)

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

for spaces in range(0,len_word):
    display.append("_")
print(f"{' '.join(display)}\n")



#TODO-3: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.

#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-4: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while not End_Game:
    guess = input("Can you guess the letter? ") 
    guess = guess.lower()  
    if guess in display:
        print(f"You've already guessed {guess}")   
    for index in range(0,len_word):
        if guess == chosen_word[index]: 
            display[index]=guess
              
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")       
    if "_" not in display:
        End_Game = True
        print("You win.")
    elif lives == 0:
        End_Game = True
        print("You lose.")
   
    
    print(f"{' '.join(display)}\n")
    print(stages[lives])        
