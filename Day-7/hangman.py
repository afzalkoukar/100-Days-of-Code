import random
import hangman_art
import hangman_words

print(hangman_art.logo)

word = random.choice(hangman_words.word_list)


def split(word):
    return list(word)

split_word = (split(word))



lenght = len(word)
print(lenght)
display = []
for i in range(0,lenght):
    display.append("_")

end_of_game = False

lives = 6
 
while (not end_of_game):
    guess = input("Take a guess\n").lower()

    if(guess in display):
        print(f'You have already guessed {guess}')

    for i in range (0,lenght):
        if(guess==split_word[i]):
            display[i] = guess
    
    if(guess not in word):
        print(f'{guess} is not in the word, You lost a live')
        lives = lives - 1
    
    print(display)

    if("_" not in display):
        end_of_game = True
        print("you win")
    
    if(lives==0):
        end_of_game = True
        print("You lose")
    
    print(hangman_art.stages[lives])


