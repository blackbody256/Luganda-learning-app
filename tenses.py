import random

tense = ['Nzanya in far past', 'Nzanya in near past', 'Nzanya in very near past', 'ngamba in far future', 'ngamba in very near past', 'ngamba in near past', 'mbuulira in near past',
         'mbuulira in very near past', 'mbuulira in far past','mbeera in very near past', 'mbeera in near past', 'mbeera in near future','ntegeeza in very near past', 'ntegeeza in near past',
         'nsinza in very near past', 'nsinza in near past', 'nsinza in far future', 'nfugga in very near past', 'nfugga in near past', 'nfugga in far past', 'nsoma in very near past',
         'nsoma in near past', 'nsoma in far past', 'nkuba in very near past', 'nkuba in near past', 'nkuba in far past', 'ngenda in very near past', 'ngenda in near past', 'ngenda in far past']

#stem ending in -la or -ra longer than 4 words becomes -dde
#stem ending in -da, -ga, -ja or -la or -ra becomes -ze
#-ka or -ta becomes -se, if consonant before final a is a double. modified ending also takes double z or s

def tenses1():
    print(*options, sep="/n")
    print("Type terms or help")
    choice = input()
    while choice not in("terms","help"):
        print("Type terms or help")
        choice = input()
    if choice == "vocab":
        print("okay we'll practice terms")
        gameplay1()
    elif choice == "help":
        print("'class 2 contains the word friend, trees, parts of the body, things and abstract concepts like year and more. Singular is (o)mu and plural is (e)mi'")



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

        def tenses2():
                random_question = random.choice(tense)
        print(random_question)
        if random_question == tense[0]:
            term = 'nazanya'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[1]:
            term = 'nazanye'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')

        if random_question == tense[2]:
            term = 'nzanye'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[3]:
            term = 'ndigamba'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[4]:
            term = 'ngambye'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[5]:
            term = 'nagambye'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[6]:
            term = 'nabuulidde'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[7]:
            term = 'mbuulidde'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[8]:
            term = 'nabuulira'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[9]:
            term = 'mbaadde'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)


        if random_question == tense[10]:
            term = 'nabaadde'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[11]:
            term = 'njjakubeera'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[12]:
            term = 'ntegezeza'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[13]:
            term = 'nategezeza'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[14]:
            term = 'nsinziza'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[15]:
            term = 'nasinziza'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[16]:
            term = 'ndisinza'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[17]:
            term = 'nfuze'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[18]:
            term = 'nafuze'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[19]:
            term = 'nafugga'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[20]:
            term = 'nsomye'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[21]:
            term = 'nasomye'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[22]:
            term = 'ndisoma'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[23]:
            term = 'nkubye'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[24]:
            term = 'nakubye'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[25]:
            term = 'nakuba'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[26]:
            term = 'ngenze'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[27]:
            term = 'nagenze'
            answer=input()
            words= answer.split()

            if term in answer:
                    print('kitufu')
                    return(lives, score + 10, count + 1)
            else:
                    print('oli mukyamu')
                    return(lives - 1, score, count + 1)

        if random_question == tense[28]:
            term = 'nagenda'
            answer=input()
            words= answer.split()

            if term in answer:
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
tenses1()

        
