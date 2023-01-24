"""
    Number guessing game involving three digits and the clues "Pico" (correct digit but wrong position), "Fermi" (correct digit and position), and "Bagels" (nothing correct)
    Filename: morris_project1.py
    Author: Beckett Morris
    Date: 01/08/2023
    Course: COMP 1352-3
    Assignment: Project 1 - A Guessing Game (called Pico Fermi Bagels)
    Collaborators: None
    Internet Source: None
"""


from random import randint


"""
    Checks for duplicate digits
    parameters: numbers (string of three digits)
    return: boolean True (duplicates exist) or False (no duplicates)
"""
def check_duplicates(numbers):
    previous = []
    for num in numbers:  #loops through string, checking for duplicates by comparing with previously unique digits in 'previous'
        if num in previous:
            return True
        previous.append(num)  #appended only if unique
    return False


"""
    Compares two strings to determine if digits are in the correct place (Fermi!), correct but in the wrong place (Pico!), or wholly incorrect (Bagels!);
        adds these words to a list according to the place of the digit they refer to;
        joins the list items into a string to be returned
    parameters: answer (string of three digits), guess (string of three digits)
    return: output (string)
"""
def compare(answer, guess):
    results = []
    for i in range(3):
        if guess[i] in answer:
            if guess[i] == answer[i]:  #guessed digit is in correct place
                results.insert(i, "Fermi!")
            else:  #guessed digit is not in correct place but still present in answer
                results.insert(i, "Pico!")
    if len(results) == 0:  #no Fermi!'s or Pico!'s have been inserted into 'results', meaning no correctly placed or guessed digits
        results.append("Bagels!")
    return " ".join(results)


"""
    Generates an answer using 'choose_numbers';
        prompts continual guesses from the user until solved, tracks the number of tries,
        checks that there are no duplicate digits in the user's guess with 'check_duplicates';
        prints resulting clues from 'compare' and determines if solved
    parameters: None
    return: None
"""
def main():
    repeating_answer = True
    while repeating_answer == True:  #loop used to create answer of 3 unique digits
        answer = "".join([str(randint(0,9)), str(randint(0,9)), str(randint(0,9))])  #joins list of three random digits [0, 9] into string
        if check_duplicates(answer) == False:  #if no repeat digits in answer
            repeating_answer = False  #stops future iterations of while loop
    tries = 0
    solved = False
    while solved == False:  #following commands occur continually while unsolved
        guess = input("What is your guess? ")
        if check_duplicates(guess) == False:  #checks that the guess is valid (no duplicates)
            tries += 1
            result = compare(answer, guess)
            print(result)
            if result == "Fermi! Fermi! Fermi!":  #checks that answer is solved (Fermi! Fermi! Fermi!)
                solved = True  #stops future iterations of while loop
                print("You got it in " + str(tries) + " guesses!")
        else:
            print("Invalid guess - duplicate digits not allowed")


main()