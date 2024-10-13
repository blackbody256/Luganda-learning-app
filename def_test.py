
import random
import tkinter as tk
import keyboard 
from verb_def import * #import from other file
#from sentences1 import * 
from tkinter import messagebox
from tkinter import *

questions1 = ['the player runs on the field', 'my child is suffering because of a snake bite'
              ,'I have a strong desire to become a singer', 'my child ran away from home', 'this jackfruit is delicious', 'this person is tall',
             'my small child doesnt eat meat', 'my short guest is bad', 'neighbor','omuwanguzi','he came to save all people','that boy likes fighting alot',
              ]

questions2 = ['this arm of mine is small', 'the mattresses needs to be cleaned', 'this tree is short', 'my friends are coming', 'the body needs to sleep',
              'trees benefit from water', 'please share this salt', 'my habits are very good']

questions3 = ['this goat sleeps', 'this elephant of mine is going','your ants are tall',
             'this atm doesnt work', 'these chicken eat alot','meat','nose', 'I mop those ants', 'my cow likes to laugh','your mistakes are bad' ]

questions4 = ['our village is where?', 'the book that you gave me is bad', 'that bowl is white'
             ,'these two good bowls of mine','show me the four short banana fiber', 'my dreams fortell the future']

questions5 = ['this land needs to be cut', 'these bananas are very good',
             'My stone is very tall','voice','banana','eye','medicine']

verbs = ['doubts','next','trust','sick of/fed up','hide something','fail/not allow',
         'save','think','fight','explain','avoid','exert oneself','refuse','take away / remove','throw',
         'hide','converse','be quite / shut up','hope','start'] 

def help_event(event):
    messagebox.showinfo("Class 1","Class 1 contains people and words that do not have a prefix. prefix is (o)mu and plural (a)ba")
root = tk.Tk()
root.geometry("150x150")
root.bind('h', help_event)
tk.mainloop()


       
def rquestion():
        random_question = random.choice(questions1)
        print(random_question)
        if random_question == questions1[0]:
            term = 'omusambi adduka ku kissawe'
            answer=input()
            words = answer.split()

            if term in answer.lower():
                print('kitufu')
                
            else:
                print('oli mukyamu')
                
                
        if random_question == questions1[1]:
            term='omwana wange abonaabona lwamusota kumubojja'
            question=input()
            words = question.split()

            if term in question.lower():
                print('kitufu')
                
            else:
                print('oli mukyamu')
        
        
        if random_question == questions1[2]:
            term='neegomba okufuuka omuyimbi' or 'nnina eegomba okufuuka omuyimbi'
            question=input()
            words = question.split()

            if term in question.lower():
                print('kitufu')
                
    
            else:
                print('oli mukyamu')
                
        if random_question == questions1[3]:
            term='abaana wange yabaama okuva ewaka'
            question=input()
            words = question.split()

            if term in question.lower():
                print('kitufu')
                
    
            else:
                print('oli mukyamu')
                
        if random_question == questions1[4]:
            term='fenna eno awooma'
            question=input()
            words = question.split()

            if term in question.lower():
                print('kitufu')
                
    
            else:
                print('oli mukyamu')

        if random_question == questions1[5]:
            term='omuntu ono muwaanvu'
            question=input()
            words = question.split()

            if term in question.lower():
                print('kitufu')
               
    
            else:
                print('oli mukyamu')

        if random_question == questions1[6]:
            term='omwana omutono talya ekyama'
            question=input()
            words = question.split()

            if term in question.lower():
                print('kitufu')
               
    
            else:
                print('oli mukyamu')

        if random_question == questions1[7]:
            term='omugenyi wange omumpi mubi'
            question=input()
            words = question.split()

            if term in question.lower():
                print('kitufu')
               
    
            else:
                print('oli mukyamu')

        if random_question == questions1[8]:
            print('What is neighbor?')
            print('(a)omujaasi(b)munnabyabufuzi(c)omulirwana(d)omufumbo')
            question=input()
            if question == 'c':
                print('kitufu')
            else:
                print('oli mukyamu')

        if random_question == questions1[9]:
            print('What is winner?')
            print('(a)omuwanguzi(b)munnabyabufuzi(c)omulirwana(d)omufumbo')
            question=input()
            if question == 'a':
                print('kitufu')
            else:
                print('oli mukyamu')

        if random_question == questions1[10]:
            term='yajja kulokola abantu bonna'
            question=input()
            words = question.split()

            if term in question.lower():
                print('kitufu')
               
    
            else:
                print('oli mukyamu')

        if random_question == questions1[11]:
            term='omulenzi oyo ayagala nnyo okulwana'
            question=input()
            words = question.split()

            if term in question.lower():
                print('kitufu')
               
    
            else:
                print('oli mukyamu')
        print('Next question')
        rquestion()


        
