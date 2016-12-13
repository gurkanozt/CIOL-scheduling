import schedulingProblem as SP
import solution as SS
import TransformPermutaionToSolution as TS
import createSolution as CS



pr1 = SP.FJSSP(3, 2, 1.1, 1)#generate problem

pr1.printTable()#call print function from schedulingProblem file
s1 = SS.Solution(pr1)#call solution function from solution file
cs1 = CS.createSolution(pr1,s1)
#s2 = cs1.randomSolution(s1)
#cs1.initialization()
cs1.simulatedSolution()


#a=TS.tranformation(pr1,s2)#call transformation function from TranformPermutationToSolution file
#print s1.order, "\n"#print solution



print "oldu bu is"
