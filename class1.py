
import random



eq1 = ['this person','these people','that person','those people','my child','my children','your baby','your babies','his helper','his helpers',
       'our grandchild','our grandchildren','your[pl] enemy','your[pl] enemies','their buyer','their buyers','one idiot','two idiots','the ruler of buganda','the rulers of buganda']

mq1 = ['the player runs on the field', 'the small child doesnt eat meat','our politicians are bad','the soldiers walk far', 
       'my short guest is bad', 'father and mother went to the store','your girl goes to school','his neighbor is very wise','their good doctor', 'their good doctors',
       'the workers play soccer','this person is big']

hq1 = ['my child is suffering because of a snake bite','I have a strong desire to become a singer','my child ran away from home','our queen is good and strong','this superstar will buy sugar',
       'that singer is very beautiful','your girl is very beautiful','this man cuts the big tree','he came to save all people']

# abagenyi bange abampi babi
#'that boy likes fighting alot'
#omulenzi n'omusajja basimba omuti omutono

#diffculty setting
dif = ['easy','medium','hard']

vocabulary = ['winner','neighbor','nannyini','enemy(omulabe)','omukulu(adult)',
              'attendant(omuweereza)','baby(omuwere)','beggar(omusabi)','builder(omuzimbi)',
              'bully(omujoozi)','buyer(omuguzi)', 'defendant omuwawaabirwa', 'dependant omuwereza',
              'disciple omuyigirizwa', 'distributor omugabuzi', 'elder n., omukadde',
              'foreigner omunnagwanga','grandchild omuzzukulu','guard n., omukuumi',
              'helper omubeezi', 'idiot omusiru', 'instructor omuyigiriza', 'judge n., omulamuzi',
              'liar omulimba', 'listener omuwulizi', 'nephew omujjwa', 'nurse n.omujjanjabi',
              'reader omusomi', 'rival n., omuvuganyi','ruler omufuzi', 'runner omuddusi', 'saviour omulokozi',
              'secretary omuwandiisi', 'staff omuggo','twin omulongo','tyrant omujoozi','waiter omuweerbza',
              'warrior omulwanyi','witness omujulirwa','youth omuvubuka']

options = ['Vocab','Sentences','Help']

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
        gameplay1()
    elif choice == "sentences":
        print("okay we'll practice sentences")
        gameplay()
    elif choice == "help":
        print("Class 1 contains people and words that do not have a prefix. prefix is (o)mu and plural (a)ba")




