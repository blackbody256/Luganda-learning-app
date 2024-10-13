#class3
import random

eq1 = ['your shoe','your shoes','her mistake','his mistakes','my house','my houses','their monkey','their chairs','our border','our meats',
       'the dog is big','the big dog','the elephant is little','the little elephant','the dust is bad','the rain has','the winds have','the nose is good',
       'one lion','the yellow giraffe','the yellow giraffes']
       #,'the ant is going','two tomatoes',
       #'the ants are going','two countries']

mq1 = ['this goat sleeps', 'this elephant of mine is going','your giraffes are tall','this atm doesnt work', 'these chicken eat alot',
       'my cow likes to laugh','your mistakes are very bad','those shoes are big and good',
       'cats are better than dogs','the monkey has a small plate','the plate of the elephant']


hq1 = ['']

vocabulary = ['meat', 'nose','engatto','ensobi','emundu','essowani','entugga','enkima',
              'ennyaanya','ensi','ensalo','enswaswa','empuliziganya','ssente','kkapa',
              'ssaati','poliisi']

#'I mop those ants
#embizi yaabwe
#embizi zaabwe
#ensobi yo
#'the dog is dressing'
#when the dust is going'
#embwa eyambala
#
#
#'communications is important'

options = ['Vocab','Sentences','Help']

#diffculty setting
dif = ['easy','medium','hard']

def class3():
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
        print("class 3 contains mainly things and animals, but also contains close to all foreign words. Singular and plural are same but the prefixes change. Characterized by -En")




def gameplay():
    def game_mode():
        print("For class 3 we have 3 difficulty settings: easy, medium and hard")
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
            term = {'engatto yo', 'embuzi eno yeebaka',''}
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
            term = {'engatto zo', 'enjovu yange eno egenda',''}
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
            term = {'ensobi ye', 'entugga zo ziwaanvu',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[3] or random_question == mq1[3] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'ensobi ze', 'ATM eno eganye okukola',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[4] or random_question == mq1[4] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'ennyumba yange', 'enkoko zino zirya nnyo',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[5] or random_question == mq1[5] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'ennyumba zange', 'ente yange eyagala okueseka',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[6] or random_question == mq1[6] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'enkima yaabwe', 'ensobi zo mbi nnyo',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[7] or random_question == mq1[7] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'entebe zaabwe', 'engatto ezo nnene era nnungi',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[8] or random_question == mq1[8] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'ensalo yaffe', 'kkapa zisinga embwa',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[9] or random_question == mq1[9] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'ennyama zaffe', 'enkima erina essowaani enntono',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[10] or random_question == mq1[10] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'embwa nnene', "essowaani y'enjovu",''}
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
            term = {'embwa ennene', '',''}
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
            term = {'enjovu ntono', '',''}
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
            term = {'enjovu entono', '',''}
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
            term = {'enfuufu mbi', '',''}
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
            term = {'enkuba erina', '',''}
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
            term = {'empewo zirina', '',''}
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
            term = {'ennyindo nnungi', '',''}
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
            term = {'empologoma emu', '',''}
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
            term = {'entuuga ya kyenvu', '',''}
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
            term = {'entuuga za kyenvu', '',''}
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
        print(random_question)
    
    
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
            


    while(True):
        lives, score,mode,count, = game_mode()
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 3):
            lives,score,count = rquestion(lives, score, count, mode)
        if mode == "lives":
            print(f"you ran out of lives")
        else:
            print(f"Your final score was {score}")

class3()



