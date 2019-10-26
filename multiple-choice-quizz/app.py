#Simple question and answer program
from question import Question

#Create the questions
questions_prompts = [
    "What colors are the bananas?\n(a) Red\n(b) Green\n(c) Yellow\n\n",
    "What colors are the apples?\n(a) Blue\n(b) Red\n(c) Purple\n\n",
    "What color is the sky\n(a) Blue\n(b) Yellow\n(c) White\n\n"
]

#Create an array of questions objects with their question and answer
questions = [
    Question(questions_prompts[0], 'c'),
    Question(questions_prompts[1], 'b'),
    Question(questions_prompts[2], 'a')
]

#With the question and answer array, iterate and compare their answer against the user input
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {str(score)} of {str(len(questions))} correct")

run_test(questions)