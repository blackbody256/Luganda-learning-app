import random

verbs1 = ['mislead','self control','hate','make laugh','should','last',
          'pleased with / approve / grateful','open','lift',
          'carry','join / add','be lazy','patience / endurance','discipline',
          'break','be annoyed / angry','fun','stay put / remain','first'
          ,'name','survive','examine / look carefully','reply to / answer / do again / start again / repeat'
          ,'tempt']
verbs3 = ['punish','go round','unity / coming together'
          ,'carry','prepare for','compare','represent','bring something back','warn'
          ,'order / command','inspect','bring to or for someone','lie / cheat','bite / sting / hurt','hurt someone',
          'pay','say goodbye to','be better than / defeat / overcome / more / most','be possible',
          'enable','promise','prepare / schedule / get ready','annoy','set up','increase']

score=0
count=0
correct=0

#emirembe - calm, peace, quite
def verbs2():


    random_question = random.choice(verbs1)
    print(random_question)
        
    if random_question == verbs1[0]:
        #mislead
        print('(a)buzabuza (b)sanidde (c)kuza (d)fanana')
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            
        else:
            print('oli mukyamu')
                
            
    if random_question == verbs1[1]:
        #self control
        print('(a)situla (b)kakasa (c)kuza (d)eefuga')
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            
        else:
            print('oli mukyamu')
                
            
    if random_question == verbs1[2]:
        #hate
        print('(a)funa (b)kyawa (c)gonjoola (d)eefuga')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
            
        else:
            print('oli mukyamu')

    if random_question == verbs1[3]:
        #make laugh
        print('(a)osesa (b)eeyanze (c)fuuka (d)buzabuza')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[4]:
        #should
        print('(a)fanana (b)situla (c)fuuka (d)sanidde')
        count +=1
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[5]:
        #last
        print('(a)gezaako (b)senguka (c)sembayo (d)sanidde')
        count +=1
        answer=input()
        if answer== 'c':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[6]:
        #pleased with / approve / grateful
        print('(a)siima (b)kaaba (c)sembayo (d)sanidde')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[7]:
        #open
        print('(a)gezaako (b)sumulula (c)kyawa (d)kaaba')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[8]:
        #lift

        print('(a)situla (b)senguka (c)sembayo (d)yimuka')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')


    if random_question == verbs1[9]:
        #carry

        print('(a)eetikka (b)siima (c)eefuga (d)gonjoola')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[10]:

        #join / add
        print('(a)buusabuusa (b)sumulula (c)Okuddirila (d)bonaabona')
        count +=1
        answer=input()
        if answer== 'c':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[11]:
        #be lazy
        print('(a)kuba (b)sumulula (c)gatta (d)gayaala')
        count +=1
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[12]:
        #patience/ endurance
        print('(a)ddamu (b)gumiikiriza (c)gatta (d)kyuusa')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[13]:
        #discipline
        print('(a)senguka (b)gumiikiriza (c)kangabula (d)eewala')
        count +=1
        answer=input()
        if answer== 'c':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[14]:
        #break
        print('(a)menya (b)kasuka (c)kangabula (d)keera')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[15]:
        #be annoyed / angry
        print('(a)menya (b)nyiiga (c)kangabula (d)eeyanze')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[16]:
        #fun
        print('(a)menya (b)kendeeza (c)labula (d)nyuma')
        count +=1
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[17]:
        #stay put / remain
        print('(a)osesa (b)sigala (c)sanga (d)nyuma')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[18]:
        #first
        print('(a)menya (b)sanyuka (c)mala (d)sooka')
        count +=1
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[19]:
        #name
        print('(a)teekwa (b)tunda (c)tuuma (d)tera')
        count +=1
        answer=input()
        if answer== 'c':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[20]:
        #survive
        print('(a)wonawo (b)tegeka (c)tuuma (d)sooka')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[21]:
        #examine / look carefully
        print('(a)wagira (b)eetegereza (c)sumulula (d)teganya')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[22]:
        #reply to / answer / do again / start again / repeat
        print('(a)dda (b)ddamu (c)buuka (d)wandiika')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs1[23]:
        #tempt
        print('(a)kema (b)ddamu (c)bonereza (d)seefuga')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    while(True):
        lives, score,mode,count, = game_mode()
        while (mode == "lives" and lives > 0) or (mode == "score" and count <= 3):
            lives,score,count = verbs2(lives, score, count, mode)
        if mode == "lives":
            print(f"you ran out of lives")
        else:
            print(f"Your final score was {score}")

