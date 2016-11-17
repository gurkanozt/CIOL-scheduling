import numpy as np

class FJSSP:
    class machine:
        def __init__(self):
            self.id = 0
            self.MTBF = 0
            self.MTTR = 0


    class operation:
        def __init__(self):
            self.id = 0
            self.machineSet = list()
            self.processingTimes = list()

    class job:
        def __init__(self):
            self.id = 0
            self.operations = list()
            self.releaseTime = 0
            self.dueDate=0

    def __init__(self,nm, nj, c, fr):
        self.nj = nj
        self.nm = nm
        self.c = c
        self.fr=fr
        self.jobs = list()
        self.averageProcessingTime =0
        for j in range(nj):
            job = self.job()
            job.id=j
            numberOfOperations = self.nm
            for o in range(numberOfOperations):
                numberOfMachines = 1+np.random.randint(0,fr*self.nm)
                operation = self.operation()
                operation.id= o
                machineSetPermutation = np.random.permutation(self.nm)[:numberOfMachines]
                for m in machineSetPermutation:
                    machine = self.machine()
                    machine.id = m
                    operation.machineSet.append(machine)
                    t = np.random.uniform((self.nm)/2, (self.nm)*2)
                    operation.processingTimes.append(t)
                job.operations.append(operation)

            if self.nj>=50:
                realeaseTime = np.random.uniform(0, 40)
            else:
                realeaseTime = np.random.uniform(0, 20)
            job.releaseTime = realeaseTime

            job.averageProcessingTime=0
            for o in job.operations:
                job.averageProcessingTime += np.average(o.processingTimes)

            dueDate = realeaseTime + self.c * job.averageProcessingTime
            job.dueDate = dueDate

            self.jobs.append(job)

        #print "aaaaa",self.machines

    def printTable(self):
        for j in self.jobs:
            print "JOB :\t", j.id, "\t", round(j.releaseTime,2), round(j.dueDate,2),"\n"
            for o in j.operations:
                ma=""
                for j in range(len(o.machineSet)):
                    ma += "(" + str(o.machineSet[j].id) + "," + str(round(o.processingTimes[j],2)) + ") \t"
                print o.id, "\t\t", ma
            print "\n"

