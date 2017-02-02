def dispatchingRules(k,solution,problem,mid,rid,currentTime):
    dRules=list()
    dRules.append([0,"FIFO"])
    dRules.append([1,"SPT"])
    dRules.append([2,"EDD"])
    dRules.append([3,"MOOD"])
    dRules.append([4,"SPT+SRPT+SLK"])
    dRules.append([5,"ODD"])
    result=list()
    def FindOperationTime():
        pass
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
    return result