def verbs4():

    global score
    global correct
    global count

    if count == 25:
                print('All done. You answered:',correct)
                exit()
                
    random_question = random.choice(verbs3)
    print(random_question)
    if random_question == verbs3[0]:
        #punish
        print('(a)bonereza (b)kema (c)kuza (d)wonawo')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[1]:
        #go round
        print('(a)bonereza (b)eetooloola (c)sigala (d)ddako')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[2]:
        #unity / coming together
        print('(a)wandiika (b)eetooloola (c)eegata (d)menya')
        count +=1
        answer=input()
        if answer== 'c':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[3]:
        #carry
        print('(a)copa (b)eesiga (c)eegata (d)eetikka')
        count +=1
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[4]:
        #prepare for
        print('(a)wandiika (b)eetegekera (c)eegata (d)eetikka')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[5]:
        #compare
        print('(a)fuula (b)eetegekera (c)geerageeranya (d)fumitiriza')
        count +=1
        answer=input()
        if answer== 'c':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[6]:
        #represent
        print('(a)kiikirira (b)gatta (c)funa (d)gaana')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[7]:
        #bring something back
        print('(a)kweka (b)lwana (c)geerageeranya (d)komyawo')
        count +=1
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[8]:
        #warn
        print('(a)kiikirira (b)eetooloola (c)labula (d)gaba')
        count +=1
        answer=input()
        if answer== 'c':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[9]:
        #order / command
        print('(a)gula (b)lagira (c)gayaala (d)komyawo')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[10]:
        #inspect
        print('(a)ggala (b)lagira (c)labula (d)lambula')
        count +=1
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[11]:
        #bring to or for someone
        print('(a)kakasa (b)leetera (c)lokola (d)kisa')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[12]:
        #lie / cheat
        print('(a)limba (b)bwama (c)kendeeza (d)zimbe')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[13]:
        #bite / sting / hurt
        print('(a)limba (b)lowooza (c)labula (d)luma')
        count +=1
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[14]:
        #hurt someone
        print('(a)limba (b)lumye (c)labula (d)luma')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[15]:
        #pay
        print('(a)sasula (b)lumye (c)sanyuka (d)sanyusa')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[16]:
        #say goodbye to
        print('(a)siibula (b)lumye (c)labula (d)luma')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[17]:
        #be better than / defeat / overcome / more / most
        print('(a)siibula (b)eewala (c)singa (d)fuba')
        count +=1
        answer=input()
        if answer== 'c':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[18]:
        #be possible
        print('(a)tera (b)funa (c)singa (d)soboka')
        count +=1
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[19]:
        #enable
        print('(a)siibula (b)sobozesa (c)singa (d)soboka')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[20]:
        #promise
        print('(a)suubiza (b)nnyonyola (c)lemesa (d)soboka')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[21]:
        #prepare / schedule / get ready
        print('(a)gaana (b)sobozesa (c)teekateeka (d)buuza')
        count +=1
        answer=input()
        if answer== 'c':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[22]:
        #annoy
        print('(a)suubiza (b)sobozesa (c)ddugala (d)teganya')
        count +=1
        answer=input()
        if answer== 'd':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[23]:
        #set up
        print('(a)teekateeka (b)yimuka (c)yongera (d)bonereza')
        count +=1
        answer=input()
        if answer== 'b':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')

    if random_question == verbs3[24]:
        #increase
        print('(a)yongera (b)yimuka (c)singa (d)teganya')
        count +=1
        answer=input()
        if answer== 'a':
            print('kitufu')
            score = score + 100
            print('your score is:',score)
            correct +=1
        else:
            print('oli mukyamu')
verbs4()
