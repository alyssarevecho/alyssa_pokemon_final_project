"""A collection of functions for my project """


from classes import PokemonQuiz
from prompts import question_prompts
from answers import question_answers
import random
#from my_module.classes import PokemonQuiz
#from my_module.prompts import question_prompts
#from my_module.answers import question_answers

def poke_quiz(question_answers):
    """
    The questions for the quiz presented in a randomized order

    Parameters
    ----------
    question_answers: list
        The question's answers
    
    Return
    ------
    final_count : int
        Any integer from 0-10, including 10

    """
    #This shuffles the questions in a randomized order
    random.shuffle(question_answers)

    final_count = 0 #Will count how many questions the player gets correct
    
    for question in question_answers:
        
        answer = input(question.prompt).lower() #Makes the input from the player lowercase
    
        while answer not in ["a", "b", "c"]: #If the player inputs a letter that is not "a", "b" or "c", output invalid answer
            answer = input("Invalid answer choice. Pick from a to c:"). lower()
        
        if answer == question.answer:
            final_count = final_count + 1 #If the player gets a question correct, one point will be added and "You got that right!" will output
            print("You got that right!")
            
        else:
            print("That's incorrect.") #If the player gets a question wrong, the output will read "That's incorrect."
            
    print("You got " + str(final_count) + " right!")
    return final_count

def final_count_placement(final_count):
    """
    Sees where a player's final count lands
    
    Parameters
    ----------
    final_count : int
        The number of questions a player got right

    Returns
    -------
    outcome : str
        Three possible outcomes which are "You've got more training to do young grasshopper!" or
        "Youve got the basics, good job!" or "You sure are a pokemon master!"

    """
    outcome = ""
   
    if final_count == 0 or final_count == 1 or final_count == 2 or final_count == 3: #Will assign your score to a output message
        outcome = " You've got more training to do young grasshopper!"
    
    elif final_count == 4 or final_count == 5 or final_count == 6 or final_count == 7:
        outcome = " You've got the basics, good job!"
    
    elif final_count == 8 or final_count == 9 or final_count == 10:
        outcome = " You sure are a pokemon master!"
    
    return outcome


#run both of these functions together
def play_quiz(): #Quiz will play
    """
    This is the main function that runs the quiz game
    """
    print('Lets see how much you know about pokemon!')
    
    print('How many can you get correct?')
   
    play = poke_quiz(question_answers)
    
    return str(poke_quiz(question_answers)) + final_count_placement(play)