def rquestion1():
        print('class 2 contains the word friend, trees, parts of the body, things and abstract concepts like year and more. Singular is (o)mu and plural is (e)mi')
        random_question = random.choice(questions2)
        print(random_question)
        if random_question == questions2[0]:
            term = 'omukono gwange guno mutono'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions2[1]:
            term = 'emifaliso gyetaaga okuwoza'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions2[2]:
            term = 'omuti guno mumpi'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions2[3]:
            term = 'miwano gyange gijja'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions2[4]:
            term = 'omubiri gwetaaga okwebaka'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')
        print('Next question')

        if random_question == questions2[5]:
            term = 'amazzi gagasa emiti'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')
        print('Next question')

        if random_question == questions2[6]:
            term = 'omunnyo guno mwattu mugugabane'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')
        print('Next question')

        if random_question == questions2[7]:
            term = 'emize gyange mirungi nnyo'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')
        print('Next question')
        rquestion1()

def rquestion2():
        print('class 3 contains mainly things and animals, but also contains close to all foreign words. Singular and plural are same but the prefixes change. Characterized by -En')
        random_question = random.choice(questions3)
        print(random_question)
        if random_question == questions3[0]:
            term = 'embuzi eno yeebaka'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')
                
        if random_question == questions3[1]:
            term = 'enjovu yange eno egenda'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions3[2]:
            term = 'ensawa yo mpaanvu'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions3[3]:
            term = 'ATM eno eganye okukola'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions3[4]:
            term = 'enkoko zino zirya nnyo'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions3[5]:
            term = 'ente yange eyagala okueseka'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions3[6]:
            term = 'ensobi zo mbi '
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')
        print('Next question')
        rquestion2()

def rquestion3():
        random_question = random.choice(questions4)
        print(random_question)
        if random_question == questions4[0]:
            term = 'ekyaalo kyamwe kiri wa'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions4[1]:
            term = "ekitabo ky'ompadde kibi"
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions4[2]:
            term = 'ekibiya ekyo kyeru'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        
        if random_question == questions4[3]:
            term = 'ebibya byange bino ebirungi ebibiri' 
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        if random_question == questions4[4]:
            term = "ndaga ebyayi ebina ebimpi"
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        print('Next question')
        rquestion3()

def rquestion4():
        random_question = random.choice(questions5)
        print(random_question)
        if random_question == questions5[0]:
            term = 'Ettaka lino lyeetaga okusala'
            answer=input()
            words = answer.split()

            if term in answer:
                print('kitufu')
                
            else:
                print('oli mukyamu')

        
        
