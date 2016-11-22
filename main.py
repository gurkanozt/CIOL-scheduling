import schedulingProblem as SP
import solution as SS
import TransformPermutaionToSolution as TS
import createSolution as CS



pr1 = SP.FJSSP(6, 5, 1.1, 1.0)#generate problem
cs1 = CS.createSolution(pr1)
pr1.printTable()#call print function from schedulingProblem file
s1 = SS.Solution(pr1)#call solution function from solution file
s1 = cs1.randomSolution(s1)
cs1.initialization()


a=TS.tranformation(pr1,s1)#call transformation function from TranformPermutationToSolution file
print s1.order, "\n"#print solution



print "oldu bu is"
