#class6
import random

eq1 = ['my toe','my toes','your sign','your signs','her little girl','her little girls','our child','our children','their guest','their guests','your[pl] plastic',
       'your[pl] plastics','the knife is bad','the bad knife','the one toe','the toe is one','the chicken needs','the chickens need','this book','these books',
       'that school','those schools','that[far] gift','those[far] gifts']

mq1 = ['']

hq1 = ['']

neg = ['not walking is bad','not speaking is painful','not crying is very good']
#akayovu kange kagenda okulya my little elephant 
#akazzukulu ko keetaaga okuyamba 


#akabenji ke mmotoka




#oluvanyuma ngolokoka

#obutamanya bangi mubantu
  

#obuzibu bwange buli bumu |my problem is one
#obugaaga 
#diffculty setting
dif = ['easy','medium','hard','neg']

vocabulary = ['akaveera(plastic)','akabenje(accident)','kabuvubuka(adolescence)',
             'obulungi(goodness)','obuzibu(issues)',
             'obulwadde(disease)','obuto(childhood)','obugagga(wealth)',
             'obuwanguzi(success)','obukenuzi(corruption)','obukulu(age)',
              'obusungu','obubaka','obusobozi','obuyambi','obunyiivu','obwegassi']

questions1 = ['obutakola(inaction)']
options = ['Vocab','Sentences','Help']

def class6():
    print(*options, sep="/n")
    print("Type vocab, sentences or help")
    choice = input()
    while choice not in("vocab","sentences","help"):
        print("Type vocab, sentences or help")
        choice = input()
    if choice == "vocab":
        print("okay we'll practice vocabulary")
        gameplay()
    elif choice == "sentences":
        print("okay we'll practice sentences")
        gameplay1()
    elif choice == "help":
        print("Class 1 contains people and words that do not have a prefix. prefix is (o)mu and plural (a)ba")

def gameplay1():
    def game_mode():
        print("For class 6 we have 3 difficulty settings: easy, medium, hard and negatives")
        #print difficulty options from list 
        print(dif)
        #saves the settings so can be called in another def function
        global setting
        #take user input for difficulty 
        setting = input()
        while setting not in('easy','medium','hard','neg'):
            print("Choose which difficulty you want to play")
            setting = input()
        if setting == "easy" or setting == "medium" or setting == "hard" or setting == "neg":
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
        elif setting == "neg":
            random_question = random.choice(neg)
            print(random_question)
    
    
        if random_question == eq1[0] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akagere kange', '','','obutatambula bubi'}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[1] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[1]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'obugere bwange', '','','obutayogera buuluma'}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[2] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[2]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akabonero ko', '','','obutakaaba bulungi nnyo'}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[3] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'obubonero bwo', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[4] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akawala ke', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[5] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'obuwala bwe', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[6] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akaana kaffe', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[7] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'obwaana bwaffe', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[8] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akagenyi kaabwe', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[9] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'obugenyi bwabwe', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[10] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akaveera kaamwe', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[11] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'obuveera bwamwe', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[12] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akambe kabi', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[13] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akambe akabi', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[14] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akagere akamu', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[15] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akagere kali kamu', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[16] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akakoko keetaaga', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[17] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'obukoko bwetaaga', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[18] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akatabo kaakano', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[19] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'obutabo buubwo', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[20] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akasomero kaako', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[21] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'obusomero buubo', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[22] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'akarabo kaakali', '','',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[23] or random_question == mq1[0] or random_question == hq1[0] or random_question == neg[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'oburabo buubuli', '','',''}
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
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 20):
            lives,score,count = rquestion(lives, score, count, mode)
        if mode == "lives":
            print(f"you ran out of lives")
        else:
            print(f"Your final score was {score}")        

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
        random_question = random.choice(vocabulary)
        
    
    
        if random_question == vocabulary[0]:
            print('What is plastic?')
            print('(a)akaveera(b)akatungulu(c)akalevu(d)akabenje')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[1]:
            print('What is accident?')
            print('(a)akaveera(b)akatungulu(c)akakiiko(d)akabenje')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[2]:
            print('What is adolescence?')
            print('(a)akalevu(b)kabuvubuka(c)obulamu(d)akabenje')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[3]:
            print('What is goodness?')
            print('(a)obulungi(b)obukenuzi(c)obulwadde(d)obugaaga')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[4]:
            print('What is issues?')
            print('(a)obugaaga(b)akatungulu(c)obulungi(d)obuzibu')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[5]:
            print('What is disease?')
            print('(a)akaveera(b)akagere(c)obulwadde(d)akabonero')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[6]:
            print('What is childhood?')
            print('(a)obuto(b)akajanja(c)akalevu(d)akabenje')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[7]:
            print('What is wealth?')
            print('(a)akaveera(b)obugaaga(c)obuto(d)akabenje')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[8]:
            print('What is success?')
            print('(a)akaveera(b)akatungulu(c)akalevu(d)obuwanguzi')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[9]:
            print('What is corruption?')
            print('(a)obukenuzi(b)akatungulu(c)akalevu(d)akabenje')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[10]:
            print('What is age?')
            print('(a)akaveera(b)akatungulu(c)obukulu(d)akabenje')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[11]:
            print('What is anger?')
            print('(a)obukulu(b)obunene(c)obukulu(d)obusungu')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[12]:
            print('What is message?')
            print('(a)obubaka(b)obusungu(c)obukulu(d)obukenuzi')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[13]:
            print('What is ability?')
            print('(a)akatungulu(b)akatungulu(c)obusobozi(d)obuyambi')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[14]:
            print('What is assistance?')
            print('(a)obuwanguzi(b)obukenuzi(c)obukulu(d)obuyambi')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[15]:
            print('What is anger?')
            print('(a)obwenzi(b)obunyiivu(c)obukulu(d)akabenje')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[16]:
            print('What is union?')
            print('(a)obwegassi(b)akatungulu(c)obusungu(d)obukulu')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

    while(True):
        lives, score,mode,count, = game_mode()
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 20):
            lives,score,count = rquestion(lives, score, count, mode)
        if mode == "lives":
            print(f"you ran out of lives")
        else:
            print(f"Your final score was {score}")

class6()
