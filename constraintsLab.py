#!/usr/bin/env python3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import constraint
import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Task 1    
def Travellers(pairList):
  #Initial setup, registering variables and domains
  problem = constraint.Problem()
  time_List = ['2:30','3:30','4:30','5:30']
  destination_List =['peru','romania','taiwan','yemen']
  traveller_List = ['claude','olga','pablo','scott']
  t_variables = list(map((lambda x: 't_'+ x), traveller_List))
  d_variables = list(map((lambda x: 'd_'+ x), traveller_List))
  problem.addVariables(t_variables, time_List)
  problem.addVariables(d_variables, destination_List)
  
  #adding the basic premises of the problem
  problem.addConstraint(constraint.AllDifferentConstraint(), t_variables)
  problem.addConstraint(constraint.AllDifferentConstraint(),d_variables)
  
  #adding constraints 2-5 of the problem:
  #Claude is either leaving at 2:30 or 3:30:
  for traveller in traveller_List:
    problem.addConstraint((lambda x,y:((x!=y) or (x == '2:30') or (x == '3:30'))),['t_'+traveller, 't_claude'])
  #Person at 2:30 is leaving from Peru:
  for traveller in traveller_List:
    problem.addConstraint((lambda x,y:((x!='peru') or (y == '2:30'))),['d_'+traveller, 't_'+traveller])
  #Person flying from Yemen is flying earlier than that of the person flying from Taiwan:
  for traveller in traveller_List:
    for t in traveller_List:
      problem.addConstraint((lambda x,y,t1,t2:((x != 'yemen' or y!='taiwan') or (t1[0]<t2[0]))), ['d_'+traveller, 'd_'+t, 't_'+traveller, 't_'+t]) 
  #4 travellers are {Pablo, Yemen Traveller, person leaving at 2:30 and person leaving at 3:30}
  for traveller in traveller_List:
    problem.addConstraint((lambda x,y,z,w: ((w=='yemen' or (z=='2:30' or z=='3:30')) or (z==x and w==y))),['t_pablo', 'd_pablo','t_'+ traveller, 'd_'+traveller])
  # Olga is leaving 2 hours before the traveller from Yemen
  #for person in traveller_List:
  #  problem.addConstraint((lambda x,y,z:(y != 'yemen')or (((x == '4:30') and (z == '2:30'))or ((x == '5:30') and (z == '3:30')))), ['t_'+person, 'd_'+person, 't_olga'])
  #print(problem.getSolutions())
  #Adding constraints of pairlist:
  #for person, specs in pairList:
  #  for traveller in traveller_List:
  #    if(specs in time_List):
  #      problem.addConstraint((lambda x: (traveller!=person) or (x==specs)),['t_'+traveller])
  #    else:
  #      problem.addConstraint((lambda y: (traveller!=person) or (y==specs)),['d_'+traveller])
  for i in range(len(pairList)):
    addPairList(problem, pairList[i][0], pairList[i][1],time_List)
  return problem.getSolutions()

def addPairList(problem,person, specs, time_List):
  if(specs in time_List):
    problem.addConstraint((lambda x: (x==specs)),['t_'+person])
  else:
    problem.addConstraint((lambda x: (x==specs)),['d_'+person])
  
# Task 2
def CommonSum(n):
  return 0


from constraint import *
# Task 3
def MSquares(n, pairList):
  return constraint.Problem().getSolutions()


# Task 4
def PMSquares(n, pairList):
  return constraint.Problem().getSolutions()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# debug run
if __name__ == '__main__':
  if len(sys.argv) > 2:
    cmd = "{}({})".format(sys.argv[1], ",".join(sys.argv[2:]))
    print("debug run:", cmd)
    ret = eval(cmd)
    print("ret value:", ret)
    try:
      cnt = len(ret)
      print("ret count:", cnt)
    except TypeError:
      pass
  else:
    sys.stderr.write("Usage: {} <FUNCTION> <ARG>...\n".format(sys.argv[0]))
    sys.exit(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et ts=2 sw=2:
