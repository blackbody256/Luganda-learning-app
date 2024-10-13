import random

sentences1 = ['After coffee, they can eat lunch', 'First in the morning', 'They eat two or three times',
              'They don’t have time to eat breakfast', 'Greet the others', 'It is Mr. Mukasa who is our teacher',
              'What kind of food do they eat?','Why do they eat at that hour?', 'These fruits are very bad / rotten',
              'This man is very wise']

sentences2 = ['andrew works hard', 'He/she went home to rest', 'He/she went to the store to buy a nice shirt', 'Tea with milk is tastier than tea without', 'andrew is best at working than all others',
              'I am going to return on tuesday', 'do they have enough funds']

#andrew akola nnyo
#Yagenda ka kuwummula
#yagenze ku dduka okugula essati ennungi
#caayi w’amata asinga caayi omukalu okuwooma
#andrew akola okusinga abalala bonna
#n'genda kukomawo ku lwokubiri
#balina ensimbi ezimala
#embwa yetaaga kumira ddagala | the dog needs to take medicine
#you are lazy and need to go to work | oli mugayaavu era weetaaga okugenda kukola
#weetaga ssente za mmere |do you need money for food
# he has already gone, amaze okugenda

def sent():
    #print(*options, sep="/n")
    print("Type 1,2, or 3 for different sentences")
    choice = input()
    while choice not in("1","2","3"):
        print("Type 1,2, or 3 for different sentences")
        choice = input()
    if choice == "1":
        print("okay we'll practice sentences")
        gameplay()
    elif choice == "2":
        print("okay we'll practice sentences")
        gameplay()


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
        random_question = random.choice(sentences1)
        print(random_question)
    
    
        if random_question == questions1[0]:
            term = 'oluvannyuma lwa kaawa bayinza okulya ekyemisana'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == questions1[1]:
            term = 'okusooka ku makya'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == questions1[2]:
            term = 'balya emirundi ebbiri oba esatu'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == questions1[3]:
            term = 'tebalina kiseera kulya kyankya'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == questions1[4]:
            term = 'Mubuuzanga abalala'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == questions1[5]:
            term = 'Omwami Mukasa ye musomesa waffe'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == questions1[6]:
            term = 'balya mmere ya ngeri ki'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == questions1[7]:
            term = 'lwaki balya ku ssaawa eyo'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == questions1[8]:
            term = 'ebibala bino bivundu nnyo'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                return(lives, score + 10, count + 1)

            else:
                print('oli mukyamu')
                return(lives - 1, score, count + 1)

        if random_question == questions1[9]:
            term = 'omusajja ono mugezigezi nnyo'
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
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 10):
            lives,score,count = rquestion(lives, score, count, mode)
        if mode == "lives":
            print(f"you ran out of lives")
        else:
            print(f"Your final score was {score}")  


   
sent()

    



    

    




    


