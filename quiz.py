import json
import random
import time
from colorama import init, Fore, Style

init(autoreset=True)

def load_questions():

    # open questions
    with open ('data/questions.json', 'r') as file:
        questions = json.load(file)

    # randomize them
    random.shuffle(questions)

    return questions

def run_quiz(questions):

    if not questions:
        print(Fore.RED + 'No questions found.')
        return 0,0

    score = 0
    total = len(questions)

    # intro
    print(Fore.CYAN + Style.BRIGHT + "=" * 70)
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to Quizificate!")
    print(Fore.CYAN + Style.BRIGHT + "=" * 70)
    print(Fore.GREEN + "questions are about programming languages")
    print(Fore.MAGENTA + f"You must answer 70% questions from {total} questions.")
    print(Fore.CYAN + "-" * 70)
    time.sleep(5)

    # iterate questions
    for i, question in enumerate(questions, 1):

        # show details
        print(Fore.WHITE + Style.BRIGHT + f"Question {i}/{total}:\t", end="")
        time.sleep(0.5)
        print(Fore.YELLOW + question["question"])
        time.sleep(2)

        # options
        for option in question['options']:
            print(Fore.CYAN + option)
            time.sleep(0.5)

        # user input
        while True:
            try:
                inp = int(input(Fore.WHITE + Style.BRIGHT + 'Enter your choice: ' + Style.RESET_ALL))

                if not 1 <= inp <= 4:
                    print(Fore.RED + 'Invalid input.')
                    continue

                if inp == question['correct']:
                    score += 10
                    print(Fore.GREEN + Style.BRIGHT + 'Correct!\tyou earned 1 point!')
                else:
                    print(Fore.RED + Style.BRIGHT + 'Incorrect!')

            except Exception as e:
                print(Fore.RED + "Uncommon input: " + e)
                continue

            else:
                break

            finally:
                print(Fore.WHITE + Style.BRIGHT + f"Your scores: {score}")
                print(Fore.BLUE + "=" * 70)

    return score, total