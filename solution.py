import numpy as np

class Machine:
    def __init__(self):
        self.id = 0

class Operation:
    def __init__(self):
        self.id = 0
        self.machineid = 0
        self.processingTime = 0.0
        self.oreleaseTime = 0
        self.ostartTime = -1
        self.ofinishTime = 0


class Job:
    def __init__(self):
        self.id = 0
        self.operations = list()
        self.startTime = -1
        self.finishTime = 0


class Solution(Operation, Job, Machine):
    def __init__(self, problem):
        self.jobs = list()
        self.solution = list()

        totalNumberofOperations = 0
        for j in problem.jobs:
            sjob = Job()
            sjob.id = j.id

            for o in j.operations:
                sop = Operation()
                sop.id = o.id
                sjob.operations.append(sop)
            totalNumberofOperations += len(sjob.operations)
            self.jobs.append(sjob)


        allOperations = []

        index = 0
        for job in problem.jobs:
            for o in job.operations:
                allOperations.append([job.id,0,0])
                index +=1

        randomSolution = np.random.permutation(allOperations)

        for job in self.jobs:
            for o in job.operations:
                jId = job.id
                oId = o.id
                numberOfMachine = len(problem.jobs[jId].operations[oId].machineSet)

                index = np.random.randint(0, numberOfMachine)
                machineId = problem.jobs[jId].operations[oId].machineSet[index].id
                self.jobs[jId].operations[oId].machineid = machineId
                processingTime = problem.jobs[jId].operations[oId].processingTimes[index]
                self.jobs[jId].operations[oId].processingTime = processingTime
                #print job.id,"\t", o.id, "\t", o.machineid
        processingTimes=[]
        indexSet = np.zeros(problem.nj)
        for o in randomSolution:
            o[1] = indexSet[o[0]]
            indexSet[o[0]] = indexSet[o[0]]+ 1
            o[2] = self.jobs[o[0]].operations[o[1]].machineid
            processingTimes.append(self.jobs[o[0]].operations[o[1]].processingTime)

        sol = []
        for si, s in enumerate(randomSolution):
            sol.append([s[0], s[1], s[2], processingTimes[si]])

        self.solution = sol







'''
def simulation(a, eList, ct, generation):
    notFinishO = list()
    AssignedOperation = list()
    eventlist = list()
    Mwlw = list()
    Amachine = list()
    for i in range(generation.nj):
        Amachine.append([i, 0])
    print Amachine
    for i in eList:
        eventlist.append(i)
    # eventList.sort(key=lambda tup: tup[2])
    print eventlist
    for i in a:
        for j in i.operations:
            notFinishO.append([i.id, j.id])
    preAllocation()
    # findNotFinishO(notFinishO,a,ct) is it necessary?

    while len(notFinishO) >= 1:
        ct = findNextTime(eventlist, AssignedOperation, ct)
        print "current time", ct
        LeastWaitingTimeAssignment(a, eventlist, ct, Amachine)
        break


def preAllocation():
    freeMachineSet = list()
    releasedOperationSet = list()


def findNotFinishO(notFO, a, ct):
    for i in notFO:
        pass


def findNextTime(a, AO, ct):
    y = min(a, key=lambda tup: tup[2])
    z = y[2]
    if z > ct:
        ct = z
        y[3] = ct
        AO.append(y)  # operasyonun atama zamani ct olarak degistirildi
    return ct


def findReleasedOperationSet(a):
    pass


def LeastWaitingTimeAssignment(a, eventlist, ct, Amachine):
    y = min(eventlist, key=lambda tup: tup[2])
    print "ilk eleman", y
    for i in a:
        if y[0] == i.id:
            for j in i.operations:
                if y[1] == j.id:
                    k = j.machineSet
                    x = 0  # index i tutabilmek icin
                    minp = 100000
                    for l in k:
                        if l.Mlft != 0:
                            wm1 = 1
                        else:
                            wm1 = 0
                        wm2 = l.Mwlwm
                        wm3 = j.processingTimes[x]
                        wm = wm1 + wm2 + wm3
                        print "makineid", l.id
                        x = x + 1
                        if wm < minp:
                            minp = wm
                            a = l.id

                        print "wm", wm
                    print "m.id", a
                    l.Mao.append([a, (str(i.id) + str(j.id))])
                    l.Mlst.append([a, y[3]])
                    print l.Mao, l.Mlst


ss = simulation(pr1.jobs, pr1.eventList, 0, pr1)
'''
