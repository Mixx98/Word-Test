import random

def out(correct,count):
    print("\n\n============================================\n")
    print("\t\t정답률 = %d/%d"%(correct,count))


def ord(list,a):
    correct=0
    count=0
    
    if(a=='1'):
        print("\n============================================\n")
        for i in list:
            print("\n%d. %s"%(count+1,i[1]))
            ans=input(">> ")
            if(ans==i[0]):
                correct+=1
            count+=1
        out(correct,count)
    
    elif(a=='2'):
        print("\n============================================\n")
        for i in list:
            print("\n%d. %s"%(count+1,i[0]))
            ans=input(">> ")
            if(ans==i[1]):
                correct+=1
            count+=1
        out(correct,count)
        
        
def rand(list,a):
    correct=0
    count=0
    list2=list.copy()
    
    if(a=='1'):
        print("\n============================================\n")
        while(len(list2)!=0):
            i=(random.choice(list2))
            print("\n%d. %s"%(count+1,i[1]))
            ans=input(">> ")
            if(ans==i[0]):
                correct+=1
            count+=1
            list2.remove(i)
        out(correct,count)
    
    elif(a=='2'):
        print("\n============================================\n")
        while(len(list2)!=0):
            i=(random.choice(list2))
            print("\n%d. %s"%(count+1,i[0]))
            ans=input(">> ")
            if(ans==i[1]):
                correct+=1
            count+=1
            list2.remove(i)
        out(correct,count)
        

myFile=open("C:\VS CODE\Word Test\word.txt","r",encoding='UTF8')

list = []
for line in myFile:
    word=(line.strip('\n')).split('=')
    word[0]=word[0].strip()
    word[1]=word[1].strip()
    list.append(word)
myFile.close()

while(1):
    print("\n============================================\n")
    a=input("\t영어(1) | 뜻(2) | 나가기(3)\n\n============================================\n\n>> ")
    if(a=='3'):
        break
    print("\n============================================\n")
    b=input("\t순서대로(1) | 랜덤(2)\n\n============================================\n\n>> ")
    if(b=='1'):
        ord(list,a)
    elif(b=='2'):
        rand(list,a)

