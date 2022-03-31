#!/usr/bin/python3

import re
import os
import sys
debug = True

lines = sys.stdin.readlines()
lemma = sys.argv[1]

# INPUT:
# - lines contain a list of "%i:goal" where "%i" is the index of the goal
# - lemma contain the name of the lemma under scrutiny
# OUTPUT:
# - (on stdout) a list of ordered index separated by EOL


rank = []             # list of list of goals, main list is ordered by priority
maxPrio = 110
for i in range(0,maxPrio):
  rank.append([])



if re.match('.*orrect.*', lemma):
  print ("applying oracle to "+str(lemma))
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*UserReaction.*', line): rank[109].append(num)
    elif re.match('.*KU\( ~x.*', line): rank[105].append(num)
    elif re.match('.*KU\( \'g\'.*', line): rank[105].append(num)
    elif re.match('.*!Ltk.*', line): rank[100].append(num)
    elif re.match('.*!Pk.*', line): rank[100].append(num)
    elif re.match('.*DHgen.*', line): rank[95].append(num)
    elif re.match('.*State.*Init.*', line): rank[90].append(num)
    elif re.match('.*StatePC.*', line): rank[90].append(num)
    elif re.match('.*StateCD.*', line): rank[80].append(num)
    elif re.match('.*StateWSS.*', line): rank[70].append(num)
    elif not(re.match('.*splitEqs.*', line)): rank[10].append(num)
    elif re.match('.*splitEqs.*', line): rank[0].append(num)

else:
    print ("not applying the rule to: "+str(lemma))
    exit(0)

# Ordering all goals by ranking (higher first)
for listGoals in reversed(rank):
  for goal in listGoals:
    sys.stderr.write(goal)
    print (goal)
