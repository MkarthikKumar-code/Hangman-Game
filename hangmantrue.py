print('                                    HANGMAN                          ' )
print()
print()
print('PROJECT DONE BY KARTHIK')
print()
z=input('Enter Your Name')

def hangman():
    
    import random
    import pickle
    h=random.randint(0,7)
    ch=random.randint(1,3)
    if ch==1:
        print()
        print("-->It is a car")
        print()
        s=['altroz','ecosport','rapid','endeavour','punto','phantom','elandra','accord']
        r=s[h]
    if ch==2:
        print()
        print("-->It is an animal")
        print()
        p=['leopard','rhinoceros','sloth','bison','lizard','jackel','camel','sambardeer']
        r=p[h]
    if ch==3:
        print()
        print("-->It is a fruit or vegetable")
        print()
        t=['watermelon','grape','raspberry','peach','lettuce','radish','spinach','broccoli']
        r=t[h]
    x=[]
    for i in range(1,len(r)):
        x.append(r[i])
        
    e=[]
    for i in range(len(r)):
        if i%7==0:
            print(r[i],end="")
            e.append(r[i])
        else:    
            print('_',end=" ")
            e.append(' ')

    s=[]
    for i in r:
        s.append(i)   
    t=[]
    global m
    m=7
    

    print()
    for j in range(20):
        print()   
       
        print("__________________")
        print() 
        k=input('Enter alphabet to be searched')
        print()
        if k in t:
            print()
            
            print('-->Alphabet already searched')
            continue
        t.append(k)
        print('-->Guesses already tried',t)
        if k in x:
         
            print()
            print('-->Found')
            print() 
            print('-->Number of chances left=',m)
            print()
            for i in range(1,len(r)):
                    if r[i]==k:
                        e[i]=k
            for i in e:
                if i==" ":
                    print("_",end=" ")
                else:
                    print(i,end=" ")       

        if k not in x:
           
            print()
            print('-->Not Found')
            m=m-1
            print()
            print('-->No of chances left=',m)
            print()
            for i in e:
                if i==' ':
                    print('_',end=" ")
                else:
                    print(i,end=" ")
            print()        
           
         
            if m==6:
                print() 
                print('  |====|')
                print('  O    |')
                print('       |')
                print('       |')
                print('       |')
                print('       |')
            if m==5:
                print() 
                print('  |====|')
                print('  O    |')
                print('  |    |')
                print('       |')
                print('       |')
                print('       |')
            if m==4:
                print() 
                print('  |====|')
                print('  O    |')
                print('  |    |')
                print('  |    |')
                print('       |')
                print('       |')
            if m==3:
                print() 
                print('  |====|')
                print('  O    |')
                print(' /|    |')
                print('  |    |')
                print('       |')
                print('       |')
            if m==2:
                print() 
                print('  |====|')
                print('  O    |')
                print(' /|\   |')
                print('  |    |')
                print('       |')
                print('       |')
            if m==1:
                print() 
                print('  |====|')
                print('  O    |')
                print(' /|\   |')
                print('  |    |')
                print('   \   |')
                print('       |')
            if m==0:
                print() 
                print('  |====|')
                print('  O    |')
                print(' /|\   |')
                print('  |    |')
                print(' / \   |')
                print('       |')
                print(' You LOST the game better luck next time')
                print()
                print('The correct word is',r)
                print()
                print()
                break
        if e==s:
            print()
            print()
            print('The word is',r,'u WON the game')
            print()
            break       
while True:
        print()
        print()
        print('press 1 For instructions to play')
        print()
        print('press 2 To play the game')
        print()
        print('press 3 To view your score')
        print()
        print('press 4 To exit game')
        print()
        ch=int(input('Enter your choice➜'))
        if ch==1:
            print()
            print()
            f=open("int.txt",'r')
            ch=f.read()
            print(ch)   
        if ch==2:
            c=hangman()
        if ch==3:
            print()
            print()
            print(z,'your score is',m)
        if ch==4:
            print('Thank You for Playing')
            break