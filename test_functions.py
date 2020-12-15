"""Tests for my functions"""

from classes import PokemonQuiz
from functions import poke_quiz, final_count_placement, play_quiz
from prompts import question_prompts
from answers import question_answers

#from my_module.classes import PokemonQuiz
#from my_module.function import cm_quiz, final_count_placement, play_quiz
#from my_module.prompts import question_prompts
#from my_module.answers import question_answers

def test_poke_quiz(): #This tests that the quiz is running 
    assert callable(poke_quiz)
    assert isinstance(poke_quiz(final_count) == int) 
    
def test_final_count_placement(): #This tests that the final score will output with the corresponding output message
    assert callable(final_count_placement)
    assert isinstance(final_count_placement(outcome)== str)
    assert isinstance(final_count_placement(1)== " You've got more training to do young grasshopper!")
    assert isinstance(final_count_placement(5)== " Youve got the basics, good job!")
    assert isinstance(final_count_placement(6)== " You sure are a pokemon master!")
    
def test_play_quiz():
    assert callable(play_quiz)
    assert isinstance((play_quiz()), str)