import random
headsize=5#parameter
n=2#parameter
tailsize=headsize*(n-1)+1
dcsize=headsize
genelength=headsize+tailsize+dcsize
geneCount=1#parameter
homeoticlength=5#parameter
homeoticCount=0
chromosomelength=geneCount*genelength+homeoticCount*homeoticlength
functioset=["+","-","/","*"]
terminalset=["p","P","dd","r","Re"]
chromosome=list()
head=list()
tail=list()
dcset=list()
codingArray=[[],[],[],[]]
for j  in range (0,geneCount):
    for i in range(0,headsize):
        a=random.randint(0,1)
        print a
        if i==0:
            head.append(random.choice(functioset))
        else:
            if a==0:
                head.append(random.choice(functioset))
            else:
               head.append(random.choice(terminalset))
        dcset.append(random.randrange(0,10))
    for i in range(0,tailsize):
        tail.append(random.choice(terminalset))
    chromosome.append(head)
    chromosome.append(tail)
    chromosome.append(dcset)

for index,j in enumerate(chromosome):
    count=1
    if index%3==0:
        for i in j:
            if i in functioset:
                codingArray[1].append(count)
                codingArray[2].append(count+1)
                codingArray[3].append(0)
                count+=2
            else:
                codingArray[1].append(0)
                codingArray[2].append(0)
                codingArray[3].append(0)
for i in chromosome:
    for j in i:
        codingArray[0].append(j)
for i in range(len(codingArray[1])-1,-1,-1):
    if codingArray[1][i]==0:
        del codingArray[1][i]
        del codingArray[2][i]
        del codingArray[3][i]
    else:
        break


for i in range(len(codingArray[1])-1,-1,-1):
    x=codingArray[1][i]
    y=codingArray[2][i]
    d=""
    if x>len(codingArray[1])-1:
        a=codingArray[0][x]
        b=codingArray[0][y]
    else:
        a=codingArray[3][x]
        b=codingArray[3][y]
    c=codingArray[0][i]
    if a!=0:
        if c=="+":
            d=a+"+"+b
        elif c=='-':
            d=a+"-"+b
        elif c=="*":
            d=a+"*"+b
        elif c=="/":
            d=a+"/"+b
        else:
            print "there is wrong something"
        codingArray[3][i]=d
    else:
        codingArray[3][i]=codingArray[0][i]

    dwdw=11

print codingArray
aaa=111