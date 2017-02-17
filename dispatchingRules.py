def dispatchingRules(k,solution,problem,mid,rid,currentTime,GRules):
    dRules=list()
    dRules.append([0,"FIFO"])
    dRules.append([1,"SPT"])
    dRules.append([2,"EDD"])
    dRules.append([3,"MOOD"])
    dRules.append([4,"SPT+SRPT+SLK"])
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
            a=operationProcessingTime+remainingProcessingTime+(dDate-remainingProcessingTime-currentTime)
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
    '''

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
        if SLK>=0:
            SOPN=SLK/LRnOps
        else:
            SOPN=SLK*LRnOps
        COVERT=max(1-(max(SLK,0)/2*remainingProcessingTime),0)/operationProcessingTime
        MODD=max(rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime,operationProcessingTime+currentTime)
        OOD=rTime +((dDate-rTime)*remainingProcessingTime)/ntotalProcessingTime
        #a=eval(dRules[rid][1])#it is worked main promram
        a=eval(GRules[rid].fenotip[3][0])#it is worked with GA
        decisonList.append([mindex,a])
    z= min(decisonList, key=lambda tup: tup[1])
    index=z[0]
    result.append([k[index][0],k[index][1],mid])
    '''
    if rid==7:
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
            p=operationProcessingTime
            P=totalProcessingTime
            dd=dDate
            r=rTime
            SLK=dDate-currentTime-rTime
            CR=(dDate-currentTime)/remainingProcessingTime
            ODD=rTime+((dDate-rTime)*remainingProcessingTime)/totalProcessingTime
            CRODD=(ODD-currentTime)/totalProcessingTime
            a=eval(dRules[rid][1])
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
    if rid==8:
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
            p=operationProcessingTime
            P=totalProcessingTime
            dd=dDate
            r=rTime
            SLK=dDate-currentTime-rTime
            CR=(dDate-currentTime)/remainingProcessingTime
            ODD=rTime+((dDate-rTime)*remainingProcessingTime)/totalProcessingTime
            CRODD=(ODD-currentTime)/totalProcessingTime
            a=eval(dRules[rid][1])
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
    if rid==9:
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
            p=operationProcessingTime
            P=totalProcessingTime
            dd=dDate
            r=rTime
            SLK=dDate-currentTime-rTime
            CR=(dDate-currentTime)/remainingProcessingTime
            ODD=rTime+((dDate-rTime)*remainingProcessingTime)/totalProcessingTime
            CRODD=(ODD-currentTime)/totalProcessingTime
            a=eval(dRules[rid][1])
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
    if rid==10:
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
            p=operationProcessingTime
            P=totalProcessingTime
            dd=dDate
            r=rTime
            SLK=dDate-currentTime-rTime
            CR=(dDate-currentTime)/remainingProcessingTime
            ODD=rTime+((dDate-rTime)*remainingProcessingTime)/totalProcessingTime
            CRODD=(ODD-currentTime)/totalProcessingTime
            a=eval(dRules[rid][1])
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
    if rid==11:
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
            SLK=dDate-currentTime-rTime
            CR=(dDate-currentTime)/remainingProcessingTime
            ODD=rTime+((dDate-rTime)*remainingProcessingTime)/totalProcessingTime
            CRODD=(ODD-currentTime)/totalProcessingTime
            a=eval(dRules[rid][1])
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
    if rid==12:
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
            p=operationProcessingTime
            P=totalProcessingTime
            dd=dDate
            r=rTime
            SLK=dDate-currentTime-rTime
            CR=(dDate-currentTime)/remainingProcessingTime
            ODD=rTime+((dDate-rTime)*remainingProcessingTime)/totalProcessingTime
            CRODD=(ODD-currentTime)/totalProcessingTime
            a=eval(dRules[rid][1])
            decisonList.append([mindex,a])
        z= min(decisonList, key=lambda tup: tup[1])
        index=z[0]
    '''
    return result




