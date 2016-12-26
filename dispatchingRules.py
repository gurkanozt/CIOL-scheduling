def dispatchingRules(k,solution,problem,mid,rid):
    dRules=list()
    dRules.append([0,"FIFO"])
    dRules.append([1,"SPT"])
    dRules.append([2,"EDD"])
    dRules.append([3,"MDD"])
    dRules.append([4,"CR"])
    result=list()
    if rid==0:
        result.append([k[0][0],k[0][1],mid])
    if rid==1:
        oProccesingTime=list()
        for mindex,j in enumerate(k):
            for index,m in enumerate(problem.jobs[j[0]].operations[j[1]].machineSet):
                if m.id==mid:
                    order=index
            oProccesingTime.append([mindex,problem.jobs[j[0]].operations[j[1]].machineSet[order]])
        z= min(oProccesingTime, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    if rid==2:
        duedate=list()
        for mindex,j in enumerate(k):
            m=problem.jobs[j[0]].dueDate
            duedate.append([mindex,m])
        z= min(duedate, key=lambda tup: tup[1])
        index=z[0]
        result.append([k[index][0],k[index][1],mid])
    return result




