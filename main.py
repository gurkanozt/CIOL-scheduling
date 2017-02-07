import schedulingProblem as SP
import solution as SS
import TransformPermutaionToSolution as TS
import createSolution as CS
import genetikAlgoritma as GA
import timeit

start = timeit.default_timer()

#Your statements here


flexible=[0.2]
dueDateParameter=[1.2]
jobAndMachine=[[10,5],[20,5],[50,5],[20,10],[50,10],[100,10],[50,15],[100,15],[200,15]]
Result=list()
for i in flexible:
    for j in dueDateParameter:
        for index,k in enumerate(jobAndMachine):
            pr1 = SP.FJSSP(k[1], k[0], j, i)#generate problem
            #pr1.printTable()#call print function from schedulingProblem file
            s1 = SS.Solution(pr1)#call solution function from solution file
            cs1 = CS.createSolution(pr1,s1,index)
            #s2 = cs1.randomSolution(s1)
            #cs1.initialization()
            ab=cs1.simulatedSolution()
            Result.append(ab)
            #a=TS.tranformation(pr1,ab)#call transformation function from TranformPermutationToSolution file
            #print s1.order, "\n"#print solution
        print timeit.default_timer()-start
#

print Result
print "oldu bu is"
x=GA.GenetikOperations(Result)
stop = timeit.default_timer()
print stop-start
