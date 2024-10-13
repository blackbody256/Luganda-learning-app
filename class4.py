#class4
import random

eq1 = ['her secret','her secrets','your moment','your moments','my thing','my things',
       'their night','their nights','your[pl] village','your[pl] villages','whose book?','whose books',
       'the forest needs','the forests needs','one word','the one word','four cups','the four cups',
       
       'the classroom is little','the little class room','the classrooms are little','the little classrooms',
       'the insect is big','the big insect','the insects are big','the big insects'
       'the opinion is bad','the bad opinion','the opinions are bad','the bad opinions'
       'the present is good','the good present','the presents are good','the good presents',
       'the sugar cane is delicious','the delicious sugar cane','the sugar canes are delicious','the delicious sugar canes',
       'the bed is long','the long bed','the beds are long','the long beds',
       'the building is small','the small building','the buildings are small','the small buildings',
       'the picture is yellow','the yellow picture']
       #'our dream','our dreams','that bird','that[far] bird']

mq1 = ['our village is where?', 'the book that you gave me is bad', 'that bowl is white'
       ,'these two good bowls of mine','show me the four short banana fiber', 
        'his things are nice','that gourd is small, mine is large','alberts book','where are your things','ask for their opinion']
hq1 = ['']

#'my dreams fortell the future',

vocab = []
#ekyaalo kyamwe kiri wa
#ekitabo ky'ompadde kibi
#ekibiya ekyo kyeru
#ebibya byange bino ebirungi ebibiri
#ndaga ebyayi ebina ebimpi
#ebintu bye birungi
#'ekita kino kitono, ekyange kinene
#ekitabo kya albert
#ebintu byo biri ludda wa
#saba ekirowoozo kyabwe

#diffculty setting
dif = ['easy','medium','hard']

options = ['Vocab','Sentences','Help']

def class4():
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
        print("class 3 contains mainly things and animals, but also contains close to all foreign words.")


def gameplay():
    def game_mode():
        print("For class 4 we have 3 difficulty settings: easy, medium and hard")
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
            term = {'ekyama kye', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[1] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'ebyama bye', '',''}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[2] or random_question == mq1[0] or random_question == hq1[0]:
            #term is the answers for each difficulty easy, medium, and hard
            term = {'ekiseera kyo', '',''}
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
            term = {'ebiseera byo', '',''}
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
            term = {'ekintu kyange', '',''}
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
            term = {'ebintu byange', '',''}
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
            term = {'ekiro kyabwe', '',''}
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
            term = {'ebiro byabwe', '',''}
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
            term = {'ekyalo kyamwe', '',''}
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
            term = {'ebyalo byamwe', '',''}
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
            term = {'ekitabo ky ani', '',''}
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
            term = {'ebitabo by ani', '',''}
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
            term = {'ekibira kyeetaaga', '',''}
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
            term = {'ebibira byeetaaga', '',''}
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
            term = {'ekigambo kimu', '',''}
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
            term = {'ekigambo ekimu', '',''}
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
            term = {'ebikopo bina', '',''}
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
            term = {'ebikopo ebina', '',''}
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
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 5):
            lives,score,count = rquestion(lives, score, count, mode)
        if mode == "lives":
            print(f"you ran out of lives")
        else:
            print(f"Your final score was {score}")
class4()
