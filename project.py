from fpdf import FPDF
from datetime import date
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

def generate_certificate(name, score, total):

    today = date.today().strftime("%d/%m/%Y")

    if score < (7 * total): # 70% of total points
        return False
    elif score > (10 * total) or score < 0 or not score:
        return None

    if not name:
        return None

    if not total:
        return None

    name = name.capitalize()

    pdf = FPDF("L", "mm", "A4")
    pdf.add_page()
    pdf.image("./assets/background.jpg", x=0, y=0, w=297)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "", 14)
    pdf.text(12, 12, today)

    pdf.set_text_color(0, 0, 0)

    pdf.set_font("Times", "B", 40)
    pdf.set_xy(0, 55)
    pdf.cell(297, 20, "Certificate", align="C")

    pdf.set_font("Times", "", 18)
    pdf.set_xy(0, 90)
    pdf.cell(297, 10, "This certifies that", align="C")

    pdf.set_font("Times", "B", 18)
    pdf.set_xy(0, 105)
    pdf.cell(297, 10, name, align="C")

    pdf.set_font("Times", "", 18)
    pdf.set_xy(0, 125)
    pdf.cell(297, 10, "has successfully completed the Quiz by score", align="C")

    pdf.set_font("Times", "B", 18)
    pdf.set_xy(0, 140)
    pdf.cell(297, 10, f"{score}/{total * 10}", align="C")

    pdf.set_font("Times", "", 18)
    pdf.set_xy(0, 175)
    pdf.cell(297, 10, "be successful", align="C")

    try:
        pdf.output(f"certificates/{name}_cirtificate.pdf")
    except Exception as e:
        return e
    else:
        return True


def main():

    while True:
        try:
            name = input("What is your name? ")
        except Exception as e:
            print(e)
            continue
        else:
            break

    q = load_questions()
    score, total = run_quiz(q)

    result = generate_certificate(name, score, total)

    if result is True:
        print("Thank you for playing!\t go to /certificates")
    elif result is False:
        print("Sorry, you didn't answer correctly.\t try again")

if __name__ == "__main__":
    main()