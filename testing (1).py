#import the random module so can randomize questions
import random


#easy question
eq1 = ['the player runs on the field','that girl is cool','I am']

#medium question
mq1 = ['the big and strong player runs on the field','i have a good job']

#hard question
hq1 = ['the many players who are big and strong run together onto the field','my dad who is big and strong can pick up your dad']

#difficulty setting
dif = ['easy','medium','hard']

#options
options = ['Vocab','Sentences','Help']

#testing function
def class1():
    print(*options, sep="/n")
    print("Type vocab, sentences or help")
    #takes user input
    choice = input()
    #if user does not type one of the three options above then it will repeat
    while choice not in("vocab","sentences","help"):
        print("Type vocab, sentences or help")
        choice = input()
    if choice == "vocab":
        print("okay we'll practice vocabulary")
        game_mode()
    elif choice == "sentences":
        print("okay we'll practice sentences")
        game_mode()
    elif choice == "help":
        print("class 1")
        next

def game_mode():
    print("For class 1 we have 3 difficulty settings: easy, medium and hard")
    #print difficulty options from list 
    print(dif)
    #saves the settings so can be called in another def function
    global setting
    #take user input for difficulty 
    setting = input()
    while setting not in('easy','medium','hard'):
        print("Choose which difficulty you want to play")
        setting = input()
    if setting == "easy" or setting == "medium" or setting == "hard":
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
    #depending on which difficulty mode choosen, the program will display different lists
    if setting == "easy":
        random_question = random.choice(eq1)
        print(random_question)
    elif setting == "medium":
        random_question = random.choice(mq1)
        print(random_question)
    elif setting == "hard":
        random_question = random.choice(hq1)
        print(random_question)
        
    
    if random_question == eq1[0] or random_question == mq1[0] or random_question == hq1[0]:
        #term is the answers for each difficulty easy, medium, and hard
        term = {'the player runs on the field', 'the big and strong player runs on the field','the many players who are big and strong run together onto the field'}
        answer=input('>>> ').lower()
        words = answer.split()

        if answer in term:
            print('correct')
            return(lives, score + 10, count + 1)

        else:
            print('wrong')
            return(lives - 1, score, count + 1)
            
            

        print('Next question')

    if random_question == eq1[1] or random_question == mq1[1] or random_question == hq1[1]:
        #term is the answers for each difficulty easy, medium, and hard
        term = {'that girl is cool', 'i have a good job','my dad who is big and strong can pick up your dad'}
        answer=input('>>> ').lower()
        words = answer.split()

        if answer in term:
            print('correct')
            return(lives, score + 10, count + 1)

        else:
            print('wrong')
            return(lives - 1, score, count + 1)
            
            

        print('Next question')




#while everything is running
while(True):
    #sets the lives, score, mode and count in the def game_mode() function
    lives, score,mode,count, = game_mode()
    #while mode is lives and the lives are greater than 0 the game continues. If mode is score, the game checks that 3 questions have been answered and then ends the game 
    while (mode == "lives" and lives > 0) or (mode == "score" and count <= 3):
        #maps the lives,score,count from def game_mode() to the rquestion def function
        lives,score,count = rquestion(lives, score, count, mode)
    if mode == "lives":
        print(f"you ran out of ")
    else:
        print(f"Your final score was {score}")


