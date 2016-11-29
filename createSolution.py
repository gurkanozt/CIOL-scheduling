import numpy as np

class createSolution:

    def __init__(self, problem,solution):
        self.notReleasedOpSet = list()
        self.releasedOpSet = list()
        self.notFinishedOpSet = list()
        self.freeMahchinesSet = list()
        self.nextEventsSet = list()
       # self.EventsSet = list()
        self.machineWaitingList = list()
        self.machineEventSet = list()
        self.problem = problem
        self.solution=solution
        self.currentTime=0
        self.nextTime=0
        self.assignment=list()#it is necessary to hold assigned object


    def initialization(self):

        for j in self.problem.jobs:
            for o in j.operations:
                self.notFinishedOpSet.append([j.id, o.id])
        self.notReleasedOpSet = self.notFinishedOpSet
        for m in range(self.problem.nm):
            self.freeMahchinesSet.append(m)#define machine as free
            self.machineWaitingList.append([])

        for j in self.problem.jobs:
            self.nextEventsSet.append([j.id ,0,j.releaseTime,'r'])
        z= min(self.nextEventsSet, key=lambda tup: tup[2])
        #self.releasedOpSet.append([z[0],z[1],z[2]])
        self.currentTime=z[2]
        #self.releasedOpSet.sort(key=lambda tup: tup[2])
        # ilk released olan isi bul, ilgili operasyonu releasedOpSet'e ata



    def LeastWaitingTimeAssignment(self):
        for j in self.releasedOpSet:
            for m in self.problem.jobs[j[0]].operations[j[1]].machineSet:
                if m.id not in self.freeMahchinesSet:
                  a=1
    def update(self,assignment,a):#completed
        for j in assignment:
            self.solution.jobs[j[0]].operations[j[1]].ost=self.nextTime
            mid=self.solution.jobs[j[0]].operations[j[1]].machineId
            self.solution.jobs[j[0]].operations[j[1]].oft=self.solution.jobs[j[0]].operations[j[1]].ost+self.problem.jobs[j[0]].operations[j[1]].processingTimes[a]
            self.nextEventsSet.append([j[0],j[1],self.solution.jobs[j[0]].operations[j[1]].oft,mid])
            if j[1]!=self.problem.nm:
                releaseTime=self.solution.jobs[j[0]].operations[j[1]].oft
                self.solution.jobs[j[0]].operations[j[1]+1].oreleaseTime=releaseTime
                self.nextEventsSet.append([j[0],j[1]+1,releaseTime,'r'])
            self.solution.machines[mid].mwlm.append([j[0],j[1]])
            self.solution.machines[mid].mwlwm +=self.problem.jobs[j[0]].operations[j[1]].processingTimes[a]#add workload to machine has mid
            self.solution.machines[mid].mlst=self.solution.jobs[j[0]].operations[j[1]].ost
            self.solution.machines[mid].mlft=self.solution.jobs[j[0]].operations[j[1]].oft
            self.freeMahchinesSet.remove(mid)

            #print self.solution.jobs[j[0]].id,self.solution.jobs[j[0]].operations[j[1]].id,self.solution.jobs[j[0]].operations[j[1]].machineId,self.solution.jobs[j[0]].operations[j[1]].ost,self.solution.jobs[j[0]].operations[j[1]].oft
            #print self.solution.machines[mid].mwlm,self.solution.machines[mid].mwlwm,self.solution.machines[mid].mlst,self.solution.machines[mid].mlft
            #print self.freeMahchinesSet
        #print self.nextEventsSet
    def findNextTimeandEvents(self):

        for j in self.nextEventsSet:
            if j[3]=='r' :
                self.releasedOpSet.append(j[:3])
            else:
                pass
            #self.notFinishedOpSet.remove()#how to delete a row.
            #self.freeMahchinesSet.append('machine.id')#is it True?
            #self.machineEventSet.append('machine.id')#is it True?


    def simulatedSolution(self):
        self.initialization()
        self.nextTime=self.currentTime
        z= min(self.nextEventsSet, key=lambda tup: tup[2])#job in Evenset assigned to machines randomly
        lena=len(self.problem.jobs[z[0]].operations[z[1]].machineSet)
        a=np.random.randint(0,lena)
        assignedMachineId=self.problem.jobs[z[0]].operations[z[1]].machineSet[a].id
        self.solution.jobs[z[0]].operations[z[1]].machineId=assignedMachineId
        self.solution.jobs[z[0]].operations[z[1]].ost=self.nextTime
        self.solution.jobs[z[0]].operations[z[1]].oft=self.solution.jobs[z[0]].operations[z[1]].ost+self.problem.jobs[z[0]].operations[z[1]].processingTimes[a]
        self.assignment.append([z[0],z[1],assignedMachineId])
        print self.solution.jobs[z[0]].id,self.solution.jobs[z[0]].operations[z[1]].id,self.solution.jobs[z[0]].operations[z[1]].machineId
        self.update(self.assignment,a)
        #self.nextEventsSet.remove()
        self.findNextTimeandEvents()

        while self.notFinishedOpSet>0:
            for j in self.releasedOpSet:
                if j[2]<=self.currentTime:
                    self.LeastWaitingTimeAssignment()

            pass



    def randomSolution(self, solution):
        allOperations = []  # define all operation set

        index = 0
        for job in self.problem.jobs:
            for o in job.operations:
                allOperations.append(
                    [job.id, 0, 0])  # add job id, operation id(default value=0) and machine id(default value=0)
                index += 1

        randomSolution = np.random.permutation(allOperations)  # convert allOperation set to numpy permutation

        for job in solution.jobs:
            for o in job.operations:
                jId = job.id
                oId = o.id
                numberOfMachine = len(self.problem.jobs[jId].operations[
                                          oId].machineSet)  # calculate assignable number of machine according to job id an opeation id
                index = np.random.randint(0,
                                          numberOfMachine)  # select random index between 0 and assignable number of machine
                o.machine.id = self.problem.jobs[jId].operations[oId].machineSet[
                    index].id  # assig m id that selects ramdomly assignable machine
                processingTime = self.problem.jobs[jId].operations[oId].processingTimes[
                    index]  # calculate operation process time on assigned  machine
                solution.jobs[jId].operations[oId].processingTime = processingTime  # assign this processing time to solution jobs set
                # print job.id,"\t", o.id, "\t", o.machineid

        processingTimes = []
        indexSet = np.zeros(self.problem.nj)  # define numpy zeros permutation whose lenght equals to number of jobs
        for o in randomSolution:  # generate job based permutation
            o[1] = indexSet[o[0]]
            indexSet[o[0]] = indexSet[o[0]] + 1
            o[2] = solution.jobs[o[0]].operations[o[1]].machine.id
            processingTimes.append(solution.jobs[o[0]].operations[o[1]].processingTime)

        sol = []
        for si, s in enumerate(randomSolution):  # add processing time to job based permutation
            sol.append([s[0], s[1], s[2], processingTimes[si]])

        solution.order = sol
        return solution  # assign sol set to solution set