import math
def Evaluation(solution):
    def MAL():
        mal=0
        for i in solution.jobs:
            duedate=i.dueDate
            finishedTime=i.operations[-1].oft
            mal+= abs(duedate-finishedTime)
        mal=mal/len(solution.jobs)
        return mal

    def MSL():
        msl=0
        for i in solution.jobs:
            duedate=i.dueDate
            finishedTime=i.operations[-1].oft
            msl+=math.pow((duedate-finishedTime),2)
        msl=msl/len(solution.jobs)
        return msl

    a=MAL()
    b=MSL()
    return a,b