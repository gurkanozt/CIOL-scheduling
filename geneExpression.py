from __future__ import division
import random
def GeneExtraction(k,solution,problem,mid,rid,currentTime):
    visit=0
    GeneticRules=list()
    result=list()
    if visit==0:
        for i in range(0,10):
            headsize=10#parameter
            n=2#parameter
            tailsize=headsize*(n-1)+1
            dcsize=headsize
            genelength=headsize+tailsize+dcsize
            geneCount=1#parameter
            homeoticlength=5#parameter
            homeoticCount=0
            chromosomelength=geneCount*genelength+homeoticCount*homeoticlength
            functioset=["+","-","*"]
            terminalset=["p","P","dd","r","Re"]
            chromosome=list()
            head=list()
            tail=list()
            dcset=list()
            codingArray=[[],[],[],[]]
            for j  in range (0,geneCount):
                for i in range(0,headsize):
                    a=random.randint(0,1)
                    #print a
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

            count=1
            countoperation=0
            countparameter=0
            for j in chromosome[0]:

                    #if j[1] not in functioset and j[2] not in functioset:
                        #a=3
                if countparameter<=countoperation:#if countparameters are bigger than countoperations in any step, branching will finish
                    if j in functioset:
                        codingArray[1].append(count)
                        codingArray[2].append(count+1)
                        codingArray[3].append(0)
                        count+=2
                        countoperation+=1
                    else:
                        codingArray[1].append(0)
                        codingArray[2].append(0)
                        codingArray[3].append(0)
                        countparameter+=1
                else:
                    break
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
                if x!=0:
                    if x>len(codingArray[1])-1:
                        a=codingArray[0][x]
                    else:
                        a=codingArray[3][x]
                    if y>len(codingArray[1])-1:
                        b=codingArray[0][y]

                    else:
                        b=codingArray[3][y]
                    c=codingArray[0][i]
                    if a!=0 and b!=0:
                        if c=="+":
                            d=a+"+"+b
                        elif c=='-':
                            d=a+"-"+b
                        elif c=="*":
                            d=a+"*"+b
                        #elif c=="/":
                            #d=a+"/"+b
                        else:
                            print "there is wrong something"

                        codingArray[3][i]="("+d+")"
                else:
                    codingArray[3][i]=codingArray[0][i]
            GeneticRules.append(codingArray[3][0])
            visit+=1

    decisonList=list()
    for mindex,j in  enumerate(k):
        dDate=problem.jobs[j[0]].dueDate
        rTime=problem.jobs[j[0]].releaseTime
        totalProcessingTime=problem.jobs[j[0]].averageProcessingTime
        pastProcessingTimes=0
        for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
            if m.id==mid:
                order=index
        operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
        for i in solution.jobs[j[0]].operations:
            if i.id<j[1]:
                pastProcessingTimes+=i.processingTime
        remainingProcessingTime=totalProcessingTime-pastProcessingTimes


        p=operationProcessingTime
        P=totalProcessingTime
        dd=dDate
        r=rTime
        Re=remainingProcessingTime

        GDR=GeneticRules[rid]
        a=eval(GDR)
        decisonList.append([mindex,a])

    z= min(decisonList, key=lambda tup: tup[1])
    index=z[0]
    result.append([k[index][0],k[index][1],mid])
    return result


