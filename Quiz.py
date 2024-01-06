import time
import random
mark = 0
def FootballQuiz():
    global mark
    if mark > 0:
        mark = 0
    mydict = {
        1: "Who is the winner of the Champions League in 1992? ",
        2: "Who is the player who has won three World Cups? ",
        3: "How many clubs have achieved the historic sextuple? ",
        4: "Who is the first club achieved the Champions League? ",
        5: "Who is the most successful team in the World Cup? ",
        6: "Exit to main menu. "
    }
    number_of_question = 0
    while number_of_question != 6:
        print("Please enter the number of Question: ")
        for j in mydict.items():
            print(j)
        number_of_question = int(input())
        if number_of_question == 1:
            print("Please enter the answer: ")
            print(mydict[1])
            print("""A. Barcelona 
B. Real Madrid
C. Melan """)
            answer1 = input().lower()
            if answer1 == "a":
                print("Your answer is correct")
                mark += 1
            else:
                print("Your answer is wrong")
        if number_of_question == 2:
            print(mydict[2])
            print("Please enter the answer: ")
            print("""A. Messi
B. Maradona
C. Pele""")
            answer2 = input().lower()
            if answer2 == "c":
                print("Your answer is correct")
                mark += 1
            else:
                print("Your answer is wrong")
        if number_of_question == 3:
            print(mydict[3])
            print("Please enter the answer: ")
            print("""A. 1
B. 2
C. 3""")
            answer3 = input().lower()
            if answer3 == "b":
                print("Your answer is correct")
                mark += 1
            else:
                print("You answer is wrong")
        if number_of_question == 4:
            print(mydict[4])
            print("Please enter the answer: ")
            print("""A. Real Madrid 
B. Ajax
C. Barcelona""")
            answer4 = input().lower()
            if answer4 == "a":
                print("Your answer is correct")
                mark += 1
            else:
                print("You answer is wrong")
        if number_of_question == 5:
            print(mydict[5])
            print("Please enter the answer: ")
            print("""A. Germany 
B. Italy 
C. Brazil""")
            answer5 = input().lower()
            if answer5 == "c":
                print("Your answer is correct")
                mark += 1
            else:
                print("You answer is wrong")
        if number_of_question == 6:
            print(f"Your result is {mark}, its {result()}")
def PythonQuiz():
    global mark
    if mark > 0:
        mark = 0
    mydict = {
        1: "What is the lambda function? ",
        2: "What is the map function? ",
        3: "Is mytuple = (1) valid definition of tuple? ",
        4: "In the arbitrary arguments the function will receive the tuple of arguments? ",
        5: "The append() function used to insert value in the end of the dictionary? ",
        6: "Exit to main menu. "
    }
    number_of_question = 0
    while number_of_question != 6:
        print("Please enter the number of Question: ")
        for j in mydict.items():
            print(j)
        number_of_question = int(input())
        if number_of_question == 1:
            print("Please enter the answer: ")
            print(mydict[1])
            print("""A. Anonymous function in one line code 
B. Anonymous function in multi line codes """)
            answer1 = input().lower()
            if answer1 == "a":
                print("Your answer is correct")
                mark += 1
            else:
                print("Your answer is wrong")
        if number_of_question == 2:
            print(mydict[2])
            print("Please enter the answer: ")
            print("""A. Function returns a list of those elements that return True when evaluated by the lambda function
B. Maps every item in the input iterable to the corresponding item in the output iterable""")
            answer2 = input().lower()
            if answer2 == "b":
                print("Your answer is correct")
                mark += 1
            else:
                print("Your answer is wrong")
        if number_of_question == 3:
            print(mydict[3])
            print("Please enter the answer: ")
            print("""A. True 
B. False""")
            answer3 = input().lower()
            if answer3 == "b":
                print("Your answer is correct")
                mark += 1
            else:
                print("You answer is wrong")
        if number_of_question == 4:
            print(mydict[4])
            print("Please enter the answer: ")
            print("""A. True 
B. False""")
            answer4 = input().lower()
            if answer4 == "a":
                print("Your answer is correct")
                mark += 1
            else:
                print("You answer is wrong")
        if number_of_question == 5:
            print(mydict[5])
            print("Please enter the answer: ")
            print("""A. True 
B. False""")
            answer5 = input().lower()
            if answer5 == "b":
                print("Your answer is correct")
                mark += 1
            else:
                print("You answer is wrong")
        if number_of_question == 6:
            print(f"Your result is {mark}, its {result()}")
def PalestineQuiz():
    global mark
    if mark > 0:
        mark = 0
    mydict = {
        1: "Where is the Ibrahimi Mosque located? ",
        2: "What borders Palestine from the south? ",
        3: "What is Jenin famous for? ",
        4: "What is the Canaanite name for the city of Nablus? ",
        5: "What is called the city of Jericho? ",
        6: "Exit to main menu. "
    }
    number_of_question = 0
    while number_of_question != 6:
        print("Please enter the number of Question: ")
        for j in mydict.items():
            print(j)
        number_of_question = int(input())
        if number_of_question == 1:
            print("Please enter the answer: ")
            print(mydict[1])
            print("""A. Nablus
B. Hebron
C. Safed""")
            answer1 = input().lower()
            if answer1 == "b":
                print("Your answer is correct")
                mark += 1
            else:
                print("Your answer is wrong")
        if number_of_question == 2:
            print(mydict[2])
            print("Please enter the answer: ")
            print("""A. Gulf of Aqaba
B. Negev desert
C. Beersheba""")
            answer2 = input().lower()
            if answer2 == "a":
                print("Your answer is correct")
                mark += 1
            else:
                print("Your answer is wrong")
        if number_of_question == 3:
            print(mydict[3])
            print("Please enter the answer: ")
            print("""A. Citrus fruits
B. Grapes
C. Watermelon """)
            answer3 = input().lower()
            if answer3 == "c":
                print("Your answer is correct")
                mark += 1
            else:
                print("You answer is wrong")
        if number_of_question == 4:
            print(mydict[4])
            print("Please enter the answer: ")
            print("""A. Yurshalim
B. The eye of the gardens
C. Shechem""")
            answer4 = input().lower()
            if answer4 == "c":
                print("Your answer is correct")
                mark += 1
            else:
                print("You answer is wrong")
        if number_of_question == 5:
            print(mydict[5])
            print("Please enter the answer: ")
            print("""A. Moon City
B. The fog city
C. beauty City""")
            answer5 = input().lower()
            if answer5 == "a":
                print("Your answer is correct")
                mark += 1
            else:
                print("You answer is wrong")
        if number_of_question == 6:
            print(f"Your result is {mark}, its {result()}")
def result():
    global mark
    if mark == 5:
        return "Excellent"
    if 5 > mark >= 3:
        return "Very Good"
    else:
        return "Bad"
def main():
    print("Hello")
    time.sleep(1)
    print("How are you?")
    time.sleep(1)
    print("You have three short quizzes")
    time.sleep(1)
    print("You have to choose the quiz you want")
    time.sleep(1)
    print("Since each test contains ten circles, you can select the number of circles you want to answer")
    time.sleep(1)
    choise = 0
    while choise != 4:
        print("What quiz do you want?")
        print("""You have three quizzes:
    1. Football Quiz.
    2. Python Quiz.
    3. Palestine Quiz.
    4. Exit""")
        time.sleep(1)
        choise = int(input())
        if choise == 1:
            FootballQuiz()
        if choise == 2:
            PythonQuiz()
        if choise == 3:
            PalestineQuiz()
        if choise == 4:
            print("Good Bye ")
main()