import schedulingProblem as SP
import solution as SS

pr1 = SP.FJSSP(6, 2, 1.3, 1.0)

pr1.printTable()
s1 = SS.Solution(pr1)
s2 = SS.Solution(pr1)

print s1.solution.T, "\n"
print s2.solution.T





print "oldu bu is"
