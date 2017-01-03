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
        self.nj = nj#number of jobs
        self.nm = nm#number of machines
        self.c = c#tightness factor
        self.fr=fr#flexiblity rate
        self.jobs = list()#jobs set in problem set
        self.averageProcessingTime =0
        #self.createDataFSSP()#create data for FJSSP
        #self.createDataFJSSP()
        self.readJSSP()
    def createDataFSSP(self):#create data for FJSSP
        for j in range(self.nj):
            job = self.job()#define job as class
            job.id=j# assign jobs id
            numberOfOperations = self.nm#assign each job operations number
            m=0
            for o in range(numberOfOperations):
                numberOfMachines =1#assign each operation assignable machines number
                operation = self.operation()#define operation as class
                operation.id= o#assign operations id
                machine = self.machine()#define machine as class
                machine.id = m#assign machine id
                m+=1
                operation.machineSet.append(machine)#add machine objects to operations assignable machines set
                t = np.random.uniform((self.nm)/2, (self.nm)*2)#define each operations processing time
                operation.processingTimes.append(t)#add processing time to each operation
                job.operations.append(operation)#add operation objects to jobs

            if self.nj>=50:
                releaseTime = np.random.uniform(0, 40)#generate jobs release time
            else:
                releaseTime = np.random.uniform(0, 20)
            job.releaseTime = releaseTime#assign release time to jobs

            job.averageProcessingTime=0
            for o in job.operations:
                job.averageProcessingTime += np.average(o.processingTimes)#calculate jobs average processing time

            dueDate = releaseTime + self.c * job.averageProcessingTime#calculate jobs due date according to TWK method
            job.dueDate = dueDate#assign due date to jobs

            self.jobs.append(job)#add job object to jobs set
    def createDataFJSSP(self):#create data for FJSSP
        for j in range(self.nj):
            job = self.job()#define job as class
            job.id=j# assign jobs id
            numberOfOperations = self.nm#assign each job operations number
            for o in range(numberOfOperations):
                numberOfMachines = 1+np.random.randint(0,self.fr*self.nm)#assign each operation assignable machines number
                operation = self.operation()#define operation as class
                operation.id= o#assign operations id
                machineSetPermutation = np.random.permutation(self.nm)[:numberOfMachines]#assign each operation assignable machines set
                for m in machineSetPermutation:
                    machine = self.machine()#define machine as class
                    machine.id = m#assign machine id
                    operation.machineSet.append(machine)#add machine objects to operations assignable machines set
                    t = np.random.uniform((self.nm)/2, (self.nm)*2)#define each operations processing time
                    operation.processingTimes.append(t)#add processing time to each operation
                job.operations.append(operation)#add operation objects to jobs

            if self.nj>=50:
                releaseTime = np.random.uniform(0, 40)#generate jobs release time
            else:
                releaseTime = np.random.uniform(0, 20)
            job.releaseTime = releaseTime#assign release time to jobs

            job.averageProcessingTime=0
            for o in job.operations:
                job.averageProcessingTime += np.average(o.processingTimes)#calculate jobs average processing time

            dueDate = releaseTime + self.c * job.averageProcessingTime#calculate jobs due date according to TWK method
            job.dueDate = dueDate#assign due date to jobs

            self.jobs.append(job)#add job object to jobs set
    def readJSSP(self):
        f = open("1.csv", "r")
        row=1
        for line in f:
            lines=line.split(';')
            if row ==1:
                self.nj=int(lines[0])
                self.nm=int(lines[1])

            else:
                job = self.job()#define job as class
                job.id=row-2# assign jobs id
                numberOfOperations = self.nm

                lines=line.split(';')
                for j in range(0,len(lines)-1,2):
                    operation = self.operation()#define operation as class
                    operation.id=j/2 #assign operations id
                    machine = self.machine()#define machine as class
                    machine.id = int(lines[j])#assign machine id
                    operation.machineSet.append(machine)#add machine objects to operations assignable machines set
                    t = float(lines[j+1])#define each operations processing time
                    operation.processingTimes.append(t)#add processing time to each operation
                    job.operations.append(operation)#add operation objects to jobs
                if self.nj>50:
                    releaseTime = np.random.uniform(0, 40)#generate jobs release time
                else:
                    releaseTime = np.random.uniform(0, 20)
                job.releaseTime = releaseTime#assign release time to jobs

                job.averageProcessingTime=0
                for o in job.operations:
                    job.averageProcessingTime += o.processingTimes[0]#calculate jobs average processing time

                dueDate = releaseTime + self.c * job.averageProcessingTime#calculate jobs due date according to TWK method
                job.dueDate = dueDate#assign due date to jobs
                self.jobs.append(job)
            row+=1


    def printTable(self):# print problem set
        for j in self.jobs:
            print "JOB :\t", j.id, "\t", round(j.releaseTime,2), round(j.dueDate,2),"\n"
            for o in j.operations:
                ma=""
                for j in range(len(o.machineSet)):
                    ma += "(" + str(o.machineSet[j].id) + "," + str(round(o.processingTimes[j],2)) + ") \t"
                print o.id, "\t\t", ma
            print "\n"

