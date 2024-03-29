questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is attributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What IS Earth even?..."]
]


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------")
        print(key)

        for i in options[question_num-1]:
            print(i)

        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("\nCorrect!")
        return 1
    else:
        print("\nWrong!")
        return 0


def display_score(correct_guesses, guesses):
    print("-------------------")
    print("RESULTS:")
    print("-------------------\n")

    print("Correct Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Your Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print()
    print("Your final score is: " + str(score) + "%")


def play_again():
    response = input("Do you want to play again? (Y/N): ").lower()
    if response != "yes" and response != "y":
        return False
    else:
        return True


new_game()
while play_again():
    new_game()

print("Bye!")


