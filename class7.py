#class7
import random

eq1 = ['this proverb','these proverbs','that door','your song','your songs','her trip','her trips','my finger','my fingers','our meeting','our meetings',
       'the door is white','their cloth','their clothes','the big battle','the little skin','the hair is small','the day is bad','the bad day','the mountain is long','one meeting',
       "lubega's vacation"]

mq1 = ['your skin is very soft','your hair is not soft','the trip was long','his smell is so bad']

#olusu lwe lubi nnyo 
hq1 = ['']

vocabulary = ['olulimi','olusozi(mountain)','oluviiri(hair)',
              'olugero(proverb)','olukung"aana(meeting)','olusu(smell)','oluyimba(song)',
              'olunaku','olutalo(battle)','olugoye','olugendo(trip, hike)','olugalo(finger)',
              'olugambo(rumour)','oludda(direction)','oluwummula(vacation)','olususu(skin)',
              'olukiiko(meeting)']


#diffculty setting
dif = ['easy','medium','hard']

options = ['Vocab','Sentences','Help']

def class7():
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
        print("contains languages,body parts and all sorts of things")

def gameplay():
    def game_mode():
        print("For class 7 we have 3 difficulty settings: easy, medium and hard")
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
            term = {'olugero luno','olususu lwo lugonda nnyo',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[1] or random_question == mq1[1] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'engero zino','enviiri zo tezigonda',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[2] or random_question == mq1[2] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'olujji olwo', 'olugendo lubadde lwanvu',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[3] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'oluyimba lwo', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[4] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'ennyimba zo', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[5] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'olugendo lwe', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[6] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'engendo ze', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[7] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'olugalo lwange', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[8] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'engalo zange', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[9] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {"olukung'aana lyaffe", '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[10] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {"enkung'aana zaffe", '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[11] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'oluggi lweru', '',''}
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
            term = {'olugoye lwabwe', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[13] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'engoye zaabwe', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[14] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'olutalo olunene', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[15] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'olususu olutono', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[16] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'oluviiri lumpi', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[17] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'olunaku lubi', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[18] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'olunaku olubi', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[19] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'olusozi luwaanvu', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[20] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'olukiiko lumu', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[21] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'oluwummula lwa lubega', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)


        

     

    while(True):
        lives, score,mode,count, = game_mode()
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 10):
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
            print('What is language or tongue?')
            print('(a)olulimi(b)oludda(c)olugambo(d)olukung"aana')
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
class7()

