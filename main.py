import schedulingProblem as SP
import solution as SS
import TransformPermutaionToSolution as TS
import createSolution as CS

flexible=[0.2,0.5,1]
dueDateParameter=[1.2,1.5,2,0]
jobAndMachine=[[10,5],[20,5],[50,5],[20,10],[50,10],[100,10],[50,15],[100,15],[200,15]]
for i in flexible:
    for j in dueDateParameter:
        for k in jobAndMachine:
            pr1 = SP.FJSSP(k[1], k[0], j, i)#generate problem
            pr1.printTable()#call print function from schedulingProblem file
            s1 = SS.Solution(pr1)#call solution function from solution file
            cs1 = CS.createSolution(pr1,s1)
            #s2 = cs1.randomSolution(s1)
            #cs1.initialization()
            ab=cs1.simulatedSolution()

            #a=TS.tranformation(pr1,ab)#call transformation function from TranformPermutationToSolution file
            #print s1.order, "\n"#print solution



print "oldu bu is"
