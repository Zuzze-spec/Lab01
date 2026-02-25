import random


class Question:
    def __init__(self, text, difficulty, correct_answer, answer_choices=[]):
        self.text = text
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.answer_choices = answer_choices

    def randomify_options(self):
        random.shuffle(self.answer_choices) #shuffle è un'opzione della funzione random che mischia gli elementi di una lista
        return self.answer_choices