import random
questions = ["What is the capital of France?", "What is 2+2?"]
answers = ["Paris", "4"]
for i in range(len(questions)):
    print(questions[i])
    user = input("Your answer: ")
    if user == answers[i]:
        print("You got it! ")
    else:
        print("try again")

