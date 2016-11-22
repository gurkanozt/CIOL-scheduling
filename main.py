import schedulingProblem as SP
import solution as SS
import TransformPermutaionToSolution as TS


pr1 = SP.FJSSP(6, 5, 1.1, 1.0)#generate problem

pr1.printTable()#call print function from schedulingProblem file
s1 = SS.Solution(pr1)#call solution function from solution file
s2 = SS.Solution(pr1)
a=TS.tranformation(pr1,s1)#call transformation function from TranformPermutationToSolution file
print s1.solution, "\n"#print solution
print s2.solution

print "oldu bu is"
