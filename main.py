import schedulingProblem as SP
import solution as SS
import TransformPermutaionToSolution as TS


pr1 = SP.FJSSP(6, 5, 1.1, 1.0)

pr1.printTable()
s1 = SS.Solution(pr1)
s2 = SS.Solution(pr1)
a=TS.tranformation(pr1,s1)
print s1.solution, "\n"
print s2.solution

print "oldu bu is"
