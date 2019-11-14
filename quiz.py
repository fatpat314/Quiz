
#If len(answerlist) > 3 print "YOU WIN" else "Better luck next time"
answerlist = []
correct_answer_list = []
#Question One
def space():
    print("----------------------------------------------------------------------")
def question_one():
    space()
    print("Are you ready for this quiz? Please enter 1 for Yes or 0 for No.")
    space()
    answer = input("Please enter 1 or 0: ")

    if answer == "1":
        answerlist.append("Question one: Correct!")
        correct_answer_list.append("1")
        print('Correct!')
        print(answerlist)
    elif answer == "0":
        answerlist.append("Question one: wrong")
        print('wrong')
        print(answerlist)

    else:
        question_one()

question_one()
space()

#Question Two
def question_two():
    print("What is the the scope of a veriable that can be accessed from any point of the code called?")
    space()
    print("A: Mobal\nB: Focal\nC: Global\nD: Colloquial\nE: Local")
    space()
    answer = input("Enter answer here: ")

    if answer == "A":
        answerlist.append("Question two: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "a":
        answerlist.append("Question two: wrong")
        print('wrong')
        print(answerlist)

    elif answer == "B":
        answerlist.append("Question two: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "b":
        answerlist.append("Question two: wrong")
        print('wrong')
        print(answerlist)

    elif answer == "C":
        answerlist.append("Question two: Correct!")
        correct_answer_list.append("2")
        print("Correct!")
        print(answerlist)
    elif answer == "c":
        answerlist.append("Question two: Correct!")
        correct_answer_list.append("2")
        print("Correct!")
        print(answerlist)

    elif answer == "D":
        answerlist.append("Question two: wrong")
        print("wrong")
        print(answerlist)
    elif answer == "d":
        answerlist.append("Question two: wrong")
        print("wrong")
        print(answerlist)

    elif answer ==  "E":
        answerlist.append("Question two: wrong")
        print("wrong")
        print(answerlist)
    elif answer ==  "e":
        answerlist.append("Question two: wrong")
        print("wrong")
        print(answerlist)

    else:
        question_two()

question_two()
space()

#Question Three
def question_three():
    print("Is this pseudocode?\nIf len(answerlist) > 3 print 'YOU WIN' else 'Better luck next time'")
    space()
    answer = input("Enter 1 for yes or 0 for no: ")

    if answer == "1":
        answerlist.append("Question three: wrong")
        print("wrong")
        print(answerlist)

    elif answer == "0":
        answerlist.append("Question three: Correct!")
        correct_answer_list.append("3")
        print("Correct!")
        print(answerlist)

    else:
        question_three()

question_three()
space()

#Question Four
def question_four():
    print("Objects in a dictionary contain what two elements?")
    space()
    print("A: Header and Footer\nB: Get and Post\nC: Getter and Setter\nD: Key and Value \nE: Action and Reaction")
    answer = input("Enter answer here: ")

    if answer == "A":
        answerlist.append("Question four: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "a":
        answerlist.append("Question four: wrong")
        print('wrong')
        print(answerlist)

    elif answer == "B":
        answerlist.append("Question four: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "b":
        answerlist.append("Question four: wrong")
        print('wrong')
        print(answerlist)

    elif answer == "C":
        answerlist.append("Question four: wrong")
        print("wrong")
        print(answerlist)
    elif answer == "c":
        answerlist.append("Question four: wrong")
        print("wrong")
        print(answerlist)

    elif answer == "D":
        answerlist.append("Question four: Correct!")
        correct_answer_list.append("4")
        print("Correct!")
        print(answerlist)
    elif answer == "d":
        answerlist.append("Question four: Correct!")
        correct_answer_list.append("4")
        print("Correct!")
        print(answerlist)

    elif answer ==  "E":
        answerlist.append("Question four: wrong")
        print("wrong")
        print(answerlist)
    elif answer ==  "e":
        answerlist.append("Question four: wrong")
        print("wrong")
        print(answerlist)

    else:
        question_four()
question_four()
space()

# question_five
def question_five():
    print("What is a concatenation error?")
    space()
    print("A: When you misspell a veriable\nB: When you try to divide by zero\nC: When you forget the colon then defining a function\nD: When you forget to indent\nE: When you try to add an integer to a string")
    space()
    answer = input("Enter answer here: ")

    if answer == "A":
        answerlist.append("Question four: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "a":
        answerlist.append("Question four: wrong")
        print('wrong')
        print(answerlist)

    elif answer == "B":
        answerlist.append("Question four: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "b":
        answerlist.append("Question four: wrong")
        print('wrong')
        print(answerlist)

    elif answer == "C":
        answerlist.append("Question four: wrong")
        print("wrong")
        print(answerlist)
    elif answer == "c":
        answerlist.append("Question four: wrong")
        print("wrong")
        print(answerlist)

    elif answer == "D":
        answerlist.append("Question four: wrong")
        print("wrong")
        print(answerlist)
    elif answer == "d":
        answerlist.append("Question four: wrong")
        print("wrong")
        print(answerlist)

    elif answer ==  "E":
        answerlist.append("Question four: Correct!")
        correct_answer_list.append("5")
        print("Correct!")
        print(answerlist)
    elif answer ==  "e":
        answerlist.append("Question four: Correct!")
        correct_answer_list.append("5")
        print("Correct!")
        print(answerlist)

    else:
        question_five()
question_five()
