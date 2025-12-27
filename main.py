import quiz, certificate

while True:
    try:
        name = input("What is your name? ")
    except Exception as e:
        print(e)
        continue
    else:
        break

q = quiz.load_questions()
score, total = quiz.run_quiz(q)

result = certificate.generate_certificate(name, score, total)

if result is True:
    print("Thank you for playing!\t go to /certificates")
elif result is False:
    print("Sorry, you didn't answer correctly.\t try again")