def verbs1():
        global score
        global correct
        global count
        

        
        if count == 25:
                print('All done. You answered:',correct)
                exit()
        
        
        
        random_question = random.choice(verbs)
        print(random_question)
        if random_question == verbs[0]:
                print('What is doubts?')
                print('(a)buusabuusa (b)lunda (c)mila (d)nunula')
                count +=1
                answer=input()
                if answer == 'a':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')
                        

        if random_question == verbs[1]:
                #next
                print('(a)copa (b)dduka (c)ddako (d)buuka')
                count +=1
                answer=input()
                if answer == 'c':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')
                        

        if random_question == verbs[2]:
                #trust
                print('(a)copa (b)eesiga (c)ddugala (d)yingira')
                count +=1
                answer=input()
                if answer == 'b':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[3]:
                #be sick of/fed up
                print('(a)zimbe (b)fumitiriza (c)fuga (d)eetamwa')
                count +=1
                answer=input()
                if answer == 'd':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[4]:
                #hide something
                print('(a)kweka (b)kosa (c)kuuma (d)kuwa')
                count +=1
                answer=input()
                if answer == 'a':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                        
                else:
                        print('oli mukyamu')

        if random_question == verbs[5]:
                #fail/not allow
                print('(a)weyongerayo (b)londa (c)buuza (d)lemesa')
                count +=1
                answer=input()
                if answer == 'd':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[6]:
                #save
                print('(a)kendeeza (b)lokola (c)tegeeza (d)jjukira')
                count +=1
                answer=input()
                if answer == 'b':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[7]:
                #think
                print('(a)kyuusa (b)lowooza (c)tegeera (d)baawo')
                count +=1
                answer=input()
                if answer == 'b':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[8]:
                #fight
                print('(a)lwana (b)tegeka (c)wulira (d)lowooza')
                count +=1
                answer=input()
                if answer == 'a':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[9]:
                #explain
                print('(a)lemesa (b)lokola (c)sinza (d)nnyonyola')
                count +=1
                answer=input()
                if answer == 'd':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[10]:
                #avoid
                print('(a)kulakulana (b)tegeka (c)eewala (d)nnyonyola')
                count +=1
                answer=input()
                if answer == 'c':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[11]:
                #exert oneself
                print('(a)fuba (b)kumatiza (c)eewala (d)tera')
                count +=1
                answer=input()
                if answer == 'a':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[12]:
                #refuse
                print('(a)teekwa (b)gaana (c)kozesa (d)nyumya')
                count +=1
                answer=input()
                if answer == 'b':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[13]:
                #take away / remove
                print('(a)buuka (b)gaana (c)salawo (d)ggya')
                count +=1
                answer=input()
                if answer == 'd':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[14]:
                #throw
                print('(a)faayo (b)ggya (c)bwama (d)kasuka')
                count +=1
                answer=input()
                if answer == 'd':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[15]:
                #hide
                print('(a)tandika (b)lokola (c)kisa (d)kasuka')
                count +=1
                answer=input()
                if answer == 'c':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[16]:
                #converse
                print('(a)nyumya (b)labira(c)kisa (d)kulakulana')
                count +=1
                answer=input()
                if answer == 'a':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[17]:
                #be quite / shut up
                print('(a)sanyusa (b)okwegendereza(c)sirika (d)bwama')
                count +=1
                answer=input()
                if answer == 'c':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[18]:
                #hope
                print('(a)fuuka (b)suubira(c)funa (d)gabana')
                count +=1
                answer=input()
                if answer == 'b':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')

        if random_question == verbs[19]:
                #start
                print('(a)tandika (b)eegomba(c)eeyanze (d)kuza')
                count +=1
                answer=input()
                if answer == 'a':
                        print('kitufu')
                        
                        score = score + 100
                        print('your score is:',score)
                        correct +=1
                else:
                        print('oli mukyamu')
                
                
        verbs1()       

        
        
         
print('omusajja ono alabika(appears), ')
print('what class do you want?')




score=0
count=0
correct=0






choice=int(input())
if choice == 1:
    rquestion()
elif choice == 2:
    rquestion1()
elif choice == 3:
    rquestion2()
elif choice == 4:
    rquestion3()
elif choice == 5:
        verbs1()
elif choice == 6:
        verbs2()
elif choice == 7:
        verbs4()
#elif choice == 8:
        #s1()

        
