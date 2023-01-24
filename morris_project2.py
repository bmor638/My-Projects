"""
    Terminal version of "Wordle," where the user has 6 tries to guess a random 5-letter word
    Filename: morris_project2.py
    Author: Beckett Morris
    Date: 01/16/2023
    Course: COMP 1352-3
    Assignment: Project 2 - A Word Game
    Collaborators: None
    Internet Source: None
"""


from random import choice


"""
    Corrects the number of Y's for duplicate characters
    parameters: guess (string of 5 letters), answer (string of 5 letters), result (list of 5 G's, Y's, and B's)
    return: result (list of corrected G's, Y's, and B's)
"""
def check_duplicates(guess, answer, result):
    for i in range(5):
        letter = answer[i]
        guess_instances = guess.count(letter)
        answer_instances = answer.count(letter)
        if guess_instances > answer_instances:  #if there are more instances of letter in guess than in answer
            indices_in_guess = [index for index in range(5) if guess[index] == letter]  #gets the indices of letter in guess
            #removes indices corresponding with G's to isolate Y's
            for index in indices_in_guess:
                if result[index] == "G":
                    indices_in_guess.remove(index)
            result[indices_in_guess[-1]] = "B"  #changes last "Y" instance of letter to "B"
    return result  #result now corrected


"""
    Compares the letters in guess to the answer, adding a G to the result if the letter is in the correct place, 
        a Y if the letter is in the answer but not in the correct place, and a B if the letter is not in the answer
    parameters: guess (string of 5 letters), answer (string of 5 letters)
    return: string of the list returned by check_duplicates(guess, answer, result)
"""
def compare(guess, answer):
    result = []
    for i in range(5):
        if guess[i] in answer:
            if guess[i] == answer[i]:
                result.insert(i, "G")  #letter in answer and correctly placed
            else:
                result.insert(i, "Y")  #letter in answer but incorrectly placed
        else:
            result.insert(i, "B")  #letter not in answer
    return ''.join(check_duplicates(guess, answer, result))  


"""
    Chooses a random word from the opened dictionary to be the answer, repeatedly prompts the user for guesses until solved
        while ensuring that the word is in the dictionary and that the user does not go beyond 6 guesses
    parameters: None
    return: None
"""
def main():
    #opening print statements
    print("Welcome to Wordle! You have six chances to guess the five-letter word.")
    print("A letter G means you got that letter correct and in the right position.")
    print("A letter Y means you matched that letter, but it is in the wrong position.")
    print("A letter B means that letter does not appear in the correct word.")

    #creates a list of 5-letter words from the file of words
    with open(r"C:\Users\Beckett Morris\OneDrive - University of Denver\Documents\Freshman Year\Winter\COMP 1352\Project 2\usaWords.txt") as file:
        dictionary = [word.strip() for word in file if len(word) == 6]

    #chooses a random word from 'dictionary'
    answer = choice(dictionary)

    #guessing process
    solved = False
    num_guesses = 1  
    guess_history = []
    while solved == False and num_guesses <= 6:  #continues until solved or all 6 guesses used
        guess = input("What is your guess? ")
        if guess not in dictionary:  #catches guesses that are not in the dictionary or are not the right length
            print("That is not a five-letter word in our dictionary.")
        else:
            result = compare(guess, answer)
            guess_history.append("Guess " + str(num_guesses) + ": " + guess + "  " + result)
            print("\n".join(guess_history))  #prints all guesses and result history with each guess

            #checks if solved
            if result == "GGGGG":
                solved = True
                print(f'You win. You got it in {num_guesses} guesses.')
            else:
                num_guesses += 1

            if num_guesses == 7: #stops game once all 6 guesses used
                print("You lose, you did not guess the word in 6 guesses.")


main()