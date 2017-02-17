import schedulingProblem as SP
import solution as SS
import TransformPermutaionToSolution as TS
import createSolution as CS
import timeit



#Your statements here

def Main(GeneticRules):

    start = timeit.default_timer()
    #GeneticRules=GeneticRules
    flexible=[0.2,0.5,1]
    dueDateParameter=[1.2,1.5,2,0]
    #jobAndMachine=[[10,5],[20,5],[50,5],[20,10],[50,10],[100,10],[50,15],[100,15],[200,15]]
    jobAndMachine=[[1000,10]]

    for h in range(0,1):
        for i in flexible:
            for j in dueDateParameter:
                for index,k in enumerate(jobAndMachine):
                    pr1 = SP.FJSSP(k[1], k[0], j, i)#generate problem
                    #pr1.printTable()#call print function from schedulingProblem file
                    s1 = SS.Solution(pr1)#call solution function from solution file
                    cs1 = CS.createSolution(pr1,s1,index,GeneticRules)
                    #s2 = cs1.randomSolution(s1)
                    #cs1.initialization()
                    Result=cs1.simulatedSolution()
                    #a=TS.tranformation(pr1,ab)#call transformation function from TranformPermutationToSolution file
                    #print s1.order, "\n"#print solution
                print timeit.default_timer()-start

    print Result
    print "oldu bu is"
    stop = timeit.default_timer()
    print stop-start
    return Result
