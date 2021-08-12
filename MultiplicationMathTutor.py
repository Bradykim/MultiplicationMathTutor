#Method called Math Tutor
#Ask user for number of questions
#Randomly generate that number of questions
#And have the user provide a response for each question
#Continually check the number of questions the user got correct
#At the end thank the user for playing and print the correct questions and the % correct

from random import randint as rand
from time import time as t

print('Multiplication Math Tutor')
def MathTutor():
    totalCorrect = 0
    totalTime = 0
    allQuestions = dict()
    numberQuestions = int(input('Please enter the number of questions you want asked: '))
    highestMultiple= int(input('Please specify the highest multiple: '))
    for index in range(int(numberQuestions)):
        randNum1 = rand(0,highestMultiple)
        randNum2 = rand(0,highestMultiple)
        correctAnswer = randNum1*randNum2
        t0= t()
        newQuestion = int(input(f'{randNum1}*{randNum2}= '))
        allQuestions[f'{randNum1}*{randNum2}'] = newQuestion
        if newQuestion == correctAnswer:
            totalCorrect+=1
        t1= t()
        totalTime += (t1-t0)
    percentCorrect = int((totalCorrect/numberQuestions)*100)
    print("Thank you for playing!")
    print(f'You got {totalCorrect} correct.')
    print(f'You got {percentCorrect}% correct.')
    print(f'This is your total time {totalTime} and this is your average time per question {totalTime/numberQuestions}.')
    print("Questions & Answers: ")
    for key in allQuestions:
        print(f'{key}= {allQuestions[key]}')

MathTutor()