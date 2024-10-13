#class10
import random

questions10 = ['im tired','the water is good']

vocabulary = ['otulo','otuzzi','otuta',
              'otuzi']

options = ['Vocab','Sentences','Help']

def class10():
    print(*options, sep="/n")
    print("Type vocab, sentences or help")
    choice = input()
    while choice not in("vocab","sentences","help"):
        print("Type vocab, sentences or help")
        choice = input()
    if choice == "vocab":
        print("okay we'll practice vocabulary")
        gameplay1()
    elif choice == "sentences":
        print("okay we'll practice sentences")
        gameplay()
    elif choice == "help":
        print("very small class. contains abstract concepts like sleep and small drops of liquid")

def gameplay():
    def game_mode():
        print("Do you want to play with lives or score? L or S?")
        typ = input()
        while typ not in ("L","S"):
            print("Do you want to play with lives or score? L or S?")
            typ = input()
        if typ == "L":
            print("Okay we'll play lives")
            return(3,0,"lives",0)
        elif typ == "S":
            print("Okay try to get the highest score")
            return (0,0,"score",0)
        

    def rquestion(lives, score, count, mode ):
        random_question = random.choice(questions9)
        print(random_question)
    
    
        if random_question == questions10[0]:
            term = 'otulo tunnuma'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == questions10[1]:
            term = 'otuzzi tulungi'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
        

     

    while(True):
        lives, score,mode,count, = game_mode()
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 5):
            lives,score,count = rquestion(lives, score, count, mode)
        if mode == "lives":
            print(f"you ran out of lives")
        else:
            print(f"Your final score was {score}")
            return(lives - 1, score, count + 1)
        
def gameplay1():
    def game_mode():
        print("Do you want to play with lives or score? L or S?")
        typ = input()
        while typ not in ("L","S"):
            print("Do you want to play with lives or score? L or S?")
            typ = input()
        if typ == "L":
            print("Okay we'll play lives")
            return(3,0,"lives",0)
        elif typ == "S":
            print("Okay try to get the highest score")
            return (0,0,"score",0)

    def rquestion(lives, score, count, mode ):
        random_question = random.choice(vocabulary)
        print(random_question)
    
    
        if random_question == vocabulary[0]:
            print('What is sleep?')
            print('(a)otulo(b)okutu(c)otuzzi(d)okulonda')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[1]:
            print('What is small drop of water?')
            print('(a)okugulu(b)okutu(c)otuzzi(d)okulonda')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[2]:
            print('What is small drop of milk?')
            print('(a)otuzi(b)okutu(c)otuzzi(d)otuta')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[3]:
            print('What is small drop of feaces?')
            print('(a)otuzi(b)okulambula(c)okubala(d)okulonda')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        
    while(True):
        lives, score,mode,count, = game_mode()
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 3):
            lives,score,count = rquestion(lives, score, count, mode)
        if mode == "lives":
            print(f"you ran out of lives")
        else:
            print(f"Your final score was {score}")
class10()




