import numpy as np

class createSolution:

    def __init__(self, problem):
        self.notReleasedOpSet = list()
        self.releasedOpSet = list()
        self.notFinishedOpSet = list()
        self.freeMahchinesSet = list()
        self.nextEventsSet = list()
        self.machineWaitingList = list()
        self.problem = problem


    def initialization(self):


        for j in self.problem.jobs:
            for o in j.operations:
                self.notFinishedOpSet.append([j.id, o.id])

        self.notReleasedOpSet = self.notFinishedOpSet

        for m in range(self.problem.nm):
            self.freeMahchinesSet.append(m)
            self.machineWaitingList.append([])

        # ilk released olan isi bul, ilgili operasyonu releasedOpSet'e ata



    def update(self):
        pass

    def simulatedSolution(self, solution, type):
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