def gameplay():
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
            term = {'omuntu ono', 'omusambi adduka ku kissawe','omwana wange abonaabona lwamusota kumubojja'}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
            
                
                
        if random_question == eq1[1]  or random_question == mq1[1] or random_question == hq1[1]:
            term= {'omuntu bano', 'omwana omutono talya ekyama','neegomba okufuuka omuyimbi'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
        
        if random_question == eq1[2]  or random_question == mq1[2] or random_question == hq1[2]:
            term= {'omuntu oyo','bannabyabufuzi baffe babi', 'omwana wange yabaama okuva ewaka'}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[3] or random_question == mq1[3] or random_question == hq1[0]:
            term= {'abantu abo','abajaasi batambula wala'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[4] or random_question == mq1[4] or random_question == hq1[0]:
            term={'omuwana wange','omugenyi wange omumpi mubi',} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[5]  or random_question == mq1[5] or random_question == hq1[0]:
            term={'abawana bange','taata ne mamma bagenze ku dduka'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[6] or random_question == mq1[6] or random_question == hq1[0]:
            term={'omuwere wo','omuwala wo agenda kusommero'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[7] or random_question == mq1[7] or random_question == hq1[0]:
            term={'abawere bo','omulirwana we mugezi nnyo'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

 

        if random_question == eq1[8] or random_question == mq1[8] or random_question == hq1[0]:
            term={'omubeezi we','omusawo waabwe omulungi','yajja kulokola abantu bonna'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
            

        if random_question == eq1[9] or random_question == mq1[9] or random_question == hq1[0]:
            term={'ababeezi be','abasawo baabwe abalungi','omusajja ono attema omuti omunene'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
            


        if random_question == eq1[10] or random_question == mq1[10] or random_question == hq1[0]:
            term={'omuzzukulu waffe','abakozi bazannya omupiira'}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[11]  or random_question == mq1[1] or random_question == hq1[1]:
            term= {'abazzukulu baffe', 'omwana omutono talya ekyama','neegomba okufuuka omuyimbi'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
        
        if random_question == eq1[12]  or random_question == mq1[2] or random_question == hq1[2]:
            term= {'omulabe waamwe','bannabyabufuzi baffe babi', 'omwana wange yabaama okuva ewaka'}
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[13] or random_question == mq1[3] or random_question == hq1[0]:
            term= {'abalabe baamwe','abajaasi batambula wala'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[14] or random_question == mq1[4] or random_question == hq1[0]:
            term={'omuguzi waabwe','omugenyi wange omumpi mubi',} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[15]  or random_question == mq1[5] or random_question == hq1[0]:
            term={'abaguzi baabwe','taata ne mamma bagenze ku dduka'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[16] or random_question == mq1[6] or random_question == hq1[0]:
            term={'omusiru omu','omuwala wo agenda kusommero'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == eq1[17] or random_question == mq1[7] or random_question == hq1[0]:
            term={'abasiru bbiri','omulirwana we mugezi nnyo'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

 

        if random_question == eq1[18] or random_question == mq1[8] or random_question == hq1[0]:
            term={'omufuzi wa buganda','omusawo waabwe omulungi','yajja kulokola abantu bonna'} 
            answer=input('>>> ').lower()
            words = answer.split()

            if answer in term:
                print('kitufu')
                return(lives, score + 10, count + 1)
    
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
            

        if random_question == eq1[19] or random_question == mq1[9] or random_question == hq1[0]:
            term={'abafuzi ba buganda','abasawo baabwe abalungi','omusajja ono attema omuti omunene'} 
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
            print('What is winner?')
            print('(a)omuwanguzi(b)munnabyabufuzi(c)omulirwana(d)omufumbo')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[1]:
            print('What is neighbor?')
            print('(a)omujaasi(b)omukozi(c)omulirwana(d)omuwala')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[2]:
            print('What is owner')
            print('(a)ssukaali(b)nannyini(c)omusomesa(d)omufumbi')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[3]:
            print('What is enemy')
            print('(a)ssukaali(b)nannyini(c)omukulu(d)omulabe')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[4]:
            print('What is adult?')
            print('(a)omukulu(b)munnabyabufuzi(c)omulirwana(d)omufumbo')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[5]:
            print('What is attendant?')
            print('(a)omujaasi(b)omukozi(c)omuweereza(d)omuwala')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[6]:
            print('What is baby')
            print('(a)ssukaali(b)omuwere(c)omusomesa(d)omufumbi')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[7]:
            print('What is beggar')
            print('(a)ssukaali(b)nannyini(c)omusabi(d)omufumbi')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[8]:
            print('What is builder?')
            print('(a)omuzimbi(b)munnabyabufuzi(c)omulirwana(d)omufumbo')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[9]:
            print('What is bully?')
            print('(a)omujaasi(b)omukozi(c)omujoozi(d)omuwala')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[10]:
            print('What is buyer')
            print('(a)ssukaali(b)omuguzi(c)omusomesa(d)omufumbi')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[11]:
            print('What is dependant')
            print('(a)ssukaali(b)omuwereza(c)omusomesa(d)omufumbi')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[12]:
            print('What is disciple?')
            print('(a)omuyigirizwa(b)munnabyabufuzi(c)omulirwana(d)omufumbo')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[13]:
            print('What is distributor?')
            print('(a)omujaasi(b)omukozi(c)omugabuzi(d)omuwala')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[14]:
            print('What is elder')
            print('(a)ssukaali(b)omukadde(c)omusomesa(d)omufumbi')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[15]:
            print('What is foreigner')
            print('(a)ssukaali(b)omuwereza(c)omusomesa(d)omunnagwanga')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[16]:
            print('What is grandchild?')
            print('(a)omuzimbi(b)munnabyabufuzi(c)omulirwana(d)omuzzukulu')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[17]:
            print('What is guard?')
            print('(a)omujaasi(b)omukozi(c)omukuumi(d)omuwala')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[18]:
            print('What is buyer')
            print('(a)ssukaali(b)omuguzi(c)omusomesa(d)omufumbi')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[19]:
            print('What is helper')
            print('(a)ssukaali(b)omubeezi(c)omusomesa(d)omufumbi')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[20]:
            print('What is idiot?')
            print('(a)omusiru(b)munnabyabufuzi(c)omulirwana(d)omufumbo')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[21]:
            print('What is instructor?')
            print('(a)omujaasi(b)omukozi(c)omuyigiriza(d)omuwala')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[22]:
            print('What is judge')
            print('(a)ssukaali(b)omulamuzi(c)omusomesa(d)omufumbi')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[23]:
            print('What is liar')
            print('(a)ssukaali(b)omuwereza(c)omusomesa(d)omulimba')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
 
        if random_question == vocabulary[24]:
            print('What is listener?')
            print('(a)omulokozi(b)omuvubuka(c)omuwulizi(d)ssebo')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[25]:
            print('What is nephew')
            print('(a)kabaka(b)omujjwa(c)omulenzi(d)omwana')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[26]:
            print('What is nurse')
            print('(a)omulabe(b)omuyizi(c)omufumbo(d)omujjanjabi')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[27]:
            print('What is reader?')
            print('(a)omusomi(b)katonda(c)omwami(d)omuzadde')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[28]:
            print('What is rival?')
            print('(a)omulwanyi(b)omuwere(c)omuvuganyi(d)omujaasi')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[29]:
            print('What is ruler')
            print('(a)caayi(b)omufuzi(c)kawo(d)omuwandiisi')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[30]:
            print('What is runner')
            print('(a)jjaja(b)nannyini(c)omuddusi(d)omulokozi')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[31]:
            print('What is saviour?')
            print('(a)omulokozi(b)munnabyabufuzi(c)omuggo(d)muganda')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[32]:
            print('What is secretary?')
            print('(a)omukozi(b)omujaasi(c)omuwandiisi(d)omusambi')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[33]:
            print('What is buyer')
            print('(a)kawo(b)omuguzi(c)omusomesa(d)omulabi')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[34]:
            print('What is dependant')
            print('(a)omukadde(b)omuwereza(c)omugabuzi(d)omujjwa')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[35]:
            print('What is disciple?')
            print('(a)omuyigirizwa(b)munnabyabufuzi(c)omulokozi(d)omuvuganyi')
            answer=input()
            if answer == 'a':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)
#
        if random_question == vocabulary[36]:
            print('What is distributor?')
            print('(a)omuyigirizwa(b)omubeezi(c)omugabuzi(d)omuwulizi')
            answer=input()
            if answer == 'c':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[37]:
            print('What is elder')
            print('(a)omusabi(b)omukadde(c)omusomesa(d)omulimba')
            answer=input()
            if answer == 'b':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[38]:
            print('What is foreigner')
            print('(a)omujjwa(b)omuwereza(c)nannyini(d)omunnagwanga')
            answer=input()
            if answer == 'd':
                print('kitufu')
                return(lives, score + 10, count + 1)
            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == vocabulary[39]:
            print('What is grandchild?')
            print('(a)omukadde(b)omulamuzi(c)omuvuganyi(d)omuzzukulu')
            answer=input()
            if answer == 'd':
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

class1()

