import random

MIN_NUMBER = 1
MAX_NUMBER = 10
NB_QUESTIONS = 5
NB_POINTS = 0 


def ask_question():

    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)

    answer_str = input(f"Quel est la réponse de {a} + {b} ?")
    answer_int = int(answer_str)

    if answer_int == a+b:
        return True
    return False



for i in range(0, NB_QUESTIONS):
    print(f"Question {i+1}")
    if ask_question():
        print("Réponse correcte")
        NB_POINTS += 1
    else:
        print("Réponse incorrecte")

print(f"Votre note est {NB_POINTS}/{NB_QUESTIONS}")

if NB_POINTS == int(NB_QUESTIONS):
    print("Vous êtes excellent")
elif NB_POINTS > float(NB_QUESTIONS) /2:
    print("Pas mal")
elif NB_POINTS == 0:
    print("You suck")