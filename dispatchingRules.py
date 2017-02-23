import random
def dispatchingRules(k,solution,problem,mid,rid,currentTime,GRules):
    dRules=list()
    dRules.append([0,"FIFO"])
    dRules.append([1,"SPT"])
    dRules.append([2,"EDD"])
    dRules.append([3,"MODD"])
    dRules.append([4,"SPT+LWKR+SLK"])
    dRules.append([5,"ODD"])
    dRules.append([6,"(((CR/((ODD*3)+0.000000001))*CRODD)+ODD)"])
    dRules.append([7,"(ODD+(((CRODD-Re)+Re)+1))"])
    dRules.append([8,"(ODD+Re)"])
    dRules.append([9,"(P*Re)"])
    dRules.append([10,"((ODD-(CRODD*(CRODD*CRODD)))*Re)"])
    dRules.append([11,"((dd-(CRODD*(CRODD*CRODD)))*Re)"])
    dRules.append([12,"(r+p+(2*P))"])
    dRules.append(([13,"((7*P)+(11*p)+12*(nOps+r))"]))
    result=list()
    '''
    if rid==0:
        result.append([k[0][0],k[0][1],mid])
    if rid==1:
        oProccesingTime=list()
        for mindex,j in enumerate(k):
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            oProccesingTime.append([mindex,problem.jobs[j[0]].operations[j[1]].processingTimes[order]])
        z= min(oProccesingTime, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    if rid==2:
        duedate=list()
        for mindex,j in enumerate(k):
            dDate=problem.jobs[j[0]].dueDate
            duedate.append([mindex,dDate])
        z= min(duedate, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    if rid==3:
        decisonList=list()
        for mindex,j in enumerate(k):
            dDate=problem.jobs[j[0]].dueDate
            rTime=problem.jobs[j[0]].releaseTime
            totalProcessingTime=problem.jobs[j[0]].averageProcessingTime
            pastProcessingTimes=0
            for i in solution.jobs[j[0]].operations:
                if i.id<j[1]:
                    pastProcessingTimes+=i.processingTime
            remainingProcessingTime=totalProcessingTime-pastProcessingTimes
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
            a=max(rTime +((dDate-rTime)*remainingProcessingTime)/totalProcessingTime,operationProcessingTime+currentTime)
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    if rid==4:
        decisonList=list()
        for mindex,j in enumerate(k):
            dDate=problem.jobs[j[0]].dueDate
            pastProcessingTimes=0
            totalProcessingTime=problem.jobs[j[0]].averageProcessingTime
            for i in solution.jobs[j[0]].operations:
                if i.id<j[1]:
                    pastProcessingTimes+=i.processingTime
            remainingProcessingTime=totalProcessingTime-pastProcessingTimes
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
            a=operationProcessingTime+remainingProcessingTime+(dDate-remainingProcessingTime-currentTime)#yanlis
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    if rid==5:
        decisonList=list()
        for mindex,j in enumerate(k):
            dDate=problem.jobs[j[0]].dueDate
            rTime=problem.jobs[j[0]].releaseTime
            totalProcessingTime=problem.jobs[j[0]].averageProcessingTime
            pastProcessingTimes=0
            for i in solution.jobs[j[0]].operations:
                if i.id<j[1]:
                    pastProcessingTimes+=i.processingTime
            remainingProcessingTime=totalProcessingTime-pastProcessingTimes
            a=rTime +((dDate-rTime)*remainingProcessingTime)/totalProcessingTime
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    ################################it is used for GA and DR

    decisonList=list()
    for mindex,j in enumerate(k):
        dDate=problem.jobs[j[0]].dueDate
        rTime=problem.jobs[j[0]].releaseTime
        ntotalProcessingTime=problem.jobs[j[0]].averageProcessingTime
        npastProcessingTimes=0
        for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
            if m.id==mid:
                order=index
        operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
        for i in solution.jobs[j[0]].operations:
            if i.id<j[1]:
                npastProcessingTimes+=i.processingTime
        remainingProcessingTime=ntotalProcessingTime-npastProcessingTimes
        LnOps=problem.jobs[j[0]].nOfOperations
        LRnOps=LnOps-j[1]
        TWORK=ntotalProcessingTime
        EDD=dDate
        AT=rTime
        LWKR=remainingProcessingTime
        SLK=dDate-currentTime-rTime
        CR=(dDate-currentTime)/remainingProcessingTime
        ODD=rTime+((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime
        CRODD=(ODD-currentTime)/ntotalProcessingTime
        SPT=operationProcessingTime
        SOP=(1-(SLK/LRnOps))/operationProcessingTime
        FIFO=mindex
        if SLK>=0:
            SOPN=SLK/LRnOps
        else:
            SOPN=SLK*LRnOps
        COVERT=max(1-(max(SLK,0)/2*remainingProcessingTime),0)/operationProcessingTime
        MODD=max(rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime,operationProcessingTime+currentTime)
        OOD=rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime

        a=eval(dRules[rid][1])#it is worked main promram
        #a=eval(GRules[rid].fenotip[3][0])#it is worked with GA
        decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
        '''
    ################## it is used for Dynamic rules
    decisonList=list()
    tEDD=list()
    tr=list()
    tP=list()
    tp=list()
    tCR=list()
    tCRODD=list()
    tODD=list()
    tMODD=list()
    tSLK=list()
    tRe=list()
    for mindex,j in enumerate(k):

        dDate=problem.jobs[j[0]].dueDate
        rTime=problem.jobs[j[0]].releaseTime
        ntotalProcessingTime=problem.jobs[j[0]].averageProcessingTime
        npastProcessingTimes=0
        for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
            if m.id==mid:
                order=index
        operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
        for i in solution.jobs[j[0]].operations:
            if i.id<j[1]:
                npastProcessingTimes+=i.processingTime
        remainingProcessingTime=ntotalProcessingTime-npastProcessingTimes
        tRe.append(remainingProcessingTime)
        #LnOps=problem.jobs[j[0]].nOfOperations
        #LRnOps=LnOps-j[1]
        #TWORK=ntotalProcessingTime
        tEDD.append(dDate)
        #AT=rTime
        tr.append(rTime)
        tp.append(operationProcessingTime)
        tP.append(ntotalProcessingTime)
        #LWKR=remainingProcessingTime
        tSLK.append(dDate-currentTime-rTime)
        tCR.append((dDate-currentTime)/remainingProcessingTime)
        aODD=rTime+((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime
        tODD.append(rTime+((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime)
        tCRODD.append((aODD-currentTime)/ntotalProcessingTime)
        #SPT=operationProcessingTime
        #SOP=(1-(SLK/LRnOps))/operationProcessingTime
        #FIFO=mindex
        '''
        if SLK>=0:
            SOPN=SLK/LRnOps
        else:
            SOPN=SLK*LRnOps
        '''
        #COVERT=max(1-(max(SLK,0)/2*remainingProcessingTime),0)/operationProcessingTime
        tMODD.append(max(rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime,operationProcessingTime+currentTime))
        #OOD=rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime
    minDD=min(tEDD)
    maxDD=max(tEDD)
    minp=min(tp)
    maxp=max(tp)
    minP=min(tP)
    maxP=max(tP)
    minr=min(tr)
    maxr=max(tr)
    minCR=min(tCR)
    maxCR=max(tCR)
    maxCRODD=max(tCRODD)
    minCRODD=min(tCRODD)
    maxODD=max(tODD)
    minODD=min(tODD)
    maxMODD=max(tMODD)
    minMODD=min(tMODD)
    maxSLK=max(tSLK)
    minSLK=min(tSLK)
    maxRe=max(tRe)
    minRe=min(tRe)
    for mindex,j in enumerate(k):
        #a=eval(dRules[rid][1])#it is worked main promram
        dDate=problem.jobs[j[0]].dueDate
        rTime=problem.jobs[j[0]].releaseTime
        ntotalProcessingTime=problem.jobs[j[0]].averageProcessingTime
        npastProcessingTimes=0
        for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
            if m.id==mid:
                order=index
        operationProcessingTime=problem.jobs[j[0]].operations[j[1]].processingTimes[order]
        for i in solution.jobs[j[0]].operations:
            if i.id<j[1]:
                npastProcessingTimes+=i.processingTime
        remainingProcessingTime=ntotalProcessingTime-npastProcessingTimes
        xRe=remainingProcessingTime
        xSLK=(dDate-currentTime-rTime)
        xCR=((dDate-currentTime)/remainingProcessingTime)
        xODD=(rTime+((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime)
        xCRODD=(xODD-currentTime)/ntotalProcessingTime
        xMODD=(max(rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime,operationProcessingTime+currentTime))
        DD=(dDate-minDD)/(maxDD-minDD+0.00000001)
        p=(operationProcessingTime-minp)/(maxp-minp+0.00000001)
        P=(ntotalProcessingTime-minP)/(maxP-minP+0.00000001)
        r=(rTime-minr)/(maxr-minr+0.00000001)
        CR=(xCR-minCR)/(maxCR-minCR+0.00000001)
        CRODD=(xCRODD-minCRODD)/(maxCRODD-minCRODD+0.00000001)
        ODD=(xODD-minODD)/(maxODD-minODD+0.00000001)
        MODD=(xMODD-minMODD)/(maxMODD-minMODD+0.00000001)
        SLK=(xSLK-minSLK)/(maxSLK-minSLK+0.00000001)
        Re=(xRe-minRe)/(maxRe-minRe+0.00000001)
        b=GRules[rid].genotip
        formule=""
        for i in b:
            x=eval(i[0])
            if i[1]!=-1:
                up=True
            else:
                up=False
            if i[2]!=-1:
                down=True
            else:
                down=False
            uplimit=i[4]
            downlimit=i[3]
            if up==True and down==True:
                if downlimit<= x <=uplimit:
                    formule+=i[0]+"+"
            elif up==True and down==False:
                if x<= uplimit:
                    formule+=i[0]+"+"
            elif up==False and down==True:
                if x>=downlimit:
                    formule+=i[0]+"+"
            else:
                formule+=i[0]+"+"

        if len(formule)<1:
            a=1000000000
        else:
            formule=formule[:-1]
            a=eval(formule)
        #a=eval(GRules[rid].genotip)#it is worked with GA
        decisonList.append([mindex,a])
    z= min(decisonList, key=lambda tup: tup[1])
    index=z[0]
    result.append([k[index][0],k[index][1],mid])

    return result




