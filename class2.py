#class2
import random
eq1 = ['our friend','our friends','this year','these jobs','the tree is green','the green tree','the big tree','the tree is big','his tax','his taxes','their year','their years',
       'my head','my heads','your blood','his bread','the friend has','the friends have']

       #'one heart','two hearts','three hearts','the arms are long','the bodies are short',
       #'the job is short','the short job','the long arms','the short bodies']

mq1 = [ 'your heart is big','these trees are big','this game is short','this bread is delicious','that job is bad','the many big heads', 'the friends have their taxes',
        'the friend has his taxes','blood is red']

hq1 = ['this arm of mine is small', 'the mattresses needs to be cleaned', 'this tree is short', 'my friends are coming', 'the body needs to sleep',
              'trees benefit from water', 'please share this salt', 'my habits are very good', 'this tall tree grows','','','','','','','','','','','']

#emigaso gyaffe girina 
#emiti egyo minene



#'omukono gwange guno mutono'
#emifaliso gyetaaga okuwoza'
#'omuti guno mumpi'
#'mikwano gyange gijja'
#'omubiri gwetaaga okwebaka'
#amazzi gagasa emiti'
#'omunnyo guno mwattu mugugabane'
#'emize gyange mirungi nnyo'
#'omuti guno omuwaanvu gukula'

#diffculty setting
dif = ['easy','medium','hard']

vocabulary = ['omutima','omusaayi','omuze','omukolo','omugaso','omwezi','omuwendo','oumzizo','omuzannyo']

options = ['Vocab','Sentences','Help']

def class2():
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
        print("'class 2 contains the word friend, trees, parts of the body, things and abstract concepts like year and more. Singular is (o)mu and plural is (e)mi'")




def gameplay():
    def game_mode():
        print("For class 2 we have 3 difficulty settings: easy, medium and hard")
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
            term = {'omukwano gwaffe ', 'omutima gwo munene',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
            
                
                
        if random_question == eq1[1]  or random_question == mq1[1] or random_question == hq1[1]:
            term= {'emikwano gyaffe', 'emiti gino mirungi',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[2]  or random_question == mq1[2] or random_question == hq1[2]:
            term= {'omwaka guno', 'omuzannyo guno mumpi',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[3]  or random_question == mq1[3] or random_question == hq1[3]:
            term= {'emirimu gino', 'omugatti guno guwooma',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[4]  or random_question == mq1[4] or random_question == hq1[4]:
            term= {'omuti gwa kiragala', 'omulimu ogwo mubi',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[5]  or random_question == mq1[5] or random_question == hq1[5]:
            term= {'omuti ogwa kiragala', 'emitwe eminene mingi',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[6]  or random_question == mq1[6] or random_question == hq1[6]:
            term= {'omuti omunene', 'emikwano girina emisolo gyabwe',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[7]  or random_question == mq1[7] or random_question == hq1[1]:
            term= {'omuti munene', 'omukwano gulina emisolo gye',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[8]  or random_question == mq1[8] or random_question == hq1[2]:
            term= {'omusolo gwe', 'omusaayi mumyufu',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[9]  or random_question == mq1[3] or random_question == hq1[3]:
            term= {'emisolo gye', '',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[10]  or random_question == mq1[4] or random_question == hq1[4]:
            term= {'omwaka gwabwe', '',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[11]  or random_question == mq1[5] or random_question == hq1[5]:
            term= {'emyaka gyabwe', '',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[12] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'omutwe gwange', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
            
                
                
        if random_question == eq1[13]  or random_question == mq1[1] or random_question == hq1[1]:
            term= {'emitwe gyange', '',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[14]  or random_question == mq1[2] or random_question == hq1[2]:
            term= {'omusaayi gwo', '',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[15]  or random_question == mq1[3] or random_question == hq1[3]:
            term= {'omugaati gwe', '',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[16]  or random_question == mq1[4] or random_question == hq1[4]:
            term= {'omukwano gulina', '',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[17]  or random_question == mq1[5] or random_question == hq1[5]:
            term= {'emikwano girina', '',''} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)




            

            print('Next question')
    while(True):
        lives, score,mode,count, = game_mode()
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 15):
            lives,score,count = rquestion(lives, score, count, mode)
        if mode == "lives":
            print(f"you ran out of lives")
        else:
            print(f"Your final score was {score}")    

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
        
    
    
        if random_question == vocabulary[0]:
            print('What is heart?')
            print('(a)omuwanguzi(b)omukolo(c)omutima(d)omutwe')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[1]:
            print('What is blood?')
            print('(a)omusaayi(b)omukolo(c)oumzizo(d)omusege')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[2]:
            print('What is habit?')
            print('(a)omuze(b)omuzira(c)omutima(d)omugaati')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[3]:
            print('What is function?')
            print('(a)omuwanguzi(b)omukolo(c)omusuwo(d)omugongo')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[4]:
            print('What is benefit?')
            print('(a)omuwanguzi(b)omukolo(c)omuwendo(d)omugaso')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[5]:
            print('What is month?')
            print('(a)omwezi(b)omukolo(c)omuti(d)omutwe')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[6]:
            print('What is amount?')
            print('(a)omuwanguzi(b)omukolo(c)omutima(d)omuwendo')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[7]:
            print('What is heart?')
            print('(a)omuwanguzi(b)omukolo(c)omutima(d)omutwe')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[8]:
            print('What is taboo?')
            print('(a)omulambo(b)omuzizo(c)omuzira(d)omutwe')
            answer=input()
            if answer == 'c':
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

class2()


