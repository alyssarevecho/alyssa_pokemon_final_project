import random

class PokemonQuiz():
    """
    Creates a class called Pokemon Quiz
    
    Instance Attributes
    -----------
    prompt : str 
        Question
    answer : str 
        Player's answer
    """
    def __init__(self, prompt, answer): # these are instance attributes
        self.prompt = prompt
        self.answer = answer