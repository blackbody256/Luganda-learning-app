from class1 import class1 #import from other file



lulist = ['Class 1','Class 2','Class 3','Class 4','Class 5', 'Class 6','Class 7',
           'Class 9', 'Class 10','Verbs','Sentences', 'Story']

def start():
    print('Welcome to the Luganda Language Program. Explore the options below')
    print(*lulist, sep = "\n")
    print('enter the number of any class you want or verbs, sentences or story')
    choice=input()
    while choice not in ('A','2','3','4','5','6','7'
                         ,'9','10','verbs','sentences','story'):
        print('enter the number of any class you want or verbs, sentences or story')
        choice=input()
    if choice == "A":
        print("Class 1")
        class1()
start()
