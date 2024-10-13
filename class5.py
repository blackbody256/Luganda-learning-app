
#class5
import random

eq1 = ['my name','my names','your nation','your nations','her teeth','her teeths',
    'our light','our lights','their voice','their voices',"daniel's school",
    "albert's schools",'freedom has','truth hurts','truth has','one family','one eye']

mq1 = ['my wound hurts alot','their family walks far','this nation is strong','milk is better','these bones of mine are old','not south but north']




hq1 =['this land needs to be cut', 'these bananas are very good','My stone is very little','this sweet banana is big but not good',
    'these eggs are delicious','my breast is hurting','this wound is hurting','this long bone','this bone is long']

vocabulary = ['voice','banana','eye','medicine','breast',
              'nation or tribe','law','freedom','bone',
              'light','heat','knee','window','wound',
              'joy','grass','truth','family or home',
              'milk','backwardness','north','south',
              'importance','news','birthday']

#ettaka lino lyeetaga okusala
#amenvu gano malungi
#ejinja lyange lino litono nnyo
#eryenvu lino linene naye si ddungi
#amagi gano gawooma
#ebbeere lyange linnuma
#ebbwa lino linuma
 #eggumba lino eddene
 #eggumba lino liwaanvu

#diffculty setting
dif = ['easy','medium','hard']
options = ['Vocab','Sentences','Help']

def class5():
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
        print("")

def gameplay():
    def game_mode():
        print("For class 5 we have 3 difficulty settings: easy, medium and hard")
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
            term = {'erinnya lyange', 'ebbwa lyange lunnuma nnyo',''}
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
            term = {'amannya gange', 'amaka gaabwe gatambula wala',''}
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
            term = {'eggwanga lyo', 'eggwanga lino lya maanyi',''}
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
            term = {'amawanga go', 'eggwanga lino lya maanyi',''}
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
            term = {'errinyo lye', '',''}
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
            term = {'amannyo ge', '',''}
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
            term = {'ettaala lyaffe', '',''}
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
            term = {'amataala gaffe', '',''}
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
            term = {'eddoboozi lyabwe', '',''}
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
            term = {'amaloboozi gaabwe', '',''}
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
            term = {'essomero lya daniel', '',''}
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
            term = {'amasomero ga albert', '',''}
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
            term = {'eddembe lirina', '',''}
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
            term = {'amazima galuma', '',''}
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
            term = {'amazima galina', '',''}
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
            term = {'amaka gamu', '',''}
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
            term = {'edinisa limu', '',''}
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
        
    
    
        if random_question == vocabulary[0]:
            print('What is voice?')
            print('(a)eddoboozi(b)eggwanga(c)eggumba(d)essanyu')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[1]:
            print('What is sweet banana?')
            print('(a)ettoke(b)ettaka(c)eryenvu(d)eriiso')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[2]:
            print('What is eye')
            print('(a)amaaso(b)eriiso(c)eddembe(d)ejjuni')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[3]:
            print('What is medicine')
            print('(a)eddagala(b)ebbaluwa(c)etteeka(d)eddembe')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[4]:
            print('What is breast')
            print('(a)eggumba(b)ebbaluwa(c)eggi(d)ebbeere')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
            
    

        if random_question == vocabulary[5]:
            print('What is nation or tribe')
            print('(a)amaloboozi(b)eggwanga(c)amakoloni(d)ebbwa')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
            
        if random_question == vocabulary[6]:
            print('What is law')
            print('(a)ebbwa(b)ettaka(c)etteeka(d)amaanyi')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[7]:
            print('What is freedom')
            print('(a)eddembe(b)amagye(c)eggwanga(d)ebbaluwa')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[8]:
            print('What is bone')
            print('(a)eddembe(b)eddoboozi(c)eddagala(d)eggumba')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[9]:
            print('What is light')
            print('(a)amaanyi(b)ettaala(c)amaaso(d)eggumba')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[10]:
            print('What is  heat')
            print('(a)amaanyi(b)amazaalibwa(c)ebbugumu(d)amata')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[11]:
            print('What is knee')
            print('(a)amaaso(b)evviivi(c)eddagala(d)ettooke')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[12]:
            print('What is window')
            print('(a)eddinisa(b)essanyu(c)ebbwa(d)eggumba')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[13]:
            print('What is wound')
            print('(a)essubi(b)amaloboozi(c)ekkubo(d)ebbwa')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[14]:
            print('What is joy')
            print('(a)amambuka(b)essuubi(c)amaka(d)essanyu')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[15]:
            print('What is grass')
            print('(a)eddinisa(b)essubi(c)amagye(d)amaduuka')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[16]:
            print('What is truth?')
            print('(a)amaka(b)amaserengeta(c)eddoboozi(d)amazima')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[17]:
            print('What is family or home?')
            print('(a)ettaala(b)amaalo(c)amaka(d)erinnya')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[18]:
            print('What is milk')
            print('(a)ejjuni(b)amata(c)eggi(d)ebbugumu')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[19]:
            print('What is backwardness')
            print('(a)amaalo(b)amakulu(c)ejjinja d)eddembe')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[20]:
            print('What is north')
            print('(a)eggumba(b)amaserengeta(c)amawulire(d)amabuka')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
            
    

        if random_question == vocabulary[21]:
            print('What is south')
            print('(a)amaloboozi(b)amaserengeta(c)amakoloni(d)amakulu')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
            
        if random_question == vocabulary[22]:
            print('What is importance')
            print('(a)essomero(b)erriso(c)amakulu(d)essuubi')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[23]:
            print('What is news')
            print('(a)amawulire(b)essanyu(c)amazima(d)amazzi')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[24]:
            print('What is birthday')
            print('(a)ebbeere(b)amagezi(c)amabuka(d)amazaalibwa')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

    

    while(True):
        lives, score,mode,count, = game_mode()
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 15):
            lives,score,count = rquestion(lives, score, count, mode)
        if mode == "lives":
            print(f"you ran out of lives")
        else:
            print(f"Your final score was {score}")

class5()




